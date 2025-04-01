import pathlib
import pymupdf  # This is the correct import from PyMuPDF
import pymupdf4llm


def main():
    filename = "input/file.pdf"
    print("Attempting to open document:", filename)

    doc = pymupdf.open(filename)  # Use fitz.open, not pymupdf.open
    print("Document opened successfully!")

    out = open("output/pymupdf.txt", "wb")  # create a text output

    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
        out.write(text)  # write text of page
        out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)

    out.close()

    md_text = pymupdf4llm.to_markdown("input/file.pdf")
    pathlib.Path("output/pymu_markdown.md").write_bytes(md_text.encode())

    print("Text extraction complete.")


if __name__ == "__main__":
    main()
