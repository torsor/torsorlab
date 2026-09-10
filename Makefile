.PHONY: serve build check art clean

serve:   ## preview at http://localhost:4000
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

check: build
	python3 tools/check.py

art:     ## regenerate assets/img/*.svg
	python3 tools/gen-art.py

clean:
	rm -rf _site .jekyll-cache
