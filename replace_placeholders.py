import re
import argparse
from docx import Document
from odf.opendocument import load
from odf.text import P
from odf.table import Table, TableRow, TableCell
from odf.element import Text

def replace_placeholder_in_doc(input_string, input_doc_path, output_doc_path):
    # Determine file type by extension
    if input_doc_path.endswith('.docx'):
        replace_in_docx(input_string, input_doc_path, output_doc_path)
    elif input_doc_path.endswith('.odt'):
        replace_in_odt(input_string, input_doc_path, output_doc_path)
    else:
        raise ValueError("Unsupported file type. Please use a .docx or .odt file.")

def replace_in_docx(input_string, input_doc_path, output_doc_path):
    # Load the document
    doc = Document(input_doc_path)

    # Define the regex pattern to find text between two '@' characters
    pattern = re.compile(r'@([^@]*)@')

    # Iterate through each paragraph in the document
    for para in doc.paragraphs:
        if pattern.search(para.text):
            # Replace the matched text with the input string
            para.text = pattern.sub(input_string, para.text)

    # Iterate through each table in the document
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    if pattern.search(para.text):
                        para.text = pattern.sub(input_string, para.text)

    # Save the modified document
    doc.save(output_doc_path)

def replace_in_odt(input_string, input_doc_path, output_doc_path):
    # Load the document
    doc = load(input_doc_path)

    # Define the regex pattern to find text between two '@' characters
    pattern = re.compile(r'@([^@]*)@')

    # Iterate through each paragraph in the document
    for paragraph in doc.getElementsByType(P):
        for text in paragraph.childNodes:
            if text.nodeType == Text.TEXT_NODE and pattern.search(text.data):
                # Replace the matched text with the input string
                text.data = pattern.sub(input_string, text.data)

    # Iterate through each table in the document
    for table in doc.getElementsByType(Table):
        for row in table.getElementsByType(TableRow):
            for cell in row.getElementsByType(TableCell):
                for paragraph in cell.getElementsByType(P):
                    for text in paragraph.childNodes:
                        if text.nodeType == Text.TEXT_NODE and pattern.search(text.data):
                            text.data = pattern.sub(input_string, text.data)

    # Save the modified document
    doc.save(output_doc_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace placeholders in a document.")
    parser.add_argument("input_string", type=str, help="The string to replace the placeholders with.")
    parser.add_argument("input_doc_path", type=str, help="Path to the input document (either .docx or .odt).")
    parser.add_argument("output_doc_path", type=str, help="Path to save the output document (either .docx or .odt).")

    args = parser.parse_args()

    replace_placeholder_in_doc(args.input_string, args.input_doc_path, args.output_doc_path)
