#!/usr/bin/env python

import json
import os
import fnmatch
import re
import sys

IGNORE_ENTRIES = [
    'latex-workshop-dev.*',
    'latex-workshop.structure-toggle-follow-cursor',
    'latex-workshop.citation',
    'latex-workshop.log',
    'latex-workshop.showCompilationPanel',
    'latex-workshop.synctex',
    'latex-workshop.tab'
]

def get_from_package(pkgfile):
    with open(pkgfile, 'r') as fp:
        package_file_content = json.load(fp)
        variables = package_file_content['contributes']['configuration']['properties']
        commands = package_file_content['contributes']['commands']
        variable_names = set(variables.keys())
        commands_names = set([e['command'] for e in commands])
    return (variable_names, commands_names)


def get_variables_from_wiki():
    variables = set()
    for dirpath, _, filenames in os.walk('.'):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            (_, ext) = os.path.splitext(filepath)
            if ext != '.md':
                continue
            with open(f, 'r') as fp:
                content = fp.read()
                for match in re.finditer(r'latex-workshop(\.[a-zA-Z-]+)+', content):
                    if match:
                        variables.add(match.group(0))
    return variables

def print_if_not_ignored(s):
    """
    Print s if it is not in the list IGNORE_ENTRIES
    """
    if any(fnmatch.fnmatch(e, pat) for pat in IGNORE_ENTRIES):
        return
    print(s)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        print("Usage: check-config.py LW-package.json")
        sys.exit(0)

    vars_package, commands_package = get_from_package(sys.argv[1])
    vars_wiki = get_variables_from_wiki()

    print('--> Variables in package.json but not in the wiki:')
    for e in sorted(vars_package.difference(vars_wiki)):
        print_if_not_ignored("\t" + e)
    print('--> Commands in package.json but not in the wiki:')
    for e in sorted(commands_package.difference(vars_wiki)):
        print_if_not_ignored("\t" + e)
    print('--> Variables/commands in the wiki but not in package.json:')
    all_package = commands_package.union(vars_package)
    for e in sorted(vars_wiki.difference(all_package)):
        print_if_not_ignored("\t" + e)