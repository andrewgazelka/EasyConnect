#!/usr/bin/env python3

# alias c='sshfs $1\:/ Volumes/$1 -o noappledouble,noapplexattr,auto_cache,reconnect,defer_permissions'
import subprocess
import sys
import os


def get_server(input: str) -> str:
    split = input.split("@")
    length = len(split)
    if length == 2:
        return split[1]
    elif length == 1:
        return split[0]
    else:
        raise Exception("input not have multiple @'s")


arg: str = sys.argv[1]
server = get_server(arg)

directory = "/Volumes/" + server

if os.path.isdir(directory):
    print("Directory already exists")
else:
    subprocess.call(["sshfs", server + ":", directory, "-o",
                  "noappledouble,noapplexattr,auto_cache,reconnect,defer_permissions"])

