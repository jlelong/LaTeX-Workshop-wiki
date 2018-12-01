# Viewing & Synctex

<img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/demo_media/synctex.gif" alt="intellisense demo" height="180px">

## Viewing Documents

A document can previewed a number of ways, namely the icon that appears in the top left of an open TeX document (see gif) <img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/icons/view-pdf-light.svg" height="1em">, or by the shortcut <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>v</kbd> or alternatively <kbd>ctrl</kbd>+<kbd>l</kbd> <kbd>alt</kbd>+<kbd>v</kbd> (see also the [FAQ](https://github.com/James-Yu/LaTeX-Workshop/wiki/FAQ#i-cannot-use-ctrlalt-in-a-shortcut)).

## Synctex

This extension will automatically look for synctex in the expected location (see settings) and will alert the user if it is not found.

### Usage

**Forwards** synctex (pdf to source) is activated by right-clicking on the relevant element of the pdf preview.

**Reverse** synctex (source to pdf) can either be activated by selecting the option from right-clicking

## Relevant Settings

### Overview

| Setting key                                                                                  | Description                               | Default       | Type          |
| -------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------- | ------------- |
| [`latex-workshop​.synctex​.afterBuild​.enabled`](#latex-workshop.synctex.afterBuild.enabled) | Forward synxtex at cursor after compiling | `false`       | _boolean_     |
| [`latex-workshop​.synctex​.path`](#latex-workshop.synctex.path)                              | SyncTeX location                          | `"synctex"`   | _string_      |
| [`latex-workshop​.view.pdf​.external​.synctex`](#latex-workshop.view.pdf.external.synctex)   | SyncTeX command for the extenal viewer    | (see details) | _JSON object_ |  |  |

### Details

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
