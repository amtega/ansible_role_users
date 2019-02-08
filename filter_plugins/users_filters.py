# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from crypt import crypt
from re import compile


def users_convert_chage_date_to_yyyymmdd(value):
    """Convert a chage command date value to YYYY-MM-DD format

    Args:
        value (string): the value to convert

    Returns:
        int: date converted to YYYY-MM-DD format
    """
    re = compile("(...) (..), (....)")

    # If value does not match with date format returned by chage, assume it is
    # already the number of days

    value_cleaned = value.strip()

    if not re.match(value_cleaned):
        return int(value_cleaned)

    parts = re.split(value_cleaned)

    m = parts[1].lower()
    d = parts[2]
    y = parts[3]
    months = {"jan": "01",
              "feb": "02",
              "mar": "03",
              "apr": "04",
              "may": "05",
              "jun": "06",
              "jul": "07",
              "aug": "08",
              "sep": "09",
              "oct": "10",
              "nov": "11",
              "dec": "12"}

    result = "{}-{}-{}".format(y, months[m], d)

    return result


def users_crypt(clear_password, salt):
    """Hash a clear password match using the specified salt.

    Args:
        clear_password (string): clear password to encrypt
        salt (string): salt to use

    Returns:
        string: encrypted password using the given salt
    """
    return crypt(clear_password, salt)


class FilterModule(object):
    """Ansible users filters."""

    def filters(self):
        return {
            "users_convert_chage_date_to_yyyymmdd":
                users_convert_chage_date_to_yyyymmdd,
            "users_crypt": users_crypt
        }
