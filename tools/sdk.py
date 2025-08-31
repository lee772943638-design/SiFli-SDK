#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# File      : sdk.py
# This file is modified from env.py which is part of RT-Thread RTOS
# COPYRIGHT (C) 2006 - 2018, RT-Thread Development Team
# SPDX-FileCopyrightText: 2025 SiFli Technologies(Nanjing) Co., Ltd
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Change Logs:
# Date           Author          Notes
# 2018-5-28      SummerGift      Add copyright information
# 2019-1-16      SummerGift      Add chinese detection
# 2020-4-13      SummerGift      refactoring
#

import os
import sys
import argparse
import logging

script_path = os.path.abspath(__file__)
mpath = os.path.dirname(script_path)
sys.path.insert(0, mpath)

from vars import Export

__version__ = 'SiFli-SDK Tool v1.0.0'

cmd_map = {
    "menuconfig": "tools/kconfig/menuconfig.py",
}

def init_argparse():
    parser = argparse.ArgumentParser(description=__doc__)
    
    available_commands = list(cmd_map.keys())
    parser.add_argument("command", choices=available_commands, help="commmand")
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="command args")

    return parser


def init_logger(env_root):
    log_format = "%(module)s %(lineno)d %(levelname)s %(message)s \n"
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(
        level=logging.WARNING,
        format=log_format,
        datefmt=date_format,
        # filename=log_name
    )


def get_env_root():
    env_root = os.getenv("ENV_ROOT")
    if env_root is None:
        # env is not used, shell is used instead
        env_root = os.getenv("SIFLI_SDK_PYTHON_ENV_PATH")
    return env_root


def get_package_root():
    package_root = os.getenv("PKGS_ROOT")
    if package_root is None:
        package_root = os.path.join(get_env_root(), 'packages')
    return package_root


def export_environment_variable():
    script_root = os.path.split(os.path.realpath(__file__))[0]
    sys.path = sys.path + [os.path.join(script_root)]
    env_root = get_env_root()
    pkgs_root = get_package_root()

    os.environ["ENV_ROOT"] = env_root
    os.environ['PKGS_ROOT'] = pkgs_root
    os.environ['PKGS_DIR'] = pkgs_root

    Export('env_root')
    Export('pkgs_root')


def exec_cmd(args):
    import subprocess

    SIFLI_SDK = os.environ.get("SIFLI_SDK")
    subprocess.run([sys.executable, os.path.join(SIFLI_SDK, f"{cmd_map[args.command]}")] + args.args, check=True)


def exec_arg(arg):

    export_environment_variable()
    init_logger(get_env_root())

    sys.argv.insert(1, arg)

    parser = init_argparse()
    args = parser.parse_args()
    
    exec_cmd(args)


def main():
    export_environment_variable()
    init_logger(get_env_root())

    parser = init_argparse()

    if (len(sys.argv) == 1):
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    exec_cmd(args)


if __name__ == '__main__':
    main()
    
