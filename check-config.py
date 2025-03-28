#!/usr/bin/env python

import json
import os
import fnmatch
import re
import sys
import typing

IGNORE_ENTRIES = [
    'latex-workshop-dev.*',
    'latex-workshop.structure-toggle-follow-cursor',
    'latex-workshop.citation',
    'latex-workshop.setViewer',
    'latex-workshop.log',
    'latex-workshop.synctex',
    'latex-workshop.tab'
]

def get_commands_from_package(package_file_content):
    commands = package_file_content['contributes']['commands']
    commands_names = set((e['command'] for e in commands))
    return commands_names


def get_variables_from_package(package_file_content):
    all_variables = package_file_content['contributes']['configuration']['properties']
    variables = {}
    for key in all_variables.keys():
        entry = all_variables[key]
        subkeys = entry.keys()
        if 'deprecationMessage' not in subkeys and 'markdownDeprecationMessage' not in subkeys:
            variables[key] = entry['default']
    return variables


def get_variables_from_wiki():
    variables = set()
    for dirpath, _, filenames in os.walk('.'):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            (_, ext) = os.path.splitext(filepath)
            if ext != '.md':
                continue
            with open(f, 'r', encoding='utf8') as fp:
                content = fp.read()
                for match in re.finditer(r'latex-workshop(\.[a-zA-Z-]+)+', content):
                    if match:
                        variables.add(match.group(0))
    return variables

def check_equal_values(variable: str, actual: str, expected: any):
    expected = str(expected)
    # Use ' and not "
    actual = actual.replace('"', "'")
    expected = expected.replace('"', "'")
    # use lower case
    actual = actual.lower()
    expected = expected.lower()
    # | is escaped in markdown
    actual = actual.replace('\|','|')
    if actual.replace(' ', '') != expected.replace(' ', ''):
        print(f"Default value mismatch for {variable}")
        print(f'\texpected: {expected}')
        print(f'\tactual: {actual}')


def check_default_value(variable: str, default_value: str ):
    for dirpath, _, filenames in os.walk('.'):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            (_, ext) = os.path.splitext(filepath)
            if ext != '.md':
                continue
            with open(f, 'r', encoding='utf8') as fp:
                content = fp.read()
                match = re.search(r'^#{2,}\s*`' + re.escape(variable) + r'`([^#]*)(?:^#|\Z)', content, re.MULTILINE)
                if match:
                    var_description = match.group(1)
                    # Extract the default value: `text` in the second column
                    match_description = re.search(r'\|[^\|]*\|\s*`"?(.*?)"?`\s*\|', var_description, re.MULTILINE)
                    if match_description:
                        description_default = match_description.group(1)
                        # print(description_default)

                        check_equal_values(variable, description_default, default_value)

                    else:
                        print(f'No default value found for {variable}')
                    return


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

    with open(sys.argv[1], 'r', encoding='utf8') as fp:
        package_file_content = json.load(fp)

    commands_package = get_commands_from_package(package_file_content)
    vars_package = get_variables_from_package(package_file_content)
    var_names_package = set(vars_package.keys())
    vars_wiki = get_variables_from_wiki()

    print('--> Variables in package.json but not in the wiki:')
    for e in sorted(var_names_package.difference(vars_wiki)):
        print_if_not_ignored("\t" + e)
    print('--> Commands in package.json but not in the wiki:')
    for e in sorted(commands_package.difference(vars_wiki)):
        print_if_not_ignored("\t" + e)
    print('--> Variables/commands in the wiki but not in package.json:')
    all_package = commands_package.union(vars_package)
    for e in sorted(vars_wiki.difference(all_package)):
        print_if_not_ignored("\t" + e)

    for key, value in vars_package.items():
        check_default_value(key, value)
