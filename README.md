## Compiling

Requires [LuaLaTeX](#lualatex), and assumes source files are UTF-8 encoded.

To compile,
<pre><code>lualatex <var>template.tex</var></code></pre>
where <code><var>template.tex</var></code> can be replaced with any input file name.

### Shell escape

Some packages, in particular `minted` or `yushiyang-minted`, require the `-shell-escape` option to compile, as follows:
<pre><code>lualatex -shell-escape <var>template.tex</var></code></pre>

Note that the `-shell-escape` option must be provided **before** the input filename.

### `biblatex`

When using the package `biblatex`, an additional `.bib` file must be used. Remember to edit the `\addbibresource{document.bib}` command to point to the correct `.bib` file name.

To compile, first run
<pre><code>lualatex <var>template.tex</var></code></pre>
to generate some auxiliary files.

Thereafter, if the `.bib` file has been modified, recompile with
<pre><code>biber <var>template</var>
lualatex <var>template.tex</var></code></pre>
where <code><var>template</var></code> is the name of the LaTeX input file. Note that that the biber input **cannot** be specified with a file extension, as biber actually uses several auxiliary files with different file extensions that were generated from the original input file. If this was specified as `template.tex`, biber would look for a file called `template.tex.bcf` instead of `template.bcf` as it should.

If the `.bib` file has not been modified and only the text contents have been modified, recompile with just
<pre><code>lualatex <var>template.tex</var></code></pre>

#### `biblatex`, bibtex and biber

<code><b>biblatex</b></code> is the name of a LaTeX package that enables bibliography handling. <b>bibtex</b> and <b>biber</b> are two different commandline bibfile processors. In order for the package `biblatex` to work, it depends on an external bibfile processor, which can be either bibtex or biber. Here, biber is chosen because it supports Unicode, whereas bibtex does not.

### LuaLaTeX

**LuaTeX** is an output engine for Donald Knuth's original TeX software, that natively supports Unicode (UTF-8) input and natively produces PDF output. It can be seen as a more modern version of pdfTeX (which also produces PDF output, but did not support Unicode), whereas the original TeX software could only produce Postscript output (and did not support Unicode).

LuaTeX should not be confused with LaTeX; LaTeX is an extension of the original TeX that provides many built-in commands/macros that make it much more usable than plain TeX. **LuaLaTeX** is a software package that provides the LaTeX extensions while using LuaTeX to produce its final PDF output.

A similar output engine is XeTeX (and the analogous XeLaTeX), which also supports Unicode input and PDF output. However, LuaLaTeX is used here as its font handling was found to be more robust, though it is still not great.

### Compiling template and test files

<dl>
	<dt><code>template.tex</code></dt>
	<dd><code>lualatex template.tex</code></dd>
	<dt><code>test-hyperref-biblatex.tex</code></dt>
	<dd><code>lualatex test-hyperref-biblatex.tex && biber test-hyperref-biblatex && lualatex test-hyperref-biblatex.tex</code></dd>
</dl>


## Word count

<pre><code>texcount -inc [-incbib] -sum -sub [-html] [-v3] <var>base_tex_file</var></code></pre>
- `-inc` also counts files included using `\input{}`
- `-incbib` to also count bibliography
- `-sub` ≡ `-subcount` enables subcounts for subsections and higher
- `-sum` adds a line showing the sum of different types of word count for each file
- `-html` to output a HTML file
- `-v3` to also print the input file with highlighting to indicate whether each word is counted; use this to check word-count correctness

<strong>DO NOT</strong> use `-merge` as it modifies the input file.

To not show subcounts,
<pre><code>texcount -inc [-incbib] -sum <s>-sub</s> <b>-nosub</b> [-html] [-v3] <var>base_tex_file</var></code></pre>
- `-nosub` disables subcounts

To show only total of all files (including included files),
<pre><code>texcount -inc [-incbib] -sum <s>-sub</s> <b>-total</b> [-html] [-v3] <var>base_tex_file</var></code></pre>
- `-total` removes the per-file counts

### Sum configuration
The sum option can be configured to include or exclude each of the following types of counts: text words, header words, caption words, headers, floats, inlined formulae, displayed formulae.

Use <code>-sum=<var>b</var>[, <var>b</var>[, ...]]</code> for each of the above categories, where <code><var>b</var></code> is `1` or `0`. Any parameter after the first can be omitted to set it to `0`.
