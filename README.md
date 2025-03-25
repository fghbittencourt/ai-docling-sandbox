# Docling Test Project

## Requirements

- Python 3.8 or higher
- Poetry (for dependency management)

## Installation

1. **Install Poetry:**
   If you don't have Poetry installed, follow the instructions on the official Poetry website: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

   For macOS and Linux, you can typically install it with:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   For Windows, follow the instructions on the Poetry website.

2. **Install Project Dependencies:**
   Navigate to the project directory in your terminal and run:

   ```bash
   make install
   ```

   This command will install all the dependencies listed in `pyproject.toml` and create a `poetry.lock` file to ensure consistent dependency versions.

## Running the Project

To run the main script, use the following command in your terminal from the project root directory:

```bash
make run
```

This command uses Poetry to run the Python interpreter within the project's virtual environment, ensuring that all dependencies are correctly loaded.
