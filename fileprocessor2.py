#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if not line.startswith('#'):
        username, password, userid, groupid = line.strip().split(':')
        print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

