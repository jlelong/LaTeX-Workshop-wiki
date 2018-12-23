# Formatting

 Install [latexindent.pl](https://github.com/cmhughes/latexindent.pl) for formatting support if it is not provided by your LaTeX distribution.

 See the [FAQ](#my-file-gets-messed-up) for possible issues with formatting.

## Relevant settings

### latex-workshop.latexindent.path

Define the path of the `latexindent` executable. If `latexindent` is in the `PATH`, setting this variable to the executable name is fine.

|   type   |  default value  |
| -------- | --------------- |
| _string_ | `"latexindent"` |

### latex-workshop.latexindent.args

Define the command line arguments for latexindent. Available placeholders are:

- `%DOC%`: The LaTeX root file path and name without the `.tex` extension.
- `%DOCFILE%`: The LaTeX root file name without the `.tex` extension.
- `%DIR%`: The LaTeX root file path.
- `%TMPFILE%`: would be replaced with the path of file which contains raw TeX source to be formatted. At this moment you need to use it as an input file of `latexindent`.
- `%INDENT%`: The indent character of the file, typically ``\t``, `'  '`, `'    '`.

**Note**: For the moment the `-c` option requires trailing slash."

|        type        |                           default value                           |
| ------------------ | ----------------------------------------------------------------- |
| _Array of strings_ | `[ "-c", "%DIR%/", "%TMPFILE%", "-y=defaultIndent: '%INDENT%'" ]` |
