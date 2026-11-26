LOGIN := victor-timi

CHROME ?= $(HOME)/Library/Caches/ms-playwright/chromium_headless_shell-1254/chrome-headless-shell-mac-arm64/chrome-headless-shell

build:
	python3 scripts/build.py

refresh:
	python3 scripts/build.py --refresh $(LOGIN)

preview: build
	python3 scripts/preview.py

verify: preview

banner: build
	"$(CHROME)" --headless --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,488 \
		--default-background-color=00000000 --screenshot=$(CURDIR)/.cache/hero.png file://$(CURDIR)/.cache/hero-banner.svg
	cwebp -quiet -q 80 -alpha_q 90 .cache/hero.png -o assets/hero.webp
	python3 scripts/build.py
