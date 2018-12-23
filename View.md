# Viewing & Synctex

<img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/demo_media/synctex.gif" alt="intellisense demo" height="180px">

## Viewing Documents

A document can previewed a number of ways, namely the icon that appears in the top left of an open TeX document (see gif) <img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/icons/view-pdf-light.svg" height="1em">, or by the shortcut <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>v</kbd> or alternatively <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>alt</kbd>+<kbd>v</kbd> (see also the [FAQ](https://github.com/James-Yu/LaTeX-Workshop/wiki/FAQ#i-cannot-use-ctrlalt-in-a-shortcut)).

## Synctex

This extension will automatically look for synctex in the expected location (see settings) and will alert the user if it is not found.

### Usage

**Forwards** synctex (source to pdf) can either be activated by selecting 'Navigate, select, and edit' > 'SyncTeX from cursor' in the side bar, or by the shortcut <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>j</kbd> (<kbd>cmd</kbd>+<kbd>option</kbd>+<kbd>j</kbd> on Mac).

**Reverse** synctex (pdf to source) is activated by <kbd>ctrl</kbd> + left-clicking (<kbd>cmd</kbd> + left-clicking on Mac) on the relevant element of the pdf preview.

## Relevant Settings

### Overview

| Setting key                                                                                  | Description                               | Default       | Type          |
| -------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------- | ------------- |
| [`latex-workshop​.latex.outputDir`](#latex-workshoplatexoutputDir) | Where to find synctex and PDF files | `"./"`       | _string_     |
| [`latex-workshop​.synctex​.afterBuild​.enabled`](#latex-workshopsynctexafterBuildenabled) | Forward synctex at cursor after compiling | `false`       | _boolean_     |
| [`latex-workshop​.synctex​.path`](#latex-workshopsynctexpath)                              | SyncTeX location                          | `"synctex"`   | _string_      |
| [`latex-workshop​.view.pdf​.external​.synctex`](#latex-workshopviewpdfexternalsynctex)   | SyncTeX command for the external viewer    | (see details) | _JSON object_ |
| [`latex-workshop.synctex.synctexjs.enabled`](#latex-workshopsynctexsynctexjsenabled) | Enable using a built-in synctex function. | `false` | _boolean_ |

### Details

### latex-workshop​.latex.outputDir

The directory where the extension tries to find project files (e.g., PDF and SyncTeX files).

Both relative and absolute paths are supported. Relative path start from the root file location, so beware if it is located in sub-directory. Note that the LaTeX toolchain should output files to this path. The default [recipe](Compile#Latex-recipe), which relies on `latexmk`, takes care of putting all the generated files to the directory specified by `latex-workshop​.latex.outputDir`.
The following placeholders `%DOC%`, `%DOCFILE`, `%DIR%` and `%TMPDIR%` can be used.

| type     | default value |
| -------- | ------------- |
| _string_ | `"./"`        |


#### latex-workshop.synctex.afterBuild.enabled

Execute forward synctex at cursor position after compiling LaTeX project.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

#### latex-workshop.synctex.path

Define the location of SyncTeX executive file.

Additional arguments, e.g., synctex modes and position of click, will be appended to this command.

| type     | default value |
| -------- | ------------- |
| _string_ | `"synctex"`   |

#### latex-workshop.view.pdf.external.synctex

The command to execute when forward synctex to external viewer.

This function is not officially supported. %LINE% is the line number, %PDF% is the placeholder for the absolute path to the generated PDF file, and %TEX% is the source LaTeX file path with `.tex` extension from which syncTeX is fired.

| type          | default value                                                          |
| ------------- | ---------------------------------------------------------------------- |
| _JSON object_ | `{ "command": "SumatraPDF.exe" "args": ["%LINE%", "%PDF%", "%TEX%"] }` |

#### latex-workshop.synctex.synctexjs.enabled

Enable using a builtin synctex function. The command set in latex-workshop.synctex.path will not be used.
This builtin synctex works well even if the path of TeX files contains non-ASCII characters.

### latex-workshop.view.pdf.viewer

The default PDF viewer.

|   type   | default value                                |
| -------- | -------------------------------------------- |
| _string_ | `"none" \| "browser" \| "tab" \| "external"` |

- `"none"`: Undetermined viewer. A viewer selector will pop up upon viewing PDF.
- `"browser"`: Open PDF with the default web browser.
- `"tab"`: Open PDF with the built-in tab viewer.
- `"external"`: **Experimental** Open PDF with the external viewer set in "View > Pdf > External: command"

### latex-workshop.view.pdf.ref.viewer

PDF viewer used for [View on PDF] link on `\ref`.

|   type   | default value                            |
| -------- | ---------------------------------------- |
| _string_ | `"auto" \| "tabOrBrowser" \| "external"` |

### latex-workshop.view.pdf.external.command

The command to execute when using external viewer. When left empty, the default PDF viewer provided by the operating system is used.

This function is not officially supported. `%PDF%` is the placeholder for the absolute path to the generated PDF file.

|     type      |         default value          |
| ------------- | ------------------------------ |
| _JSON object_ | `{ "command": "" "args": [] }` |
