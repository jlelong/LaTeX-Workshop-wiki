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
| [`latex-workshop.chktex.path`](#latex-workshopchktexpath)              | Location of ChkTeX executable                           | `"chktex"`                                | _string_             |
| [`latex-workshop.chktex.run`](#latex-workshopchktexrun)                | When to run ChkTeX (on file save or while typing)       | `"onSave"`                                | _enum_               |

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

#### latex-workshop.chktex.path

Define the location of ChkTeX executive file.

This command will be joint with `latex-workshop.chktex.args.*` and required arguments to form a complete command of ChkTeX.

"latex-workshop.chktex.path": "chktex"

| type     | default value |
| -------- | ------------- |
| _string_ | `"chktex"`    |

### latex-workshop.chktex.run

When LaTeX should be linted by ChkTeX. If set to `onSave`, the whole LaTeX project will be linted upon saving. If set to `onType`, the active document will be linted when input is stopped for a period of time defined in `latex-workshop.chktex.delay`, in addition to the behavior of `onSave`.

| type   | default value |
| ------ | ------------- |
| _enum_ | `"onSave"`    |

### latex-workshop.chktex.delay

When `latex-workshop.chktex.run` is set to `onType`, defines the delay in milliseconds for chktex to wait after stopped typing. 

| type     | default value |
| -------- | ------------- |
| _number_ | 500           |
