#!/usr/bin/python
# -*- coding: utf-8 -*-

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from spwd import getspnam
from traceback import format_exc


def main():
    module = AnsibleModule(argument_spec=dict(usernames=dict(
                                                type=list, required=True)))
    try:
        usernames = module.params['usernames']
        shadows_facts = dict()
        for username in usernames:
            try:
                shadow = getspnam(username)[1]
                if shadow != "!!":
                    shadows_facts[username] = shadow
            except Exception:
                pass

        module.exit_json(
            changed=False,
            shadows=shadows_facts,
        )
    except Exception as e:
        module.fail_json(msg=str(e), exception=format_exc())


if __name__ == '__main__':
    main()
