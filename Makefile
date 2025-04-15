all: lint format

lint: 
	uvx ruff@latest check --fix

format: 
	uvx ruff@latest format