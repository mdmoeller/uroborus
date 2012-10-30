BIN_DIR=../bin
DOC_DIR=../doc

CLASSES=RangeColor CodeChecker CreateHtml

default: binaries

# Make everything
all: docs binaries

# Make all the java bytecode
binaries: $(addprefix $(BIN_DIR)/, $(addsuffix .class, $(CLASSES)))

# Make all the javadoc documentation
docs: $(addprefix $(DOC_DIR)/, $(addsuffix .html, $(CLASSES)))

$(BIN_DIR)/%.class: %.java
	javac -d $(BIN_DIR) $<

$(DOC_DIR)/%.html: %.java
	javadoc -d $(DOC_DIR) $<

clean:
	rm -rf $(BIN_DIR)/* $(DOC_DIR)/*
