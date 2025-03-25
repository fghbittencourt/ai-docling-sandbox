from docling.document_converter import DocumentConverter


class DocumentProcessor:
    def __init__(self):
        self.converter = DocumentConverter()

    def process_document(self, source_path):
        try:
            result = self.converter.convert(source_path)
            return result.document.export_to_text()
        except Exception as e:
            print(f"Error processing document: {e}")
            return None


def main():
    source = "src/sample.pdf"  # document per local path or URL
    processor = DocumentProcessor()
    document_dict = processor.process_document(source)
    if document_dict:
        print(document_dict)


if __name__ == "__main__":
    main()
