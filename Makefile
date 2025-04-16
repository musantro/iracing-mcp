all: lint format

lint: 
	uvx ruff@latest check --fix

format: 
	uvx ruff@latest format

build:
	del dist /q && uv build

publish: build
	uv publish
