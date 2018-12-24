# Installation and basic settings

## Requirements

- LaTeX distribution in system PATH. For example, [TeX Live](https://www.tug.org/texlive/).
- Please note [MikTeX](https://miktex.org/) does not ship with SyncTeX. Please use [built-in synctex functionality](View#latex-workshopsynctexsynctexjsenabled).
- `latexmk` is required for the default recipe for building LaTeX projects to work. Alternatively, you can [set up your own LaTeX recipe](Compile#latex-recipes).
- _Optional_: Install [ChkTeX](http://www.nongnu.org/chktex) to lint LaTeX projects.
- _Optional_: Install [latexindent.pl](https://github.com/cmhughes/latexindent.pl) for formatting support if it is not provided by your LaTeX distribution.

## Installation

Installing LaTeX Workshop is simple. You can find it in [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), or simply run `ext install latex-workshop` in VS Code Quick Open (`ctrl`/`cmd` + `P`).

## Usage

- Open a `.tex` file, right click to build, SyncTeX, or show all features.
- For a complete list, select `LaTeX Workshop Actions` entry.
- For reverse SyncTeX from PDF to LaTeX, `ctrl`/`cmd` + left mouse click in the PDF.
- Alternatively, VS Code commands are provided in VS Code Command Palette (`ctrl`/`cmd` + `shift` + `P`).
- Type `latex workshop` to show all related commands.
- To view an arbitrary PDF file, just click on the file in the explorer.