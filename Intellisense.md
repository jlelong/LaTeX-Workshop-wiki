# Intellisense

This extension provides a variety of intellisense completions for different LaTeX features; notably for citations, labels, and file names. Intellisense suggestions are updated on file save but a more aggressive updating strategy can be used by setting [`intellisense.update.aggressive.enabled`](#latex-workshopintellisenseupdateaggressiveenabled) to `true`, which triggers update after no key has been stroked for the delay defined by [`latex-workshop.intellisense.update.delay`](#latex-workshopintellisenseupdatedelay).

## Citations

Every file of a LaTeX project is parsed to look for bibliography resources, either directly in a `thebibliography` environment or given by the `bibliography` or `addbibresource` commands or variants of them. If some of these resources are located outside the project directly, you need to list the directories where to look for them in [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibDirs). You can also rely on the `kpsewhich` command to resolve bibliography files by setting [`latex-workshop.kpsewhich.enabled`](#latex-workshopkpsewhichenabled) to true.

Then, when citation commands like `\cite` and its derivatives are automatically completed with bibliography entries found in the various resources.

If you use very large bibtex files, you may experience temporary freezing. Hence, files larger than 5MB are ignored (see [`latex-workshop.intellisense.citation.maxfilesizeMB`](#latex-workshopintellisensecitationmaxfilesizeMB)).

| Setting key                                                                                               | Description                                                                    | Default        | Type                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- | ----------------------------------------------- |
| [`latex-workshop.intellisense.citation.label`](#latex-workshopintellisensecitationlabel)                  | Citation property used as suggestion                                           | `"bibtex key"` | _string_: "bibtex key" \| "title" \| "authors"  |
| [`latex-workshop.intellisense.citation.format`](#latex-workshopintellisensecitationformat) | List of fields to display | | _array_ of _strings_ |
| [`latex-workshop.intellisense.citation.maxfilesizeMB`](#latex-workshopintellisensecitationmaxfilesizeMB)  | Maximum bibtex file size (in MB)                                               | `5`            | _float_                                         |
| [`latex-workshop.intellisense.citation.type`](#latex-workshopintellisensecitationtype)                    | Type of vs code suggestion to use                                              | `"inline"`     | _string_: "inline" \| "browser" (dropdown menu) |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled)                | Enabling of auto-completion for commands and environments from loaded packages | `false`        | _boolean_                                       |
| [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibDirs)                                             | List of paths to look for `.bib` files.                                        | `[]`           | _array_ of _strings_                            |
| [`latex-workshop.kpsewhich.enabled`](#latex-workshopkpsewhichenabled)                | Use `kpsewhich` to resolve `.bib` files.                                        | `false`           | _boolean_                            |
| [`latex-workshop.kpsewhich.path`](#latex-workshopkpsewhichpath)                                             | location of the kpsewhich executable file.  | `"kpsewhich"`           | _string_ |

## References

Similarly as for the citation mechanism, all files of a LaTeX project are search for labels. We scan labels defined as `\label{...}` or `label={...}`. If you do prefer to ignore `label={...}`, set [`latex-workshop.intellisense.label.keyval`](#latex-workshopintellisenselabelkeyval) to false.

Any `\ref` related command is automatically completed with label keys.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/ref.gif" alt="intellisense demo" height="80px">

## Commands

The key `\` automatically triggers completion of LaTeX commands. Several mechanisms play together to build the list of available commands.

- A set of standard LaTeX commands is provided in the file [`data/commands.json`](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/commands.json). You may overwrite some of these commands by using the [`latex-workshop.intellisense.commandsJSON.replace`](#latex-workshopintellisensecommandsJSONreplace) configuration variable.
- The files of a LaTeX project are searched for any already used commands in the form `mycommand` followed by several `{}` groups. Then, a snippet is dynamically built for each of them and they are added to the command completion list.
- When [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`, the command completion list is also populated with the commands provided by all the _standard_ packages used in the project (through `\usepackage`). The list of commands provided by every package is described [here](https://github.com/LaTeXing/LaTeX-cwl). Note that homemade packages are ignored in this mechanism because they do not come with a `.cwl` file.
- If you use personal macro files and want them to be taken into account by intellisense but store them in some `texmf` structure or dedicated directory. Just add the directory containing the file to [`latex-workshop.latex.texDirs`](Multi-File-Projects#latex-workshoplatextexDirs). The file must be loaded in the LaTeX project through the `\input` macro.
- The completion list can use either placeholders or tabstops. The default is to use tabstops, but it can be changed using [`latex-workshop.intellisense.useTabStops.enabled`](#latex-workshopintellisenseuseTabStopsenabled).
  - placeholders: they provide meaningful information on the arguments but prevent any autocompletion trigger.
  - tabstops: they enable us to directly trigger autocompletion again for citations and references.
- We provide one entry in the intellisense completion list per LaTeX command signature. If you feel, it makes the completion list too long, set [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalArgsEntriesenabled) to `false`.

| Setting key                                                                                                 | Description                                                                    | Default | Type      |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------- | --------- |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled)                  | Enabling of auto-completion for commands and environments from loaded packages | `false` | _boolean_ |
| [`latex-workshop.intellisense.package.env.enabled`](#latex-workshopintellisensepackageenvenabled)      | Enable `\envname` snippets | `true` | _boolean_ |
| [`latex-workshop.intellisense.package.extra`](#latex-workshopintellisensepackageextra)                  | Extra packages to load for intellisense | `[]` | _array_ of _strings_ |
| [`latex-workshop.intellisense.unimathsymbols.enabled`](#latex-workshopintellisenseunimathsymbolsenabled)    | Show unimath symbols as suggestions when `\` pressed | `false` | _boolean_     |
| [`latex-workshop.intellisense.useTabStops.enabled`](#latex-workshopintellisenseuseTabStopsenabled)          | Use tabstops in intellisense completion                                        | `true`  | _boolean_ |
| [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalArgsEntriesenabled) | Add one completion item per command signature                                  | `true`  | _boolean_ |
| [`latex-workshop.latex.texDirs`](Multi-File-Projects#latex-workshoplatextexDirs)                            | List of paths to look for input `.tex` files.                                  | `[]`    | _array_ of _strings_ |

## Environments

There are three different ways to insert a new environment

- **The `\begin / \end` snippet**. Type `\begin` and autocomplete with _Begin a new environment_ and then _Complete with `\end`_. It will leave you with a multi-cursor inside the braces of `\begin{}` and `\end{}` and a list of environments will pop up.

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/begin-end.gif" alt="begin/end with multi-cursor demo"> 

- **The `\begin` only approach**. Type `\begin` and directly choose the environment name from the list. It will automatically add the closing command. Note that this approach enables us to take into account extra arguments. For instance, the `alignat*` environment takes the number of "equation columns" `{n}` as a mandatory argument. Note that dealing with extra arguments is not possible with the `\begin / \end` snippet.

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/begin-options.gif" alt="begin with options demo">

- **The `\envname` approach**. Standard environments can be inserted by typing `\` followed by the environment name. This approach can deal with extra arguments

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/env-cmd.gif" alt="\envname demo">

Completion for environments is based on a set of predefined environments enriched with those defined by the included packages when [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`. Moreover, when [`latex-workshop.intellisense.package.env.enabled`](#latex-workshopintellisensepackageenvenabled) is also `true`, environments provided by used packages can be inserted by using the `\envname` approach. On top of this, any custom environment is added to the completion list after being used once.

## Files

We support intellisense for file completion inside the following commands : `include`, `includegraphics`, `input`, and all the commands from the `import` package. For the `includegraphics` command, when some paths are defined by the `\graphicspath` command, only the files located under these directories are liste.

Note that any file matching one of the patterns listed in the following variables is removed from the list: `files.exclude`, `latex-wokrshop.intellisense.file.exclude`. Moreover, if `search.useIgnoreFiles` is true, any file listed in a `.gitignore` is also removed from the completion list.

To check if a file is indeed listed by a `.gitignore` file, you can run

```
git check-ignore -v full_path_to_the_file
```

### Related settings

- [`latex-workshop.intellisense.file.exclude`](#latex-workshopintellisensefileexclude)
- [`latex-workshop.intellisense.file.base`](#latex-workshopintellisensefilebase)

## Configuration variables

### latex-workshop.intellisense.includegraphics.preview.enabled

Whether or not to preview graphics for `\includegraphics`.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.intellisense.citation.label

Defines what to show as suggestion labels when intellisense provides citation suggestions.

- bibtex key: Show bibtex keys in the inline intellisense.
- title: Show publication titles in the inline intellisense.
- authors: Show publication authors in the inline intellisense.

| type     | default value  |
| -------- | -------------- |
| _string_ | `"bibtex key"` |

### latex-workshop.intellisense.citation.format

List of fields to display for citation preview and intellisense. You must reload VSCode to take into account a change in this configuration.

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `["author", "title", "journal", "publisher", "booktitle", "year"]`          |

### latex-workshop.intellisense.citation.maxfilesizeMB

Define the maximum bibtex file size for the extension to parse in MB.

| type    | default value |
| ------- | ------------- |
| _float_ | `5`           |

### latex-workshop.intellisense.citation.type

Define which type of hint to show when intellisense provides citation suggestions.

- inline: Use the inline intellisense to provide citation completion items.
- browser: Use a dropdown menu to provide citation completion items.

| type     | default value |
| -------- | ------------- |
| _string_ | `"inline"`    |

### latex-workshop.intellisense.package.enabled

Auto-complete commands and environments from used packages.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.intellisense.package.extra

List of extra packages to always add to the auto-completion mechanism.

When `latex-workshop.intellisense.package.enabled` is set to `true`, the commands and environments defined in these extra packages will be added to the intellisense suggestions

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.intellisense.package.env.enabled

If true, every environment provided by an included package is available by a snippet `\envname`. Only applies when `latex-workshop.intellisense.package.enabled` is true.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |


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

### latex-workshop.intellisense.label.keyval

Scan for labels defined as `label={some tex}` to add to the reference intellisense menu. The braces are mandatory.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.intellisense.unimathsymbols.enabled

When `\` is typed, show unimath symbols in the dropdown selector.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.intellisense.commandsJSON.replace

Dictionary of `"snippet name": "snippet action"` to replace the default snippets in `data/commands.json`. Snippet actions should not begin with a `\`. See `data/commands.json` for the list of snippet names. An empty action removes the snippet. E.g. `{ "latexdisplaymath": "[ ${1} \\]", "figure": "" }`. Reload vscode to make any change in this configuration effective

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |

### latex-workshop.latex.bibDirs

List of directories where to look for `.bib` files.

Absolute paths are required. This setting is only used by the intellisense feature, you may also need to set the environment variable `BIBINPUTS` properly for the LaTeX compiler to find the `.bib` files.

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### latex-workshop.kpsewhich.path

Define the location of the kpsewhich executable file.

| type      | default value     |
| --------- | ----------------- |
| _string_  | `"kpsewhich"`     |

### latex-workshop.kpsewhich.enabled

Use `kpsewhich -format=.bib` to resolve bibliography files in addition to looking into the directories listed in [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibDirs).

The `ksepwhich` executable is defined by [`latex-workshop.kpsewhich.path`](#latex-workshopkpsewhichpath).

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |


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
| _enum_               | `"root relative"\|"file relative"\|"both"` |

### latex-workshop.intellisense.update.aggressive.enabled

Defines whether the extension aggressively parses the changed content after stopped typing.

Disable this config will let the extension only update intellisense after saving changed files.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.intellisense.update.delay

Defines the delay in milliseconds for the extension to update current active file content for intellisense after stopped typing.

This config works only when [`intellisense.update.aggressive.enabled`](#latex-workshopintellisenseupdateaggressiveenabled) is enabled. Lower this value will let the extension to know newly defined commands/references/environments more quickly, at the cost of more frequent content parsing: more computation burden.

| type      | default value |
| --------- | ------------- |
| _number_  | `1000`        |

## BibTeX files

Two types of completion are available for BibTeX files

- Hitting `@` triggers completion for adding a new entry. The available completions are described in [data/bibtex-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-entries.json). The user can override any entry by redefining it in the variable [`latex-workshop.intellisense.bibtexJSON.replace`].
The entries are formatted according to the variables already used for bibtex formatting:

  - [`latex-workshop.bibtex-format.tab`](Format#latex-workshopbibtex-formattab)
  - [`latex-workshop.bibtex-format.surround`](Format#latex-workshopbibtex-formatsurround)
  - [`latex-workshop.bibtex-format.case`](Format#latex-workshopbibtex-formatcase)

- Inside an entry, when at the beginning of a line, intellisense suggests optional fields. the completion menu pops up after typing two characters but can also be manually triggered using <kbd>ctrl</kbd> + <kbd>space</kbd>. The available completions are described in [data/bibtex-optional-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-optional-entries.json).

### latex-workshop.intellisense.bibtexJSON.replace

Dictionary of `"entry name": ["array", "of", "fields"]` to replace the default fields used in [data/bibtex-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-entries.json). Reload vscode to make any change in this configuration effective.

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |
