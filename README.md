# Langchain (and other libs) Test Project

## Overview

This project is a document processing tool built with Python. It utilizes the `docling` library to convert PDF documents into Markdown format, while also extracting table structures.

## Features

- **PDF to Markdown Conversion:** Converts PDF documents to Markdown for easier readability and editing.
- **Table Structure Extraction:** Identifies and extracts table structures within PDF documents, preserving them in the Markdown output.
- **Memory Usage Tracking:** Includes memory usage monitoring to help optimize performance.

## Requirements

- Python 3.11.11 (with pyenv for version management)
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
   make setup
   make install
   ```

   This command will install all the dependencies listed in `pyproject.toml` and create a `poetry.lock` file to ensure consistent dependency versions.

## Code Structure

- `src/docling/doclin.py`: Contains the main application logic for document processing.
- `src/docling/document_converter.py`: Includes the `DocumentConverter` class responsible for document conversion.
- `src/docling/datamodel/`: Defines data models used within the `docling` library.

## Usage

1. Place your PDF document in the `input/` directory, naming it `file.pdf`.
2. Run the project using `make run`.
3. Find the converted Markdown file in the `output/` directory as `file.md`.

## Customization

- Modify the `source` variable in `src/docling/doclin.py` to process different PDF documents or URLs.
- Adjust `PdfPipelineOptions` in the `DocumentProcessor` class to customize the conversion pipeline, such as enabling OCR or changing accelerator options.
