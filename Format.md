# Formatting

LaTeX Workshop provides both LaTeX and BibTeX formatting capabilities. The former depends on external tools like [`latexindent`](https://github.com/cmhughes/latexindent.pl) or [`tex-fmt`](https://github.com/WGUNDERWOOD/tex-fmt). The latter is provided by the grammar parsing tool embedded in this extension.

## LaTeX files

LaTeX Workshop can invoke your installed [`latexindent`](https://github.com/cmhughes/latexindent.pl) or [`tex-fmt`](https://github.com/WGUNDERWOOD/tex-fmt) to format the whole LaTeX file or a part of it. Calling which formatter is set by config `latex-workshop.formatting.latex`, which can take three values: `none` for not using any formatter, `latexindent` and `tex-fmt` per se.

Please note that you need to first ensure installing these formatters, otherwise the formatting will fail. This should not cause unexpected data loss, though.

### Relevant settings

### `latex-workshop.format.fixQuotes.enabled`

Enable automatic conversion of \"...\" to ``...'' during formatting.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### `latex-workshop.formatting.latex`

Define the program to format the LaTeX document.

| type     | default value |
| -------- | ------------- |
| _string_ | `"none"`      |

The possible values are: `"none"`, `"latexindent"`, or `"tex-fmt"`.

#### `latex-workshop.formatting.latexindent.path`

Define the path of the `latexindent` executable. If `latexindent` is in the `PATH`, setting this variable to the executable name is fine.

| type     | default value   |
| -------- | --------------- |
| _string_ | `"latexindent"` |

#### `latex-workshop.formatting.latexindent.args`

Define the command line arguments for latexindent. In the addition to the placeholders defined for [recipes](Compile#placeholders), the following placeholders are accepted

-   `%TMPFILE%`: The full path of the raw TeX file to be formatted. At this moment you need to use it as an input file of `latexindent`.
-   `%INDENT%`: The indent character of the file, typically `\t`, `' '`, `' '`.

**Note**: For the moment the `-c` option requires trailing slash."

| type                 | default value                                                     |
| -------------------- | ----------------------------------------------------------------- |
| _Array_ of _strings_ | `[ "-c", "%DIR%/", "%TMPFILE%", "-y=defaultIndent: '%INDENT%'" ]` |

#### `latex-workshop.formatting.tex-fmt.path`

Define the path of the `tex-fmt` executable. If `tex-fmt` is in the `PATH`, setting this variable to the executable name is fine.

| type     | default value |
| -------- | ------------- |
| _string_ | `"tex-fmt"`   |

#### `latex-workshop.formatting.tex-fmt.args`

DDefine the command line arguments for tex-fmt. Refer to https://github.com/WGUNDERWOOD/tex-fmt?tab=readme-ov-file#usage for more information about the arguments. Note that `--stdin` is added by the extension, so no need to add it again. For key-value arguments, separate the key and value in two strings, e.g., `[\"--tabsize\", \"4\"]`.

| Type                 | Default Value   |
| -------------------- | --------------- |
| _Array_ of _strings_ | `[""--nowrap"]` |

## Bibtex files

BibTeX files can be formatted either by using the VSCode _Format Document_ or _Format Selection_ commands or by calling one of the following three commands

-   `latex-workshop.bibsort`: to sort the file,
-   `latex-workshop.bibalign`: to align fields,
-   `latex-workshop.bibalignsort`: to perform both at once.

These commands can be accessed through Visual Studio Code's **Command Palette** (default <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> or <kbd>⌘</kbd>+<kbd>shift</kbd>+<kbd>p</kbd>).

Whether to sort the file when calling VSCode formatting commands is set by [`latex-workshop.bibtex-format.sort.enabled`](#latex-workshopbibtex-formatsortenabled). When formatting bibtex entries, you can decide to keep the trailing comma of the last field in each entry by setting [`latex-workshop.bibtex-format.trailingComma`](#latex-workshopbibtex-formattrailingcomma) to `true`

### Sorting entries

#### `latex-workshop.bibtex-format.sortby`

The commands `latex-workshop.bibsort` and `latex-workshop.bibalignsort` will sort a `.bib` file according to an array of sorting keys specified in `latex-workshop.bibtex-format.sortby`. Valid keys are either a bibtex field name (title, author, year, etc.), or `\"year-desc\"` to sort by year in descending order, or `\"key\"` for the entry key, or `\"type\"` for the entry type (article, book, misc, etc.). E.g. `[\"author\", \"year-desc\", \"title\"]`.". For example, set this to `["author", "year-desc", "title"]` to sort by `author`, then `year` in descending order, then `title`

| Type               | Default Value |
| ------------------ | ------------- |
| _array of strings_ | `[ "key" ]`   |

#### `latex-workshop.bibtex-format.handleDuplicates`

When sorting BibTeX files, how to handle duplicates that appear. Duplicates are decided by `latex-workshop.bibtex-format.sortby`.

| Type             | Default Value            | Possible Values                                                         |
| ---------------- | ------------------------ | ----------------------------------------------------------------------- |
| _enum of string_ | `"Highlight Duplicates"` | `"Ignore Duplicates"`, `"Highlight Duplicates"`, `"Comment Duplicates"` |

#### `latex-workshop.bibtex-format.sort.enabled`

Sort content when calling VSCode formatter on a .bib file.

| Type      | Default Value |
| --------- | ------------- |
| _boolean_ | `false`       |

### `latex-workshop.bibtex-entries.first`

When [`latex-workshop.bibtex-fields.sort.enabled`](#latex-workshopbibtex-formatsortenabled) is true, these fields are put at the top, in the order defined by the array.

| Type               | Default Value           |
| ------------------ | ----------------------- |
| _array of strings_ | `[ "xdata", "string" ]` |

### Aligning fields

The commands `latex-workshop.bibalign` and `latex-workshop.bibalignsort` provide basic alignment of bibliography entries. This action can be configured through the following options.

#### `latex-workshop.bibtex-format.tab`

What kind of indentation to use before each field.

| Type     | Default Value |
| -------- | ------------- |
| _string_ | `"2 spaces"`  |

The possible values are: `"tab"`, `"X spaces"` or simply `"X"` where `X` is a number.

#### `latex-workshop.bibtex-format.align-equal.enabled`

Align equal signs inside each entry.

| Type      | Default Value |
| --------- | ------------- |
| _boolean_ | `true`        |

#### `latex-workshop.bibtex-format.surround`

Whether to surround each field value in quotation marks or curly braces.

| Type             | Default Value    | Possible Values                       |
| ---------------- | ---------------- | ------------------------------------- |
| _enum of string_ | `"Curly braces"` | `"Curly braces"`, `"Quotation marks"` |

#### `latex-workshop.bibtex-format.case`

Whether to use upper- or lowercase field names. (E.g. `AUTHOR = ...` vs `author = ...`).

| Type             | Default Value | Possible Values              |
| ---------------- | ------------- | ---------------------------- |
| _enum of string_ | `"lowercase"` | `"UPPERCASE"`, `"lowercase"` |

#### `latex-workshop.bibtex-format.trailingComma`

Keep the trailing comma of the last field item.

| Type      | Default Value |
| --------- | ------------- |
| _boolean_ | `false`       |

### Sorting fields

#### `latex-workshop.bibtex-fields.sort.enabled`

Sort fields inside every entry. The sorting order is defined by [`latex-workshop.bibtex-fields.order`](#latex-workshopbibtex-fieldsorder). This variable only has effect when formatting bibtex aligns fields. It is not possible to sort entries without aligning them.

| Type      | Default Value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### `latex-workshop.bibtex-fields.order`

When [`latex-workshop.bibtex-fields.sort.enabled`](#latex-workshopbibtex-fieldssortenabled) is true, sort fields according the order defined here and then alphabetically for not listed fields."

| Type               | Default Value |
| ------------------ | ------------- |
| _array of strings_ | `[ ]`         |
