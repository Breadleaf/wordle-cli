PROJECT_NAME=wordle
INSTALL_DIR=/opt/$(PROJECT_NAME)
BIN_LINK=/usr/bin/$(PROJECT_NAME)
ENTRY_SCRIPT=wordle.sh

install:
	@echo "Installing $(PROJECT_NAME) to $(INSTALL_DIR)"
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp -r * $(INSTALL_DIR)
	sudo chmod +x $(INSTALL_DIR)/$(ENTRY_SCRIPT)
	sudo ln -sf $(INSTALL_DIR)/$(ENTRY_SCRIPT) $(BIN_LINK)
	@echo "$(PROJECT_NAME) installed successfully."

uninstall:
	@echo "Uninstalling $(PROJECT_NAME) from $(INSTALL_DIR)"
	sudo rm -rf $(INSTALL_DIR)
	sudo rm -f $(BIN_LINK)
	@echo "$(PROJECT_NAME) uninstalled successfully."

.PHONY: install uninstall
