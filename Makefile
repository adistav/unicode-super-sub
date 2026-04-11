BINARY     = $(HOME)/.local/bin/type-unicode
SWIFT_SRC  = type-unicode.swift
KARABINER_DIR = $(HOME)/.config/karabiner/assets/complex_modifications
KARABINER_JSON = superscript_subscript.json
REPO = $(shell pwd)

.PHONY: all build karabiner install symlinks clean

all: build karabiner

build:
	swiftc -O $(SWIFT_SRC) -o $(BINARY)

karabiner:
	python3 gen_karabiner.py > $(KARABINER_JSON)

# Full install from scratch (run once on a new machine)
install: symlinks build karabiner
	@echo ""
	@echo "Done. Now in Karabiner-Elements:"
	@echo "  Complex Modifications → Add rule → 'Superscript and Subscript' → Enable"

symlinks:
	@mkdir -p $(HOME)/.local/bin $(KARABINER_DIR)
	@ln -sf $(REPO)/$(SWIFT_SRC) $(HOME)/.local/bin/$(SWIFT_SRC)
	@ln -sf $(REPO)/$(KARABINER_JSON) $(KARABINER_DIR)/$(KARABINER_JSON)
	@echo "Symlinks created."

clean:
	rm -f $(BINARY)
