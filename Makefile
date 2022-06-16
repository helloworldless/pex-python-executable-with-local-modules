build::
	rm app.pex || true
	pex . -r requirements.txt -e supercoolapp.main:main -o app.pex --disable-cache

run::
	./app.pex