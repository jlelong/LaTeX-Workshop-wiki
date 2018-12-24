# Linting

## ChkTeX

Once ChkTeX is installed, and the relevant setting enabled it is automatically run on any open TeX documents.

## Relevant Settings

### Overview

| Setting key                                                                  | Description                                             | Default                                   | Type                 |
| ---------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------- | -------------------- |
| [`latex-workshop​.chktex​.args​.active`](#latex-workshop.chktex.args.active) | Arguments to be passed to ChkTeX for **current file**   | `["-wall", "-n22", "-n30", "-e16", "-q"]` | _array_ of _strings_ |
| [`latex-workshop​.chktex​.args​.root`](#latex-workshop.chktex.args.root)     | Arguments to be passed to ChkTeX for **entire project** | `["-wall", "-n22", "-n30", "-e16", "-q"]` | _array_ of _strings_ |
| [`latex-workshop​.chktex​.enabled`](#latex-workshop.chktex.enabled)          | Enable LaTeX linting with ChkTeX                        | `false`                                   | _boolean_            |
| [`latex-workshop​.chktex​.interval`](#latex-workshop.chktex.interval)        | Time interval in ms that ChkTeX is run                  | 300                                       | _integer_            |
| [`latex-workshop​.chktex​.path`](#latex-workshop.chktex.path)                | Location of ChkTeX executable                           | `"chktex"`                                | _string_             |

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
