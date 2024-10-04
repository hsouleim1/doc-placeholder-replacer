# Document Placeholder Replacement Script
### This script replaces placeholders in DOCX or ODT documents with a specified string. Placeholders are defined as text enclosed between two @ characters (e.g., @placeholder@).

## rerequisites
Make sure you have Python installed on your system. This script requires the following Python libraries:

python-docx: To handle DOCX files
odfpy: To handle ODT files
You can install these libraries using pip:

pip install python-docx odfpy
Script Description
The script replace_placeholders.py replaces placeholders in a document with a given string. It supports both DOCX and ODT file formats.

## Usage
The script is designed to be run from the command line with the following arguments:

input_string: The string to replace the placeholders.
input_doc_path: The path to the input document (either .docx or .odt).
output_doc_path: The path to save the output document (either .docx or .odt).
## Command to Run

python replace_placeholders.py "replacement text" input_document.docx output_document.docx
or

python replace_placeholders.py "replacement text" input_document.odt output_document.odt
## Example

python replace_placeholders.py "Hello World" sample_input.docx sample_output.docx
This command will replace all placeholders in sample_input.docx with "Hello World" and save the result to sample_output.docx.
