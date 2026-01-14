# .latexmkrc - Configuration for Latexmk to use XeLaTeX with fontspec
$pdflatex = 'xelatex %O %S';
$pdf_mode = 5;  # Use xelatex by default (1=pdflatex, 5=xelatex)

# Common XeLaTeX options matching your original pdflatex command
$latex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Continuous preview mode (optional)
# $preview_mode = 1;
# $preview_continuous_mode = 1;

# Clean up auxiliary files
$clean_ext = "synctex.gz synctex.gz.bak";

# Force complete processing on errors
$force_mode = 1;
