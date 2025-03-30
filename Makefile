docling:
	poetry run python src/doclin.py

pymu:
	poetry run python src/pymu.py

setup-poetry:
	poetry config virtualenvs.in-project true

install: setup-poetry
	poetry install