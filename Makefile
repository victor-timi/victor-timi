build:
	python3 scripts/build.py

refresh:
	python3 scripts/build.py --refresh

preview: build
	python3 scripts/preview.py
