run:
	poetry run python src/main.py

setup-poetry:
	poetry config virtualenvs.in-project true

install: setup-poetry
	poetry install