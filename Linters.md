# Linting

## Duplicate labels

Duplicate labels are highlighted when [`latex-workshop.check.duplicatedLabels.enabled`](#latex-workshopcheckduplicatedLabelsenabled) is set to `true`. The computation of the duplicates is based on the data collected for intellisense, so we cannot update the duplicates more often than intellisense. When [`intellisense.update.aggressive.enabled`](Intellisense#latex-workshopintellisenseupdateaggressiveenabled) is set to `false`, duplicates are updated on file save. When [`intellisense.update.aggressive.enabled`](Intellisense#latex-workshopintellisenseupdateaggressiveenabled) is set to `true`, duplicates are updated after stopped typing for longer than [`latex-workshop.intellisense.update.delay`](Intellisense#latex-workshopintellisenseupdatedelay).

#### `latex-workshop.check.duplicatedLabels.enabled`

Enable checking for duplicated labels.

A new check is triggered every time the intellisense data is updated, see [`intellisense.update.aggressive.enabled`](Intellisense#latex-workshopintellisenseupdateaggressiveenabled) .

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

## Linting

LaTeX Workshop currently supports two LaTeX linters, namely, [`ChkTeX`](#chktex) and [`LaCheck`](#lacheck). These two linters can be enabled/disabled separately by [`latex-workshop.linting.chktex.enabled`](#latex-workshoplintingchktexenabled) and [`latex-workshop.linting.lacheck.enabled`](#latex-workshoplintinglacheckenabled), respectively.

The linter behavior is controlled by the following two configuration items.

#### `latex-workshop.linting.run`

When LaTeX should be linted. If set to `onSave`, the whole LaTeX project will be linted upon saving. If set to `onType`, the active document will be linted when input is stopped for a period of time defined in [`latex-workshop.linting.delay`](#latex-workshoplintingdelay), in addition to the behavior of `onSave`.

| type   | default value |
| ------ | ------------- |
| _enum_ | `"onSave"`    |

#### `latex-workshop.linting.delay`

When [`latex-workshop.linting.run`](#latex-workshoplintingrun) is set to `onType`, defines the delay in milliseconds for linter to wait after stopped typing. 

| type     | default value |
| -------- | ------------- |
| _number_ | `500`         |


### ChkTeX

The [ChkTeX](https://www.nongnu.org/chktex/) utility is a LaTeX semantic checker. Once installed, and the relevant setting enabled it is automatically run on any open TeX documents. Its output is parsed by the extension and displayed in the _Problems_ panel.

Auto load of `.chktexrc` configuration files is performed in the following order

1. Manually configured `-l` setting in `chktex.exec.args`
1. The `.chktexrc` file (if exists) in the same folder as the main LaTeX file
1. The `.chktexrc` file (if exists) at the project root folder.

#### `latex-workshop.linting.chktex.enabled`

Enable linting LaTeX with ChkTeX.

The active document will be linted when no document changes for a defined period of time.

The full project will be linted from the root on file save.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### `latex-workshop.linting.chktex.exec.path`

Define the location of ChkTeX executive file.

This command will be joint with [`latex-workshop.linting.chktex.exec.args`](#latex-workshoplintingchktexexecargs) to form a complete ChkTeX command.

| type     | default value |
| -------- | ------------- |
| _string_ | `"chktex"`    |

#### `latex-workshop.linting.chktex.exec.args`

Linter arguments to check LaTeX syntax

Arguments must be in separate strings in the array. Additional arguments, i.e., `-I0 -f%f:%l:%c:%d:%k:%n:%m\n` will be appended when constructing the command. Current file contents will be piped to the command through stdin.

| type                 | default value                             |
| -------------------- | ----------------------------------------- |
| _array_ of _strings_ | `["-wall", "-n22", "-n30", "-e16", "-q"]` |

#### `latex-workshop.linting.chktex.convertOutput.column.enabled`

Enable converting ChkTeX outputs' column numbers for non-ASCII characters.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### `latex-workshop.linting.chktex.convertOutput.column.chktexrcTabSize`

Write the `TabSize` number from `.chktexrc`. The default value `-1` means that LaTeX Workshop will try to find `.chktexrc` and to read the value from it.

| type     | default value |
| -------- | ------------- |
| _number_ | `-1`          |


### LaCheck

The [LaCheck](https://ctan.org/pkg/lacheck) utility is a consistency checker for LaTeX documents. Once installed, and the relevant setting enabled it is automatically run on any open TeX documents. Its output is parsed by the extension and displayed in the _Problems_ panel. Detailed introduction to LaCheck can be found [here](https://linux.die.net/man/1/lacheck).

#### `latex-workshop.linting.lacheck.enabled`

Enable linting LaTeX with LaCheck.

The active document will be linted when no document changes for a defined period of time.

The full project will be linted from the root on file save.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### `latex-workshop.linting.lacheck.exec.path`

Define the location of LaCheck executive file.

"latex-workshop.linting.lacheck.exec.path": "lacheck"

| type     | default value |
| -------- | ------------- |
| _string_ | `"lacheck"`    |
