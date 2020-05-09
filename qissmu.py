#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
#######################################################################################
#
#    ________  .___  _________ _________   _____   ____ ___
#    \_____  \ |   |/   _____//   _____/  /     \ |    |   \
#     /  / \  \|   |\_____  \ \_____  \  /  \ /  \|    |   /
#    /   \_/.  \   |/        \/        \/    Y    \    |  /
#    \_____\ \_/___/_______  /_______  /\____|__  /______/
#           \__>           \/        \/         \/
#
#######################################################################################
#
#    Copyright 2020 Freneticks
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################################
#
# Version 0.0.1
#
#######################################################################################

import argparse
import subprocess
import shutil
import shlex
import os
import runpy
import sys

configpath = os.path.join(
    os.environ.get("XDG_CONFIG_HOME") or os.path.join(os.environ["HOME"], ".config")
)

config_file = runpy.run_path(f"{configpath}/qissmu.py")  # TODO: >> importlib ?
vm = config_file["vm"]


################################### Functions #########################################


def get_vm(vm_name):
    dirty = vm[vm_name]
    return dirty.strip("\n")


def run_vm(cmd):
    cmd = shlex.split(cmd)
    qemu_path = shutil.which(cmd[0])
    if qemu_path == None:
        print(f'[!] No binary found for : "{cmd[0]}"')
        sys.exit(1)
    cmd[0] = qemu_path
    # TODO: better exit exception (exit code + message)
    process = subprocess.Popen(cmd)
    return str(process.pid)


def list():
    print("List of current VM :")
    print("===============================")
    for i in vm.keys():
        print(i)
    print("===============================")


def start(vm_name):
    try:
        cmd = get_vm(vm_name)
        print(f"Launching VM : {vm_name} ...")
        pid = run_vm(cmd)
        print(f"Process has been forked with PID : {pid}")
    except KeyError:
        print("[!] This VM doesn't exist.")


################################### Args ##############################################

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="cmd")
subparser.add_parser("list")
spp = subparser.add_parser("start")
spp.add_argument("vm_name", type=str)
args = parser.parse_args()

if args.cmd:
    if args.cmd == "list":
        list()
    elif args.cmd == "start":
        start(args.vm_name)      
    else:
        print("[!] Command not supported")
else:
    parser.print_help()