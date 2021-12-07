.PHONY: black env format isort lint

POETRY=poetry
CMD:=$(POETRY) run
PRECOMMIT=pre-commit

env:
	$(POETRY) install --no-root
	$(POETRY) run $(PRECOMMIT) install

format: black lint isort

black:
	$(CMD) black .

lint:
	$(CMD) flake8

isort:
	$(CMD) isort .
