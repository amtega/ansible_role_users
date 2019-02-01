# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from datetime import datetime
from re import compile


def users_convert_value_to_days(value):
    """Convert a chage command date value to days

    Args:
        value (string): the value to convert

    Returns:
        int: date converted to numer of days since January 1st, 1970
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
    months = { "jan": 1,
               "feb": 2,
               "mar": 3,
               "apr": 4,
               "may": 5,
               "jun": 6,
               "jul": 7,
               "aug": 8,
               "sep": 9,
               "oct": 10,
               "nov": 11,
               "dec": 12 }

    start_date = datetime(1970, 1, 1)
    value_date = datetime(int(y), months[m], int(d))

    result = str(int((value_date - start_date).total_seconds() // 86400))

    return result


class FilterModule(object):
    """Ansible users filters."""

    def filters(self):
        return {
            'users_convert_value_to_days': users_convert_value_to_days
        }
