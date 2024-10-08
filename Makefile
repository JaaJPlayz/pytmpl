.PHONY: build-project
.PHONY: run-project

build-project:
	pyinstaller --onefile pytmpl.py && chmod +x ./dist/pytmpl && sudo mv ./dist/pytmpl /usr/local/bin 

run-project:
	/usr/local/bin/pytmpl 