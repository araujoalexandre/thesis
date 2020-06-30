.PHONY: clean

pdf:
	latexmk

clean:
	latexmk -c
