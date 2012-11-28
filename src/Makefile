BIN_DIR=../bin
DOC_DIR=../doc
WR=../wr

CLASSES=RangeColor CreateHtml DisplayResult Computation

CP="../bin:."

default: binaries

# Make everything
all: docs binaries

# Make all the java bytecode
binaries: $(addprefix $(BIN_DIR)/, $(addsuffix .class, $(CLASSES)))

# Make all the javadoc documentation
docs: $(DOC_DIR)/guide.pdf $(addprefix $(DOC_DIR)/, $(addsuffix .html, $(CLASSES)))

$(BIN_DIR)/%.class: %.java
	javac -cp $(CP) -d $(BIN_DIR) $<

$(DOC_DIR)/%.html: %.java
	javadoc -d $(DOC_DIR) $<

$(DOC_DIR)/guide.pdf: $(WR)/guide.tex
	pdflatex -output-directory $(DOC_DIR) $<


clean:
	rm -rf $(BIN_DIR)/* $(DOC_DIR)/*
