# UI files directory
UI_DIR = ./forms
# Resource files directory
RESOURCES_DIR = ./res
# Output directory
COMPILED_DIR = .
# PySide UI compiler
UIC = pyside-uic
# PySide resource compiler
RCC = pyside-rcc

# UI files to compile
UI_FILES = $(foreach file,$(wildcard $(UI_DIR)/*.ui),$(notdir $(file)))
# Compiled UI files
COMPILED_UI_FILES = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)
# Resource files to compile
RESOURCE_FILES = $(foreach file,$(wildcard $(RESOURCES_DIR)/*.qrc),$(notdir $(file)))
# Compiled resource file
COMPILED_RESOURCE_FILES = $(RESOURCE_FILES:%.qrc=$(COMPILED_DIR)/%_rc.py)

# Default target, compile both UI and resource files
all : ui res

# Compile UI files only
ui : $(COMPILED_UI_FILES)

# Compile resource files only
res : $(COMPILED_RESOURCE_FILES)

$(COMPILED_DIR)/ui_%.py : $(UI_DIR)/%.ui
	@echo Compiling UI files...
	$(UIC) $< -o $@

$(COMPILED_DIR)/%_rc.py : $(RESOURCES_DIR)/%.qrc
	@echo Compiling resource files...
	$(RCC) $< -o $@

# Remove the compiled files
clean :
	$(RM) $(COMPILED_UI_FILES) $(COMPILED_RESOURCE_FILES)
