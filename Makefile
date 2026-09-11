.PHONY: serve build check art manuals clean

serve:   ## preview at http://localhost:4000
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

check: build
	python3 bin/check.py

art:     ## regenerate assets/img/*.svg
	python3 bin/gen-art.py

manuals: ## copy the built torsor-writing manuals into the site (BUILD=1 to rebuild them first)
	python3 bin/sync-manuals.py $(if $(BUILD),--build,) $(if $(GUIDES),--from $(GUIDES),)

clean:
	rm -rf _site .jekyll-cache
