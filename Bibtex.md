# Bibtex actions

There are three commands for formatting `.bib` files: `latex-workshop.bibsort`, `latex-workshop.bibalign`, `latex-workshop.bibalignsort`. These commands respectively *sort*, *align* and *sort and align* a `.bib` file. These commands can be accessed through Visual Studio Code's **Command Pallet** (default <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> or <kbd>⌘</kbd>+<kbd>shift</kbd>+<kbd>p</kbd>).

## Sorting

### `latex-workshop.bibtex-format.sortby`

The commands `latex-workshop.bibsort` and `latex-workshop.bibalignsort` will sort a `.bib` file according to an array of sorting keys specified in `latex-workshop.bibtex-format.sortby`. Valid keys are: any bibtex field (e.g. `author`, `year`, `title`) or `year-desc` for the year in descending order, or `key` for the bibtex key.

For example, set this to `["author", "year-desc", "title"]` to sort by `author`, then `year` in descending order, then `title`

|        Type        | Default Value |
| ------------------ | ------------- |
| _array of strings_ | `[ "key" ]`   |

## Algining

The commands `latex-workshop.bibalign` and `latex-workshop.bibalignsort` provide basic alignment of bibliography entries. This action can be configured through the following options.

### `latex-workshop.bibtex-format.tab`

What kind of indentation to use before each field.

|       Type       | Default Value |          Possible Values            |
| ---------------- | ------------- | ----------------------------------- |
| _enum of string_ | `"2 spaces"`  | `"2 spaces"`, `"4 spaces"`, `"tab"` |

### `latex-workshop.bibtex-format.surround`

Whether to surround each field value in quotation marks or curly braces.

|       Type       |   Default Value  |           Possible Values             |
| ---------------- | ---------------- | ------------------------------------- |
| _enum of string_ | `"Curly braces"` | `"Curly braces"`, `"Quotation marks"` |

### `latex-workshop.bibtex-format.case`

Whether to use upper- or lowercase field names. (E.g. `AUTHOR = ...` vs `author = ...`).

|       Type       | Default Value |       Possible Values        |
| ---------------- | ------------- | ---------------------------- |
| _enum of string_ | `"lowercase"` | `"UPPERCASE"`, `"lowercase"` |