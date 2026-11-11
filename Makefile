LOGIN := victor-timi

build:
	python3 scripts/build.py

refresh:
	python3 scripts/build.py --refresh $(LOGIN)

preview: build
	python3 scripts/preview.py

verify: preview
