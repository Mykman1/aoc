.PHONY: black env format isort lint

POETRY=poetry
CMD:=$(POETRY) run

env:
	$(POETRY) install --no-root

format: black lint isort

black:
	$(CMD) black .

lint:
	$(CMD) flake8

isort:
	$(CMD) isort .