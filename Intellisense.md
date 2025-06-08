# Intellisense

This extension provides a variety of intellisense completions for different LaTeX features; notably for citations, commands, environments, labels, and file names. Intellisense suggestions are updated on file save but a more aggressive updating strategy can be used by setting [`intellisense.update.aggressive.enabled`](#latex-workshopintellisenseupdateaggressiveenabled) to `true`, which triggers update after no key has been stroked for the delay defined by [`latex-workshop.intellisense.update.delay`](#latex-workshopintellisenseupdatedelay). Most of the intellisense data are obtained by parsing the project files. Some environments should be considered as verbatim like and therefore be skipped. The list of such environments can be configured by [`latex-workshop.latex.verbatimEnvs`](Compile#latex-workshoplatexverbatimenvs)

## Citations

Every file of a LaTeX project is parsed to look for bibliography resources, either directly in a `thebibliography` environment or given by the `bibliography` or `addbibresource` commands or variants of them. If some of these resources are located outside the project directory, you need to list the directories where to look for them in [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibdirs). You can also rely on the `kpsewhich` command to resolve bibliography files by setting [`latex-workshop.kpsewhich.bibtex.enabled`](#latex-workshopkpsewhichbibtexenabled) to true.

Then, when citation commands like `\cite` and its derivatives are automatically completed with bibliography entries found in the various resources.

When VS Code provides citation suggestions, they are selected (filtered) from all parsed bibliograph entries by comparing the input characters and the `filterText` of each entry, which is defined by [`latex-workshop.intellisense.citation.filterText`](#latex-workshopintellisensecitationfiltertext). Note that due to the internal limit by VS Code, only the first 128 characters of `filterText` is used (reference [here](https://github.com/microsoft/vscode/issues/74133)). Therefore, the order of BibTeX fields matters if `"other fields"` is used in [`latex-workshop.intellisense.citation.filterText`](#latex-workshopintellisensecitationfiltertext).

If you use very large bibtex files, you may experience temporary freezing. Hence, files larger than 5MB are ignored (see [`latex-workshop.bibtex.maxFileSize`](#latex-workshopbibtexmaxfilesize)).

| Setting key | Description | Default | Type |
|-------------|-------------|---------|------|
| [`latex-workshop.intellisense.citation.label`](#latex-workshopintellisensecitationfiltertext) | Citation property used as suggestion label | `"bibtex key"` | _string_: "bibtex key" \| "title" \| "authors" |
| [`latex-workshop.intellisense.citation.filterText`](#latex-workshopintellisensecitationlabel) | Citation property used as filtering text | `["bibtex key", "title", "other fields"]` | Array of _string_s: "bibtex key" \| "title" \| "other fields" |
| [`latex-workshop.intellisense.citation.format`](#latex-workshopintellisensecitationformat) | List of fields to display and to use for filtering suggestions| | _array_ of _strings_ |
| [`latex-workshop.bibtex.maxFileSize`](#latex-workshopbibtexmaxfilesize) | Maximum bibtex file size (in MB) | `5` | _float_ |
| [`latex-workshop.intellisense.citation.type`](#latex-workshopintellisensecitationtype) | Type of vs code suggestion to use | `"inline"` | _string_: "inline" \| "browser" (dropdown menu) |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) | Enabling of auto-completion for commands and environments from loaded packages | `true` | _boolean_ |
| [`latex-workshop.intellisense.package.unusual`](#latex-workshopintellisensepackageunusual) | Auto-complete less used commands and environments from loaded packages | `false` | _boolean_ |
| [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibdirs) | List of paths to look for `.bib` files. | `[]` | _array_ of _strings_ |
| [`latex-workshop.kpsewhich.bibtex.enabled`](#latex-workshopkpsewhichbibtexenabled) | Use `kpsewhich` to resolve `.bib` files. | `true` | _boolean_ |
| [`latex-workshop.kpsewhich.class.enabled`](#latex-workshopkpsewhichclassenabled) | Use `kpsewhich` to resolve `.cls` files. | `true` | _boolean_ |
| [`latex-workshop.kpsewhich.path`](#latex-workshopkpsewhichpath) | location of the kpsewhich executable file. | `"kpsewhich"` | _string_ |


## References

Similarly as for the citation mechanism, all files of a LaTeX project are searched for labels. We scan labels defined by `\label{...}` in the whole document or by `label={...}` but only inside the first argument of an environment.  Label definition with commands other than `\label{...}` can be set in [`latex-workshop.intellisense.label.command`](#latex-workshopintellisenselabelcommand).

Any `\ref` related command is automatically completed with label keys.

<img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/ref.gif" alt="intellisense demo" height="80px">

## Glossaries

Similarly to references, all files of a LaTeX project are searched for glossary and acronym entries typically defined by `\(new|provide|longnew|longprovide)glossaryentry`, `\newacronym`, `\newabbreviation`, `\newabbr`.

We also support getting glossary and acronym definitions from bibtex files as used by `bib2gls`.

We use all these entries to provide completion for most glossary and acronym commandes.

## Commands starting with `\`

The key `\` automatically triggers completion of LaTeX commands. You can define [additional triggers](#latex-workshopintellisensetriggerslatex). Several mechanisms play together to build the list of available commands.

- A set of standard LaTeX commands is provided in the file [`data/commands.json`](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/commands.json). You may overwrite some of these commands or add new ones by using the [`latex-workshop.intellisense.command.user`](#latex-workshopintellisensecommanduser) configuration variable.
- The files of a LaTeX project are searched for any already used commands in the form `mycommand` followed by several `{}` groups. Then, a snippet is dynamically built for each of them and they are added to the command completion list.
- When [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`, the command completion list is also populated with the commands provided by all the _standard_ packages used in the project (through `\usepackage`). The list of commands provided by every package is described [here](https://github.com/texstudio-org/texstudio/tree/master/completion). Note that homemade packages are ignored in this mechanism because they do not come with a `.cwl` file.
- Moreover, when [`latex-workshop.intellisense.package.unusual`](#latex-workshopintellisensepackageunusual) is also `true`, the command completion list is further populated with the less used commands provided by all the _standard_ packages used in the project. The less used commands are marked with `*` classifier in `.cwl` files, see [here](https://texstudio-org.github.io/background.html#classification-format).
- If you use personal macro files and want them to be taken into account by intellisense but store them in some `texmf` structure or dedicated directory. Just add the directory containing the file to [`latex-workshop.latex.texDirs`](Compile#latex-workshoplatextexdirs). The file must be loaded in the LaTeX project through the `\input` macro.
- If you write your own package along with the corresponding `.cwl` file, you can use the Typescript script [parse-cwl.ts](https://github.com/James-Yu/LaTeX-Workshop/blob/master/dev/parse-cwl.ts). For details on how to run this script, please read https://github.com/James-Yu/LaTeX-Workshop/tree/master/dev#parse-cwlts . Place the generated `<mypackage>.json` file in a folder defined in [`latex-workshop.intellisense.package.dirs`](#latex-workshopintellisensepackagedirs). Note it only works when [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is set to `true` and you have imported this package in LaTeX, i.e., `\usepackage{mypackage}`.
- Many snippets use text hints of the form `${\d:some_tex}` for their argument. You may prefer to hide instead by setting[`latex-workshop.intellisense.argumentHint.enabled`](#latex-workshopintellisenseargumenthintenabled) to `false`.
- We provide one entry in the intellisense completion list per LaTeX command signature. If you feel, it makes the completion list too long, set [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalargsentriesenabled) to `false`.

| Setting key | Description | Default | Type |
| ----------- | ----------- | ------- | ---- |
| [`latex-workshop.intellisense.triggers.latex`](#latex-workshopintellisensetriggerslatex) | Additional trigger characters for intellisense of LaTeX documents. | `["{"]` | _array_ of _strings_ |
| [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) | Enabling of auto-completion for commands and environments from loaded packages | `true` | _boolean_ |
| [`latex-workshop.intellisense.package.env.enabled`](#latex-workshopintellisensepackageenvenabled) | Enable `\envname` snippets | `true` | _boolean_ |
| [`latex-workshop.intellisense.package.extra`](#latex-workshopintellisensepackageextra) | Extra packages to load for intellisense | `[]` | _array_ of _strings_ |
| [`latex-workshop.intellisense.package.dirs`](#latex-workshopintellisensepackagedirs) | Extra directories where to look for intellisense data | `[]` | _array_ of _strings_ |
| [`latex-workshop.intellisense.unimathsymbols.enabled`](#latex-workshopintellisenseunimathsymbolsenabled) | Show unimath symbols as suggestions when `\` pressed | `false` | _boolean_ |
| [`latex-workshop.intellisense.subsuperscript.enabled`](#latex-workshopintellisensesubsuperscriptenabled) | Show sub- or super-scripts used in the current project as suggestions when `_{` or `^{` typed | `false` | _boolean_ |
| [`latex-workshop.intellisense.argumentHint.enabled`](#latex-workshopintellisenseargumenthintenabled) | Show argument hints in intellisense completion | `true` | _boolean_ |
| [`latex-workshop.intellisense.optionalArgsEntries.enabled`](#latex-workshopintellisenseoptionalargsentriesenabled) | Add one completion item per command signature | `true` | _boolean_ |
| [`latex-workshop.latex.texDirs`](Compile#latex-workshoplatextexdirs) | List of paths to look for input `.tex` files. | `[]` | _array_ of _strings_ |

## Environments

There are three different ways to insert a new environment

- **The `\begin / \end` snippet**. Type `\begin` and autocomplete with _Insert `\begin / \end`_. It will leave you with a multi-cursor inside the braces of `\begin{}` and `\end{}` and a list of environments will pop up.

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/begin-end.gif" alt="begin/end with multi-cursor demo">

- **The `\begin` only approach**. Type `\begin` and directly choose the environment name from the list. It will automatically add the closing command. Note that this approach enables us to take into account extra arguments. For instance, the `alignat*` environment takes the number of "equation columns" `{n}` as a mandatory argument. Note that dealing with extra arguments is not possible with the `\begin / \end` snippet.

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/begin-options.gif" alt="begin with options demo">

- **The `\envname` approach**. Standard environments can be inserted by typing `\` followed by the environment name. This approach can deal with extra arguments.

  <img src="https://github.com/James-Yu/LaTeX-Workshop/raw/master/demo_media/env-cmd.gif" alt="\envname demo">

Completion for environments is based on a set of predefined environments enriched with those defined by the included packages when [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`. Then, when [`latex-workshop.intellisense.package.unusual`](#latex-workshopintellisensepackageunusual) is also `true`, less used environments are shown in the completion list. Moreover, when [`latex-workshop.intellisense.package.env.enabled`](#latex-workshopintellisensepackageenvenabled) is also `true`, environments provided by used packages can be inserted by using the `\envname` approach. On top of this, any custom environment is added to the completion list after being used once.

## Files

We support intellisense for file completion inside the following commands : `include`, `includegraphics`, `input`, and all the commands from the `import` package. For the `includegraphics` command, when some paths are defined by the `\graphicspath` command, only the files located under these directories are listed.

Note that any file matching one of the patterns listed in the following variables is removed from the list: `files.exclude`, `latex-wokrshop.intellisense.file.exclude`.

When [`latex-workshop.intellisense.includegraphics.preview.enabled`](#latex-workshopintellisenseincludegraphicspreviewenabled) is set to `true`, triggering graphics file completion shows a preview of the file.

### Related settings

- [`latex-workshop.intellisense.file.exclude`](#latex-workshopintellisensefileexclude)
- [`latex-workshop.intellisense.file.base`](#latex-workshopintellisensefilebase)

## `@` suggestions

Next to intellisense for anything starting with `\`, we provide an independent intellisense mechanism triggered by `@`.  The trigger character `@` is set by the configuration variable [`latex-workshop.intellisense.atSuggestion.trigger.latex`](#latex-workshopintellisenseatsuggestiontriggerlatex) and can be replaced by any other non-alphabetical character. Setting [`latex-workshop.intellisense.atSuggestion.trigger.latex`](#latex-workshopintellisenseatsuggestiontriggerlatex) to the empty string deactivates these suggestions. You can remove, modify or define new suggestions using the setting [`latex-workshop.intellisense.atSuggestion.user`](#latex-workshopintellisenseatsuggestionuser).

### Inserting Greek letters

| Prefix | Letter        |
| ------ | ------------- |
| `@a`   | `\alpha`      |
| `@b`   | `\beta`       |
| `@c`   | `\chi`        |
| `@d`   | `\delta`      |
| `@e`   | `\epsilon`    |
| `@f`   | `\phi`        |
| `@g`   | `\gamma`      |
| `@h`   | `\eta`        |
| `@i`   | `\iota`       |
| `@k`   | `\kappa`      |
| `@l`   | `\lambda`     |
| `@m`   | `\mu`         |
| `@n`   | `\nu`         |
| `@p`   | `\pi`         |
| `@q`   | `\theta`      |
| `@r`   | `\rho`        |
| `@s`   | `\sigma`      |
| `@t`   | `\tau`        |
| `@u`   | `\upsilon`    |
| `@o`   | `\omega`      |
| `@&`   | `\wedge`      |
| `@x`   | `\xi`         |
| `@y`   | `\psi`        |
| `@z`   | `\zeta`       |
| `@D`   | `\Delta`      |
| `@F`   | `\Phi`        |
| `@G`   | `\Gamma`      |
| `@Q`   | `\Theta`      |
| `@L`   | `\Lambda`     |
| `@X`   | `\Xi`         |
| `@Y`   | `\Psi`        |
| `@S`   | `\Sigma`      |
| `@U`   | `\Upsilon`    |
| `@W`   | `\Omega`      |
| `@ve`  | `\varepsilon` |
| `@vf`  | `\varphi`     |
| `@vs`  | `\varsigma`   |
| `@vq`  | `\vartheta`   |

## Handy mathematical helpers

| Prefix               | Command                  |
| -------------------- | ------------------------ |
| `@(`                 | `\left( $1 \right)`      |
| `@{`                 | `\left\{ $1 \right\}`    |
| `@[`                 | `\left[ $1 \right]`      |
| `@.`                 | `\cdot`                  |
| `@8`                 | `\infty`                 |
| `@6`                 | `\partial`               |
| `@/`                 | `\frac{$1}{$2}`          |
| `@%`                 | `\frac{$1}{$2}`          |
| `@^`                 | `\Hat{$1}`               |
| `@_`                 | `\bar{$1}`               |
| `@@`                 | `\circ`                  |
| `@0`                 | `^\circ`                 |
| `@;`                 | `\dot{$1}`               |
| `@:`                 | `\ddot{$1}`              |
| `@=`                 | `\equiv`                 |
| `@*`                 | `\times`                 |
| `@<`                 | `\leq`                   |
| `@>`                 | `\geq`                   |
| `@2`                 | `\sqrt{$1}`              |
| `@I`                 | `\int_{$1}^{$2}`         |
| <code>@&#124;</code> | <code>\Big &#124;</code> |
| `@+`                 | `\bigcup`                |
| `@-`                 | `\bigcap`                |
| `@,`                 | `\nonumber`              |

## Configuration variables

### `latex-workshop.intellisense.includegraphics.preview.enabled`

Enable preview for `\includegraphics` completion.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.intellisense.citation.filterText`

Defines what contents are used to filter citation entries when user types characters in [inline](#latex-workshopintellisensecitationtype) mode. Sorting is somewhat controlled by the order of contents defined by this config.

- `bibtex key`: BibTeX keys.
- `title`: Publication titles.
- `author`: Other BibTeX fields except for title, order preserved as defined in BibTeX.

| type               | default value                             |
| ------------------ | ----------------------------------------- |
| Array of _string_s | `["bibtex key", "title", "other fields"]` |

### `latex-workshop.intellisense.citation.label`

Define what field to show as suggestion labels when intellisense provides citation suggestions in [inline](#latex-workshopintellisensecitationtype) mode.

- `bibtex key`: Show bibtex keys in the inline intellisense.
- `title`: Show publication titles in the inline intellisense.
- `author`: Show publication authors in the inline intellisense.

| type     | default value  |
| -------- | -------------- |
| _string_ | `"bibtex key"` |

### `latex-workshop.intellisense.citation.format`

List of fields to display for citation preview and intellisense. This list is also used as the filter text to narrow down the intellisense suggestions.

| type                 | default value                                                      |
|----------------------|--------------------------------------------------------------------|
| _array_ of _strings_ | `["author", "title", "journal", "publisher", "booktitle", "year"]` |

### `latex-workshop.bibtex.maxFileSize`

Define the maximum bibtex file size for the extension to parse in MB.

| type    | default value |
| ------- | ------------- |
| _float_ | `5`           |

### `latex-workshop.intellisense.citation.type`

Define which type of hint to show when intellisense provides citation suggestions.

- inline: Use the inline intellisense to provide citation completion items.
- browser: Use a dropdown menu to provide citation completion items.

| type     | default value |
| -------- | ------------- |
| _string_ | `"inline"`    |

### `latex-workshop.intellisense.triggers.latex`

Additional trigger characters for intellisense of LaTeX documents.

|            type      | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### `latex-workshop.intellisense.package.enabled`

Auto-complete commands and environments from used packages.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.intellisense.package.unusual`

Auto-complete less used commands and environments from used packages. This config is only effective when [`latex-workshop.intellisense.package.enabled`](#latex-workshopintellisensepackageenabled) is `true`.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### `latex-workshop.intellisense.package.exclude`

List of packages to exclude from the auto-completion mechanism.

When `latex-workshop.intellisense.package.enabled` is set to `true`, the commands and environments defined in these packages will not be added to the intellisense suggestions. This setting has a higher priority over `latex-workshop.intellisense.package.extra`. You may include the string "lw-default" in the list to remove all default commands and environments.

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### `latex-workshop.intellisense.package.extra`

List of extra packages to always add to the auto-completion mechanism.

When `latex-workshop.intellisense.package.enabled` is set to `true`, the commands and environments defined in these extra packages will be added to the intellisense suggestions

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### `latex-workshop.intellisense.package.dirs`

List of extra directories to look for package completion files in addition to those provided by the extension.

See the section on [Commands intellisense](#commands-starting-with-) to learn how to generate these files. Files found in these directories have a higher priority over the default ones. This setting is only relevant when [`latex-workshop.intellisense.package.env.enabled`](#latex-workshopintellisensepackageenvenabled) is true.

|         type         | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### `latex-workshop.intellisense.package.env.enabled`

If true, every environment provided by an included package is available by a snippet `\envname`. Only applies when `latex-workshop.intellisense.package.enabled` is true.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |


### `latex-workshop.intellisense.optionalArgsEntries.enabled`

Many LaTeX commands can have several signatures, each with different arguments. If set to True, the intellisense completion list will have one entry for each form of a given command.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.intellisense.argumentHint.enabled`

Many snippets use text hints of the form `${\d:some_tex}` for their argument. You may prefer to hide instead by setting this configuration to `false`.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

Reload vscode after change.

### `latex-workshop.intellisense.label.command`

The name of LaTeX commands that indicates a label definition. The command must accept one mandatory argument of the label reference string, e.g, `\linelabel{ref-str}`.

| type                 | default value            |
| -------------------- | ------------------------ |
| _array_ of _strings_ | `["label", "linelabel"]` |

### `latex-workshop.intellisense.unimathsymbols.enabled`

When `\` is typed, show unimath symbols in the dropdown selector.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### `latex-workshop.intellisense.subsuperscript.enabled`

When `_{` or `^{` are typed, show sub- or super-scripts used in the current project.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### `latex-workshop.intellisense.command.user`

Dictionary of `"command name": "command snippet"` to add to, replace, or remove the default ones in `data/commands.json`. The key of the dictionary is the command name with optional braces indicating the command arguments. The value of the dictionary is the snippet to be inserted. If the key is identical to a default command suggestion defined in `data/commands.json`, the new value in the dictionary is used for suggestion. If the value is an empty string, the command is removed from suggestion. Leading backslashes will be added to both the name and snippet by the extension, so don't include them in this config. For example, `{"mycommand[]{}": "notsamecommand[${2:option}]{$TM_SELECTED_TEXT$1}", "parbox{}{}": "parbox{${2:width}}{$TM_SELECTED_TEXT$1}", "overline{}": ""}` adds a new command with name `mycommand[]{}` that inserts `\\notsamecommand[]{}`, replaces the default snippet of `\\parbox{}{}` to make it include current selected text, and removes `\\overline{}` from suggestion.

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |

### `latex-workshop.intellisense.atSuggestion.trigger.latex`

Character to trigger `@` suggestions as part of intellisense. Set this variable to `''` to deactivate these suggestions.

|type      | default value |
|----------|---------------|
| _string_ | `@`           |

### `latex-workshop.intellisense.atSuggestion.user`

Dictionary of `"@prefix": "snippet command"` to add to, replace, or remove the default suggestions in `data/at-suggestions.json`. The key of the dictionary is the triggering string, which **must** starts with `@` regardless of [`latex-workshop.intellisense.atSuggestion.trigger.latex`](#latex-workshopintellisenseatsuggestiontriggerlatex). The value of the dictionary is the snippet to be inserted. If the key is identical to a default snippet defined in `data/at-suggestions.json`, the new value in the dictionary is used for suggestion. If the value is an empty string, the snippet is removed from suggestion. For example, `{ "@.": "\\cdot", "@6": "" }`.

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |

### `latex-workshop.latex.bibDirs`

List of directories where to look for `.bib` files.

Absolute paths are required. This setting is only used by the intellisense feature, you may also need to set the environment variable `BIBINPUTS` properly for the LaTeX compiler to find the `.bib` files.

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ | `[]`          |

### `latex-workshop.kpsewhich.path`

Define the location of the kpsewhich executable file.

| type      | default value     |
| --------- | ----------------- |
| _string_  | `"kpsewhich"`     |

### `latex-workshop.kpsewhich.bibtex.enabled`

Use `kpsewhich -format=.bib` to resolve bibliography files in addition to looking into the directories listed in [`latex-workshop.latex.bibDirs`](#latex-workshoplatexbibdirs).

The `ksepwhich` executable is defined by [`latex-workshop.kpsewhich.path`](#latex-workshopkpsewhichpath).

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.kpsewhich.class.enabled`

Use `kpsewhich` to resolve class files.

The `ksepwhich` executable is defined by [`latex-workshop.kpsewhich.path`](#latex-workshopkpsewhichpath).

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### `latex-workshop.intellisense.file.exclude`

Patterns to ignore in file completion

| type                 | default value |
| -------------------- | ------------- |
| _array_ of _strings_ |  `["**/*.aux", "**/*.bbl", "**/*.bcf", "**/*.blg", "**/*.idx", "**/*.ind", "**/*.lof", "**/*.lot", "**/*.out", "**/*.toc", "**/*.acn", "**/*.acr", "**/*.alg", "**/*.glg", "**/*.glo", "**/*.gls", "**/*.ist", "**/*.fls", "**/*.log", "**/*.nav", "**/*.snm", "**/*.fdb_latexmk", "**/*.synctex.gz", "**/*.run.xml"]` |

### `latex-workshop.intellisense.file.base`

Specify the base directory for file completion. The possible choices are

- Completion from the root file directory
- Completion from the current file directory
- both

| type   | default value | possible values                                |
| -------| ------------- | -----------------------------------------------|
| _enum_ | `"root relative"` | `"root relative", "file relative", "both"` |

### `latex-workshop.intellisense.update.aggressive.enabled`

Defines whether the extension aggressively parses the changed content after stopped typing.

Disable this config will let the extension only update intellisense after saving changed files.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### `latex-workshop.intellisense.update.delay`

Defines the delay in milliseconds for the extension to update current active file content for intellisense after stopped typing.

This config works only when [`intellisense.update.aggressive.enabled`](#latex-workshopintellisenseupdateaggressiveenabled) is enabled. Lower this value will let the extension to know newly defined commands/references/environments more quickly, at the cost of more frequent content parsing: more computation burden.

| type      | default value |
| --------- | ------------- |
| _number_  | `1000`        |

## BibTeX files

Two types of completion are available for BibTeX files

- Hitting `@` triggers completion for adding a new entry. The available completions are described in [data/bibtex-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-entries.json). The user can override any entry by redefining it in the variable [`latex-workshop.intellisense.bibtexJSON.replace`](#latex-workshopintellisensebibtexjsonreplace).
The entries are formatted according to the variables already used for bibtex formatting:

  - [`latex-workshop.bibtex-format.tab`](Format#latex-workshopbibtex-formattab)
  - [`latex-workshop.bibtex-format.surround`](Format#latex-workshopbibtex-formatsurround)
  - [`latex-workshop.bibtex-format.case`](Format#latex-workshopbibtex-formatcase)

- Inside an entry, when at the beginning of a line, intellisense suggests optional fields. the completion menu pops up after typing two characters but can also be manually triggered using <kbd>ctrl</kbd> + <kbd>space</kbd>. The available completions are described in [data/bibtex-optional-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-optional-entries.json).

### `latex-workshop.intellisense.citation.backend`

Backend to use for citation intellisense.

 type                 | default value | possible values |
| ------------------- | --------------|-----------------|
| _enum_              | `"bibtex"`    | `"bibtex" \| "biblatex"` |

### `latex-workshop.intellisense.biblatexJSON.replace`

Dictionary of `"entry name": ["array", "of", "fields"]` to replace the default fields used in [data/bibtex-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-entries.json).

This variable is used when [latex-workshop.intellisense.citation.backend](`latex-workshopintellisensecitationbackend`) is set to `biblatex`.

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |

### `latex-workshop.intellisense.bibtexJSON.replace`

Dictionary of `"entry name": ["array", "of", "fields"]` to replace the default fields used in [data/bibtex-entries.json](https://github.com/James-Yu/LaTeX-Workshop/blob/master/data/bibtex-entries.json).

This variable is used when [latex-workshop.intellisense.citation.backend](`latex-workshopintellisensecitationbackend`) is set to `bibtex`.

| type                               | default value |
|------------------------------------|---------------|
| _dictionary_ of _string_: _string_ | `{}`          |
