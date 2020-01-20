# Formatting

## LaTeX files

Install [latexindent.pl](https://github.com/cmhughes/latexindent.pl) for formatting support if it is not provided by your LaTeX distribution.

See the [FAQ](FAQ#my-file-gets-messed-up) for possible issues with formatting.

### Relevant settings

#### latex-workshop.latexindent.path

Define the path of the `latexindent` executable. If `latexindent` is in the `PATH`, setting this variable to the executable name is fine.

| type     | default value   |
| -------- | --------------- |
| _string_ | `"latexindent"` |

#### latex-workshop.latexindent.args

Define the command line arguments for latexindent. Available placeholders are:

- `%DOC%`: The LaTeX root file path and name without the `.tex` extension.
- `%DOCFILE%`: The LaTeX root file name without the `.tex` extension.
- `%DIR%`: The LaTeX root file path.
- `%TMPFILE%`: would be replaced with the path of file which contains raw TeX source to be formatted. At this moment you need to use it as an input file of `latexindent`.
- `%INDENT%`: The indent character of the file, typically `\t`, `' '`, `' '`.

**Note**: For the moment the `-c` option requires trailing slash."

| type                 | default value                                                     |
| -------------------- | ----------------------------------------------------------------- |
| _Array_ of _strings_ | `[ "-c", "%DIR%/", "%TMPFILE%", "-y=defaultIndent: '%INDENT%'" ]` |

## Bibtex files

There are three commands for formatting `.bib` files:

- `latex-workshop.bibsort`: to sort the file,
- `latex-workshop.bibalign`: to align fields,
- `latex-workshop.bibalignsort`: to perform both at once.

These commands can be accessed through Visual Studio Code's **Command Pallet** (default <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> or <kbd>⌘</kbd>+<kbd>shift</kbd>+<kbd>p</kbd>).

### Sorting

#### latex-workshop.bibtex-format.sortby

The commands `latex-workshop.bibsort` and `latex-workshop.bibalignsort` will sort a `.bib` file according to an array of sorting keys specified in `latex-workshop.bibtex-format.sortby`. Valid keys are: any bibtex field (e.g. `author`, `year`, `title`) or `year-desc` for the year in descending order, or `key` for the bibtex key.

For example, set this to `["author", "year-desc", "title"]` to sort by `author`, then `year` in descending order, then `title`

|        Type        | Default Value |
| ------------------ | ------------- |
| _array of strings_ | `[ "key" ]`   |

#### latex-workshop.bibtex-format.handleDuplicates

When sorting BibTeX files, how to handle duplicates that appear. Duplicates are decided by `latex-workshop.bibtex-format.sortby`.

|        Type       |      Default Value       | Possible Values                                                         |
| ----------------- | ------------------------ | ----------------------------------------------------------------------- |
| _enum of string_  | `"Highlight Duplicates"` | `"Ignore Duplicates"`, `"Highlight Duplicates"`, `"Comment Duplicates"` |

### Aligning

The commands `latex-workshop.bibalign` and `latex-workshop.bibalignsort` provide basic alignment of bibliography entries. This action can be configured through the following options.

#### latex-workshop.bibtex-format.tab

What kind of indentation to use before each field.

|       Type       | Default Value |          Possible Values            |
| ---------------- | ------------- | ----------------------------------- |
| _enum of string_ | `"2 spaces"`  | `"2 spaces"`, `"4 spaces"`, `"tab"` |

#### latex-workshop.bibtex-format.surround

Whether to surround each field value in quotation marks or curly braces.

|       Type       |   Default Value  |           Possible Values             |
| ---------------- | ---------------- | ------------------------------------- |
| _enum of string_ | `"Curly braces"` | `"Curly braces"`, `"Quotation marks"` |

#### `latex-workshop.bibtex-format.case`

Whether to use upper- or lowercase field names. (E.g. `AUTHOR = ...` vs `author = ...`).

|       Type       | Default Value |       Possible Values        |
| ---------------- | ------------- | ---------------------------- |
| _enum of string_ | `"lowercase"` | `"UPPERCASE"`, `"lowercase"` |