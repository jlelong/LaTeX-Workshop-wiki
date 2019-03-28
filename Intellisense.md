# Intellisense

This extension provides a variety of intellisense completions for different LaTeX features; notably for citations, labels, and file names.

## Citations

Every file of a LaTeX project is parsed to look for bibliography resources, either directly in a `thebibliography` environment or given by the `bibliography` or `addbibresource` commands or variants of them. If some of these resources are located outside the project directly, you need to list the directories where to look for them in [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibDirs).

Then, when citation commands like `\cite` and its derivatives are automatically completed with bibliography entries found in the various resources.

If you use very large bibtex files, you may experience temporary freezing. Hence, files larger than 5MB are ignored (see [`latex-workshop.intellisense.citation.maxfilesizeMB"`](#latex-workshopintellisensecitationmaxfilesizeMB)).

| Setting key                                                                                               | Description                                                                    | Default        | Type                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- | ----------------------------------------------- |
| [`latex-workshop.intellisense.citation.label`](#latex-workshopintellisensecitationlabel)                  | Citation property used as suggestion                                           | `"bibtex key"` | _string_: "bibtex key" \| "title" \| "authors"  |
| [`latex-workshop.intellisense.citation.maxfilesizeMB"`](#latex-workshopintellisensecitationmaxfilesizeMB) | Maximum bibtex file size (in MB)                                               | `5`            | _float_                                         |
| [`latex-workshop.intellisense.citation.type`](#latex-workshopintellisensecitationtype)                    | Type of vs code suggestion to use                                              | `"inline"`     | _string_: "inline" \| "browser" (dropdown menu) |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled)                | Enabling of auto-completion for commands and environments from loaded packages | `false`        | _boolean_                                       |
| [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibDirs)                                             | List of paths to look for `.bib` files.                                        | `[]`           | _array_ of _strings_                            |

## References

Similarly as for the citation mechanism, all files of a LaTeX project are search for labels. Then, any `\ref` related command is automatically completed with label keys.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/ref.gif" alt="intellisense demo" height="80px">

## Commands

The key `\` automatically triggers completion of LaTeX commands. Several mechanism play together to build the list of available commands.

- A set of standard LaTeX commands is provided.
- The files of a LaTeX project are searched for any already used commands in the form `mycommand` followed by several `{}` groups. Then, a snippet is dynamically built for each of them and they are added to command completion list.
- When [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`, the command completion list is also populated with the commands provided by all the package used in the project (through `\usepackage`). The list of commands provided by every package is described [here](https://github.com/LaTeXing/LaTeX-cwl).
- If you use personal macro files and want them to be taken into account by intellisense but store them is some `texmf` structure or dedicated directory. Just add the directory containing the file to [`latex-workshop.latex.texDirs`](#latex-workshoplatextexDirs).
- The completion list can use either placeholders or tabstops. The default is to use tabstops, but it can be changed using [`latex-workshop.intellisense.useTabStops.enabled`](#latex-workshopintellisenseuseTabStopsenabled).
  - placeholders: they provide meaningful information on the arguments but prevent any autocompletion trigger.
  - tabstops: they enable us to directly trigger autocompletion again for citations and references.
- We provide one entry in the intellisense completion list per LaTeX command signature. If you feel, it makes the completion list too long, set [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalArgsEntries) to `false`.

| Setting key                                                                                                 | Description                                                                    | Default | Type      |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------- | --------- |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled)                  | Enabling of auto-completion for commands and environments from loaded packages | `false` | _boolean_ |
| [`latex-workshop.intellisense.unimathsymbols.enabled`](#latex-workshopintellisenseunimathsymbolsenabled)    | Show unimath symbols as suggestions when `\` pressed | `false` | _boolean_     |
| [`latex-workshop.intellisense.useTabStops.enabled`](#latex-workshopintellisenseuseTabStopsenabled)          | Use tabstops in intellisense completion                                        | `true`  | _boolean_ |
| [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalArgsEntries) | Add one completion item per command signature                                  | `true`  | _boolean_ |
| [`latex-workshop.latex.texDirs`](#latex-workshoplatextexDirs)                                               | List of paths to look for input `.tex` files.                                   | `[]`    | _array_ of _strings_ |

## Environments

Completion for environments works similarly as for commands. It is based on a set of predefined environments enriched with those defined by the included packages when [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`. Moreover, any custom environment is added to the list after being used once.

## Files

We support intellisense for file completion inside the following commands : `include`, `includegraphics`, `input`, and all the commands from the `import` package. For the `includegraphics` command, we take into account the paths defined by `\graphicspath` if any.

### Related settings

- [`latex-workshop.intellisense.file.exclude`](#latex-workshopintellisensefileexclude)
- [`latex-workshop.intellisense.file.base`](#latex-workshopintellisensefilebase)

## Configuration variables

### latex-workshop.intellisense.citation.label

Defines what to show as suggestion labels when intellisense provides citation suggestions.

- bibtex key: Show bibtex keys in the inline intellisense.
- title: Show publication titles in the inline intellisense.
- authors: Show publication authors in the inline intellisense.

| type     | default value  |
| -------- | -------------- |
| _string_ | `"bibtex key"` |

### latex-workshop.intellisense.citation.maxfilesizeMB

Define the maximum bibtex file size for the extension to parse in MB.

| type    | default value |
| ------- | ------------- |
| _float_ | `5`           |

### latex-workshop.intellisense.citation.type

Define which type of hint to show when intellisense provides citation suggestions.

- inline: Use the inline intellisense to provide citation completion items.
- browser: Use a dropdown menu to provide citation completion items.

| type   | default value |
| ------ | ------------- |
| string | `"inline"`    |

### latex-workshop.intellisense.package.enabled

Auto-complete commands and environments from used packages.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.intellisense.optionalArgsEntries.enabled

Many LaTeX commands can have several signatures, each with different arguments. If set to True, the intellisense completion list will have one entry for each form of a given command.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.intellisense.useTabStops.enabled

Use tabstops instead of placeholders in intellisense. Tabstops enable us to directly trigger autocompletion again (particularly useful for citations and references). On the contrary, placeholders prevent any direct call to autocompletion but they provide more information on the arguments meaning.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

Reload vscode after change.

### latex-workshop.intellisense.unimathsymbols.enabled

When `\` is typed, show unimath symbols in the dropdown selector.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.latex.bibDirs

List of directories where to look for `.bib` files.

Absolute paths are required. This setting is only used by the intellisense feature, you may also need to set the environment variable `BIBINPUTS` properly for the LaTeX compiler to find the `.bib` files.

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.latex.texDirs

List of directories where to look for extra input `.tex/sty` files. The files found in these directories are only take into account by intellisense and not parsed for building the outline.

Absolute paths are required. This setting is only used by the intellisense feature, you may also need to set the environment variable `TEXINPUTS` properly for the LaTeX compiler to find the `.tex/sty` files, see the `env` parameter of [recipes](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-recipes).

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.intellisense.file.exclude

Patterns to ignore in file completion

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[ "**/*.aux", "**/*.bbl", "**/*.bcf", "**/*.blg", "**/*.idx", "**/*.ind", "**/*.lof", "**/*.lot", "**/*.out", "**/*.toc", "**/*.acn", "**/*.acr", "**/*.alg", "**/*.glg", "**/*.glo", "**/*.gls", "**/*.ist", "**/*.fls", "**/*.log", "**/*.fdb_latexmk", "**/*.synctex.gz", "**/*.run.xml" ]`          |

### latex-workshop.intellisense.file.base

Specify the base directory for file completion. The possible choices are

- Completion from the root file directory
- Completion from the current file directory
- both

| type                 | default value |
| -------------------- | ------------- |
| _enum_               | `"root relative"|"file relative"|"both"` |
