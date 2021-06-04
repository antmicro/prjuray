#!/usr/bin/env python3
# Copyright (C) 2020-2021  The Project U-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

# Header
contrib = ["""\
# Contributing to Project U-Ray
"""]

# Extract the "Contributing" section from README.md
found = False
for line in open('README.md'):
    if found:
        if line.startswith('# '):
            # Found the next top level header
            break
        contrib.append(line)
    else:
        if line.startswith('# Contributing'):
            found = True

# Footer
contrib.append("""\






----

This file is generated from [README.md](README.md), please edit that file then
run the `./.github/update-contributing.py`.

""")

open("CONTRIBUTING.md", "w").write("".join(contrib))
