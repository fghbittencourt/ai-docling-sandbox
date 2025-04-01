docling:
	poetry run python src/docling/doclin.py

pymu:
	poetry run python src/pymu/pymu.py

lc:
	poetry run python src/langchain/lc.py

setup:
	poetry config virtualenvs.in-project true
	pyenv local 3.11.11  

install: setup-poetry
	poetry install