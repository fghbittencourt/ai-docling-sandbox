import time
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
import psutil
import os


def print_memory_usage(label=""):
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # in MB
    print(f"{label} - 📊 Memory usage {mem:.2f} MB")


class DocumentProcessor:
    def __init__(self):
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = False
        pipeline_options.do_table_structure = True
        pipeline_options.table_structure_options.do_cell_matching = True
        # pipeline_options.ocr_options.lang = ["pt"]
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=1, device=AcceleratorDevice.CPU
        )

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            },
        )

        print_memory_usage("✅ Converter initialized!")

    def process_document(self, source_path):
        try:
            convert_start = time.time()
            result = self.converter.convert(source_path)
            convert_time = time.time() - convert_start

            print_memory_usage(f"✅ Conversion complete in {convert_time:.2f} seconds")

            exported = result.document.export_to_markdown()

            return exported
        except Exception as e:
            print(f"Error processing document: {e}")
            return None


def main():
    source = "input/file.pdf"  # document per local path or URL
    processor = DocumentProcessor()
    processed_doc = processor.process_document(source)
    if processed_doc:
        with open("output/file.md", "w", encoding="utf-8") as f:
            f.write(processed_doc)

        print_memory_usage(f"✅ Doc. processed!")


if __name__ == "__main__":
    main()
