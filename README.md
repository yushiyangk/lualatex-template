## Word count

<pre><code>texcount -inc [-incbib] -sum -sub [-html] [-v3] <var>base_tex_file</var>
</code></pre>
- `-inc` also counts files included using `\input{}`
- `-incbib` to also count bibliography
- `-sub` ≡ `-subcount` enables subcounts for subsections and higher
- `-sum` adds a line showing the sum of different types of word count for each file
- `-html` to output a HTML file
- `-v3` to also print the input file with highlighting to indicate whether each word is counted; use this to check word-count correctness

<strong>DO NOT</strong> use `-merge` as it modifies the input file.

To not show subcounts,
<pre><code>texcount -inc [-incbib] -sum <s>-sub</s> <b>-nosub</b> [-html] [-v3] <var>base_tex_file</var>
</code></pre>
- `-nosub` disables subcounts

To show only total of all files (including included files),
<pre><code>texcount -inc [-incbib] -sum <s>-sub</s> <b>-total</b> [-html] [-v3] <var>base_tex_file</var>
</code></pre>
- `-total` removes the per-file counts

### Sum configuration
The sum option can be configured to include or exclude each of the following types of counts: text words, header words, caption words, headers, floats, inlined formulae, displayed formulae.

Use <code>-sum=<var>b</var>[, <var>b</var>[, ...]]</code> for each of the above categories, where <code><var>b</var></code> is `1` or `0`. Any parameter after the first can be omitted to set it to `0`.
