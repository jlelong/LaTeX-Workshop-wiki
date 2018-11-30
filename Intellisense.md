# Intellisense

This extension provides a variety of intellisense completions for different LaTeX features; notably for citations, labels, and file names.

## Citation

When citing a bibliography entry, figure, table or other labelled document element via `\ref`, `\autoref`, `\cite` etc. the extension provides suggestions based on a list of possible values gathered in the background. This happens automatically and does not need to be enabled in settings.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/ref.gif" alt="intellisense demo" height="80px">

## Label

## Filenames

## Relevant Settings

### Overview

| Setting key                                                                                                      | Description                                                                                    | Default        | Type                                            |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------- |
| [`latex-workshop​.intellisense​.citation​.label`](#latex-workshop.intellisense.citation.label)                   | Citation property used as suggestion                                                           | `"bibtex key"` | _string_: "bibtex key" \| "title" \| "authors"  |
| [`latex-workshop​.intellisense​.citation​.maxfilesizeMB"`](#latex-workshop.intellisense.citation.maxfilesizeMB)  | Maximum bibtex file size (in MB)                                                               | `5`            | _float_                                         |
| [`latex-workshop​.intellisense​.citation​.type`](#latex-workshop.intellisense.citation.type)                     | Type of vs code suggestion to use                                                              | `"inline"`     | _string_: "inline" \| "browser" (dropdown menu) |
| [`latex-workshop​.intellisense​.package​.enabled`](#latex-workshop.intellisense.package.enabled)                 | Enabling of auto-completion for commands and environments from loaded packages                 | `false`        | _boolean_                                       |
| [`latex-workshop​.intellisense​.surroundCommand​.enabled`](#latex-workshop.intellisense.surroundCommand.enabled) | When text selected, set hotkey `\` surround selection with LaTeX command | `false` | _boolean_ |
| [`latex-workshop​.intellisense​.unimathsymbols​.enabled`](#latex-workshop.intellisense.unimathsymbols.enabled)   | Show unimath symbols as suggestions when `\` pressed | `false` | _boolean_                     |
| [`latex-workshop​.latex​.additionalBib`](#latex-workshop.latex.additionalBib)                                    | Additional bib paths to watch, both relative and absolute paths (with globs) supported         | `[]`           | _array_ of _strings_                            |

### Details

#### latex-workshop.intellisense.citation.label

Defines what to show as suggestion labels when intellisense provides citation suggestions.

- bibtex key: Show bibtex keys in the inline intellisense.
- title: Show publication titles in the inline intellisense.
- authors: Show publication authors in the inline intellisense.

| type     | default value  |
| -------- | -------------- |
| _string_ | `"bibtex key"` |

#### latex-workshop.intellisense.citation.maxfilesizeMB

Defines the maximum bibtex file size for the extension to parse in MB.

| type    | default value |
| ------- | ------------- |
| _float_ | `5`           |

#### latex-workshop.intellisense.citation.type

Defines which type of hint to show when intellisense provides citation suggestions.

- inline: Use the inline intellisense to provide citation completion items.
- browser: Use a dropdown menu to provide citation completion items.

| type   | default value |
| ------ | ------------- |
| string | `"inline"`    |

#### latex-workshop.intellisense.package.enabled

Auto-complete commands and environments from used packages.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.intellisense.surroundCommand.enabled

When `\` is typed with text selected, surround the selection with LaTeX command.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.intellisense.unimathsymbols.enabled

When `\` is typed, show unimath symbols in the dropdown selector.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.latex.additionalBib

Addition bibliography files to watch.

Both relative and absolute paths/globs are supported, but absolute ones are suggested. Relative path start from the root file location, so be ware if it is located in sub-directory.

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |
