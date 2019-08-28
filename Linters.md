# Linting

## ChkTeX

The [ChkTeX](http://www.nongnu.org/chktex/) utility is a LaTeX semantic checker. Once installed, and the relevant setting enabled it is automatically run on any open TeX documents. It output is parsed by the extension and displayed in the _Problems_ panel.

Auto load of `.chktexrc` configuration files is performed in the following order

1. Manually configured `-l` setting in `chktex.args`
1. The `.chktexrc` file (if exists) in the same folder as the main LaTeX file
1. The `.chktexrc` file (if exists) at the project root folder.

## Relevant Settings

### Overview

| Setting key                                                            | Description                                             | Default                                   | Type                 |
| ---------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------- | -------------------- |
| [`latex-workshop.chktex.args.active`](#latex-workshopchktexargsactive) | Arguments to be passed to ChkTeX for **current file**   | `["-wall", "-n22", "-n30", "-e16", "-q"]` | _array_ of _strings_ |
| [`latex-workshop.chktex.args.root`](#latex-workshopchktexargsroot)     | Arguments to be passed to ChkTeX for **entire project** | `["-wall", "-n22", "-n30", "-e16", "-q"]` | _array_ of _strings_ |
| [`latex-workshop.chktex.enabled`](#latex-workshopchktexenabled)        | Enable LaTeX linting with ChkTeX                        | `false`                                   | _boolean_            |
| [`latex-workshop.chktex.interval`](#latex-workshopchktexinterval)      | Time interval in ms that ChkTeX is run                  | 300                                       | _integer_            |
| [`latex-workshop.chktex.path`](#latex-workshopchktexpath)              | Location of ChkTeX executable                           | `"chktex"`                                | _string_             |

### Details

#### latex-workshop.chktex.args.active

Linter arguments to check LaTeX syntax of the current file state in real time with ChkTeX.

Arguments must be in separate strings in the array. Additional arguments, i.e., `-I0 -f%f:%l:%c:%d:%k:%n:%m\n` will be appended when constructing the command. Current file contents will be piped to the command through stdin.

| type                 | default value                             |
| -------------------- | ----------------------------------------- |
| _array_ of _strings_ | `["-wall", "-n22", "-n30", "-e16", "-q"]` |

#### latex-workshop.chktex.args.root

Linter arguments to check LaTeX syntax of the entire project from the root file with ChkTeX.

Arguments must be in separate strings in the array. Additional arguments, i.e., `-f%f:%l:%c:%d:%k:%n:%m\n %DOC%` will be appended when constructing the command.

| type                 | default value                             |
| -------------------- | ----------------------------------------- |
| _array_ of _strings_ | `["-wall", "-n22", "-n30", "-e16", "-q"]` |

#### latex-workshop.chktex.enabled

Enable linting LaTeX with ChkTeX.

The active document will be linted when no document changes for a defined period of time.

The full project will be linted from the root on file save.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.chktex.interval

Defines the time interval in milliseconds between invoking LaTeX linter on the active file.

| type      | default value |
| --------- | ------------- |
| _integer_ | 300           |

#### latex-workshop.chktex.path

Define the location of ChkTeX executive file.

This command will be joint with `latex-workshop.chktex.args.*` and required arguments to form a complete command of ChkTeX.

"latex-workshop.chktex.path": "chktex"

| type     | default value |
| -------- | ------------- |
| _string_ | `"chktex"`    |
