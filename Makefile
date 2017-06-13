doc = tutorial

diagrams = $(wildcard graph/*.svg)

diagramspdf = $(diagrams:.svg=.pdf)

pdf: $(diagramspdf)
	pdflatex $(doc)

bib: $(diagramspdf)
	pdflatex $(doc)
	bibtex $(doc)
	pdflatex $(doc)
	pdflatex $(doc)


%.pdf: %.svg
	inkscape $*.svg --export-pdf=$*.pdf --export-area-drawing --export-latex

clean:
	rm -rf $(doc).pdf *.aux *.log *.pdf *.toc *.out *.bbl *.blg $(diagramspdf) graph/*.pdf_tex
