.PHONY: build-project
.PHONY: build-project-nix
.PHONY: run-project
.PHONY: run-project-nix

build-project:
	pyinstaller --onefile pytmpl.py && chmod +x ./dist/pytmpl && sudo mv ./dist/pytmpl /usr/local/bin 

build-project-nix:
	pyinstaller --onefile pytmpl.py && chmod +x ./dist/pytmpl && sudo mv ./dist/pytmpl ~/.local/bin 

run-project:
	/usr/local/bin/pytmpl 
  
run-project-nix:
	~/.local/bin/pytmpl 
