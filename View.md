# Viewing & Synctex

<img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/demo_media/synctex.gif" alt="intellisense demo" height="180px">

## Viewing Documents

A document can previewed a number of ways, namely the icon that appears in the top left of an open TeX document (see gif) <img src="https://raw.githubusercontent.com/James-Yu/LaTeX-Workshop/master/icons/view-pdf-light.svg" height="1em">, or by the shortcut <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>v</kbd> (see also the [FAQ](https://github.com/James-Yu/LaTeX-Workshop/wiki/FAQ#i-cannot-use-ctrlalt-in-a-shortcut) for an alternative shortcut).

## Overview

| Setting key                                                                                      | Description                                       | Default       | Type     |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ------------- | -------- |
| [`latex-workshop.latex.outDir`](#latex-workshoplatexoutDir)                                      | Where to find the PDF files                       | `"%DIR%"`     | _string_ |
| [`latex-workshop.view.pdf.viewer`](#latex-workshopviewpdfviewer)                                 | The default PDF viewer                            | (see details) | _string_ |
| [`latex-workshop.view.pdf.external.viewer.command`](#latex-workshopviewpdfexternalviewercommand) | The command to execute when using external viewer | (see details) | _string_ |
| [`latex-workshop.view.pdf.external.viewer.args`](#latex-workshopviewpdfexternalviewerargs)       | The arguments to supply to the above command      | (see details) | _array_  |
| [`latex-workshop.view.pdf.ref.viewer`](#latex-workshopviewpdfrefviewer)                          | The PDF viewer to preview `\ref`                  | (see details) | _string_ |

## Internal PDF viewer

The PDF viewer provided with the extension internally uses [pdf.js](https://github.com/mozilla/pdf.js). The keybindings support by pdf.js are documented [here](https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions#faq-shortcuts).

You can customize the look and feel of the internal PDF viewer. Of course, this is only relevant when using the internal PDF viewer for viewing the PDF produced by the building toolchain, ie when `latex-workshop.view.pdf.viewer` is set to `tab`.

Below are the detailed explanations for the different possible settings

|                                    Setting key                                    |                Description                |
| --------------------------------------------------------------------------------- | ----------------------------------------- |
| [`latex-workshop.view.pdf.tab.useNewGroup`](#latex-workshopviewpdftabuseNewGroup) | Use new editor group for the tab viewer   |
| [`latex-workshop.view.pdf.zoom`](#latex-workshopviewpdfzoom)                      | The default zoom level of the PDF viewer  |
| [`latex-workshop.view.pdf.scrollMode`](#latex-workshopviewpdfscrollMode)          | The default scroll mode of the PDF viewer |
| [`latex-workshop.view.pdf.spreadMode`](#latex-workshopviewpdfspreadMode)          | The default spread mode of the PDF viewer |
| [`latex-workshop.view.pdf.hand`](#latex-workshopviewpdfhand)                      | Enable the hand tool                      |
| [`latex-workshop.view.pdf.invert`](#latex-workshopviewpdfinvert)                  | Define the CSS invert filter level        |
| [`latex-workshop.view.pdf.trim`](#latex-workshopviewpdftrim)                      | The default trim mode of the PDF viewer   |

### latex-workshop.view.pdf.tab.useNewGroup

When set to true, the viewer is opened in a new editor group, otherwise the current group is used.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.view.pdf.zoom

The default zoom level of the PDF viewer. This default value will be passed to the viewer upon opening.

| type     | default value | possible values                                                                                                   |
| -------- | ------------- | ----------------------------------------------------------------------------------------------------------------- |
| _string_ | `"auto"`      | `"auto"`, `"page-actual"`, `"page-fit"`, `"page-width"`, one-based scale values (e.g., 0.5 for 50%, 2.0 for 200%) |

### latex-workshop.view.pdf.scrollMode

The default scroll mode of the PDF viewer. This default value will be passed to the viewer upon opening.

| type   | default value | possible values |
| ------ | ------------- | --------------- |
| _enum_ | `0`           | `0`, `1`, `2`   |

- `0`: Vertical scroll
- `1`: Horizontal scroll
- `2`: Wrapped display

### latex-workshop.view.pdf.spreadMode

The default spread mode of the PDF viewer. This default value will be passed to the viewer upon opening.

| type   | default value | possible values |
| ------ | ------------- |-----------------|
| _enum_ | `0`           | `0`, `1`, `2`   |

- `0`: No spread
- `1`: Odd spread
- `2`: Even spread

### latex-workshop.view.pdf.hand

Define if the hand tool is enabled by default in the PDF viewer.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.view.pdf.invert

Define the CSS invert filter level of the PDF viewer.

This config can invert the color of PDF. Possible values are any floating point numbers from 0 to 1.

| type     | default value |
| -------- | ------------- |
| _number_ | `0`           |

### latex-workshop.view.pdf.trim

The default trim mode of the PDF viewer

| type   | default value | possible values    |
| ------ | ------------- |--------------------|
| _enum_ | `0`           | `0`, `1`, `2`, `3` |

- `0`: No page trimming
- `1`: Trim 5% at margin
- `2`: Trim 10% at margin
- `3`: Trim 15% at margin

## Synctex

This extension will automatically look for `synctex` in the expected location (see [settings](#latex-workshopsynctexpath)) and will alert the user if it is not found. Alternatively, you can use the javascript built-in version of `synctex`, see [settings](#latex-workshopsynctexsynctexjsenabled).

Synctex may fail if the path contains non-ASCII characters, see [FAQ](FAQ#Path-containing-Chinese-characters).

### Usage

**Forward/Direct** synctex (source to pdf) can either be activated by selecting 'Navigate, select, and edit' > 'SyncTeX from cursor' in the side bar, or by the shortcut <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>j</kbd> (<kbd>cmd</kbd>+<kbd>option</kbd>+<kbd>j</kbd> on Mac), see also the [FAQ](https://github.com/James-Yu/LaTeX-Workshop/wiki/FAQ#i-cannot-use-ctrlalt-in-a-shortcut) for an alternative shortcut.

**Backward/Reverse** synctex (pdf to source) is activated by a keybinding configured in `latex-workshop.view.pdf.internal.synctex.keybinding`.
The default option is <kbd>ctrl</kbd> + left-click (<kbd>cmd</kbd> + left-click on Mac) on the relevant element of the pdf preview.
Alternatively, the keybinding can be set to double-click.

### Using synctex with an external viewer

#### Windows

The solution is simple, and works with `sumatraPDF`. Just add the following option to your configuration

```
"latex-workshop.view.pdf.external.synctex.command": "C:/Program Files/SumatraPDF/SumatraPDF.exe",
"latex-workshop.view.pdf.external.synctex.args": [
    "-forward-search",
    "%TEX%",
    "%LINE%",
    "-reuse-instance",
    "-inverse-search",
    "code \"C:\\Users\\<name>\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\out\\cli.js\" -r -g \"%f:%l\"",
    "%PDF%",
],
```

Do not forget to set the paths according to your installation.  You can also replace `code` with the `Code.exe` path.

#### Linux

This is trickier, but works. See [here](https://ubuntuforums.org/showthread.php?t=1716268).

1. Download this file (modified to work with VScode):
    - for Python 2: [evince_synctex2.zip](files/evince_synctex2.zip)
    - for Python 3: [evince_synctex3.zip](files/evince_synctex3.zip)
1. Unzip it in any folder in your PATH (for instance, `$HOME/bin/` or `$HOME/.local/bin`).
1. Add the following options to your configuration:

    ```
    "latex-workshop.view.pdf.external.viewer.command": "evince2".
    "latex-workshop.view.pdf.external.viewer.args": [
        "%PDF%"
    ],
    "latex-workshop.view.pdf.external.synctex.command": "evince_forward_search",
    "latex-workshop.view.pdf.external.synctex.args": [
        "%PDF%",
        "%LINE%",
        "%TEX%"
    ],
    ```

To make this work both ways, first open the pdf file with the external viewer.

##### [Zathura](https://en.wikipedia.org/wiki/Zathura_(document_viewer)) support 

Forward: `--synctex-forward` flag

Backward: Use `%{input}` and `%{line}` as placeholders.

```
"latex-workshop.view.pdf.viewer": "external",
"latex-workshop.pdf.external.viewer.command": "zathura",
"latex-workshop.pdf.external.viewer.args": [
    "--synctex-editor-command",
    "code --reuse-window -g \"%{input}:%{line}\"",
    "%PDF%"
],
"latex-workshop.view.pdf.external.synctex.command": "zathura",
"latex-workshop.view.pdf.external.synctex.args": [
    "--synctex-forward=%LINE%:0:%TEX%",
    "%PDF%"
],
```

### Overview

| Setting key                                                                                        | Description                               | Default       | Type      |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------- | --------- |
| [`latex-workshop.synctex.afterBuild.enabled`](#latex-workshopsynctexafterBuildenabled)             | Forward synctex at cursor after compiling | `false`       | _boolean_ |
| [`latex-workshop.synctex.path`](#latex-workshopsynctexpath)                                        | SyncTeX location                          | `"synctex"`   | _string_  |
| [`latex-workshop.view.pdf.external.synctex.command`](#latex-workshopviewpdfexternalsynctexcommand) | SyncTeX command for the external viewer   | (see details) | _string_  |
| [`latex-workshop.view.pdf.external.synctex.args`](#latex-workshopviewpdfexternalsynctexargs)       | Arguments to use for the above command    | (see details) | _array_   |
| [`latex-workshop.synctex.synctexjs.enabled`](#latex-workshopsynctexsynctexjsenabled)               | Enable using a built-in synctex function. | `true`        | _boolean_ |

## Relevant Settings

### latex-workshop.latex.outDir

The directory where the extension tries to find project files (e.g., PDF and SyncTeX generated files).

Both relative and absolute paths are supported. Relative path start from the root file location, so beware if it is located in sub-directory. Note that the LaTeX toolchain should output files to this path. The default [recipe](Compile#Latex-recipe), which relies on `latexmk`, takes care of putting all the generated files to the directory specified by `latex-workshop.latex.outDir`. The path given to this option must not contain a trailing slash.
The following placeholders `%DOC%`, `%DOCFILE`, `%DIR%` and `%TMPDIR%` can be used.

| type     | default value |
| -------- | ------------- |
| _string_ | `"%DIR%"`     |

### latex-workshop.synctex.afterBuild.enabled

Execute forward synctex at cursor position after compiling LaTeX project.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `false`       |

### latex-workshop.synctex.path

Define the location of SyncTeX executive file.

Additional arguments, e.g., synctex modes and position of click, will be appended to this command.

| type     | default value |
| -------- | ------------- |
| _string_ | `"synctex"`   |

### latex-workshop.view.pdf.external.synctex.command

The command to execute when forward synctex to external viewer.

| type     | default value |
| -------- | ------------- |
| _string_ | ""            |

Note: this function is not officially supported.

### latex-workshop.view.pdf.external.synctex.args

The arguments to apply to the external forward synctex command. %LINE% is the line number, %PDF% is the placeholder for the absolute path to the generated PDF file, and %TEX% is the source LaTeX file path with `.tex` extension from which syncTeX is fired.

| type          | default value                 |
| ------------- | ----------------------------- |
| _array_       | ["%LINE%", "%PDF%", "%TEX%" ] |

### latex-workshop.synctex.synctexjs.enabled

Enable using a builtin synctex function. The command set in latex-workshop.synctex.path will not be used.
This builtin synctex works well even if the path of TeX files contains non-ASCII characters.

| type      | default value |
| --------- | ------------- |
| _boolean_ | `true`        |

### latex-workshop.view.pdf.viewer

The default PDF viewer.

| type     | default value                                |
| -------- | -------------------------------------------- |
| _string_ | `"none" \| "browser" \| "tab" \| "external"` |

- `"none"`: Undetermined viewer. A viewer selector will pop up upon viewing PDF.
- `"browser"`: Open PDF with the default web browser.
- `"tab"`: Open PDF with the built-in tab viewer.
- `"external"`: **Experimental** Open PDF with the external viewer set in "View > Pdf > External: command"

### latex-workshop.view.pdf.ref.viewer

PDF viewer used for [View on PDF] link on `\ref`.

| type     | default value                            |
| -------- | ---------------------------------------- |
| _string_ | `"auto" \| "tabOrBrowser" \| "external"` |

### latex-workshop.view.pdf.external.viewer.command

The command to execute when using external viewer. When left empty, the default PDF viewer provided by the operating system is used.

This function is not officially supported. `%PDF%` is the placeholder for the absolute path to the generated PDF file.

| type          | default value                     |
| ------------- | --------------------------------- |
| _string_      | "\<path to external pdf viewer\>" |

```
    "latex-workshop.view.pdf.external.viewer.command": "/usr/bin/okular",
```

### latex-workshop.view.pdf.external.viewer.args

This works with the `latex-workshop.pdf.external.viewer.args` to provide the arguments to the external viewer.

| type          | default value                       |
| ------------- | ----------------------------------- |
| _array_       | "comma separated list of arguments" |

e.g.

```
   "latex-workshop.view.pdf.external.viewer.args": [
        "--unique",
        "%PDF%"
    ],
```
