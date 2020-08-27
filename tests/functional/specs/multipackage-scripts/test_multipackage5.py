#-----------------------------------------------------------------------------
# Copyright (c) 2013-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------


# This script will use shared dependencies from multipackage5_B and multipackage5_C


# import a very simple and rarely used pure-python lib ... (shared from multipackage5_B)
import getopt
# import a module that requires .dll/.so files (shared from multipackage5_B)
import ssl
# import a module that which has package data relative to it's root (shared from multipackage5_C)
import tkinter


print('Hello World!')
