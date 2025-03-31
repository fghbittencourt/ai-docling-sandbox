docling:
	poetry run python src/doclin.py

pymu:
	poetry run python src/pymu.py

lc:
	poetry run python src/lc.py

setup-poetry:
	poetry config virtualenvs.in-project true

install: setup-poetry
	poetry install