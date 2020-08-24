@default_files = ('main.tex');

$pdflatex = 'pdflatex -synctex=1 %O --shell-escape %S';
$pdf_mode = 1;
$clean_ext = "%R.tdo %R.synctex.gz %R.maf %R.mtc* %R.loa %R.acn %R.acr %R.alg %R.aux %R.auxlock %R.bak %R.bbl %R.blg %R.dvi %R.fls %R.glg %R.glo %R.gls %R.idx %R.ist %R.ilg %R.ind %R.log %R.out %R.pdf %R.ps %R.sav %R.swp %R.toc %R.run.xml %R-blx.bib %R_latexmk %R~ %R.pgf-plot.%R figures/ sources/%R.aux"
