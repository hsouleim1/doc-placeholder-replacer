# Replace Placeholders in Documents

This script replaces placeholders in `.docx` and `.odt` documents. The placeholders are denoted by text between two `@` characters (e.g., `@placeholder@`). The output document will be saved with `_modified` appended to the original filename.

## Requirements

- `Python 3.x`
- `python-docx`
- `odfpy`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Install the required packages:
    ```sh
    pip install python-docx odfpy
## Usage
To run the script, use the following command:
    
    python replace_placeholders.py <input_string> <input_doc_path>
    <input_string>: The string to replace the placeholders with.
    <input_doc_path>: Path to the input document (either .docx or .odt).
## Example

python replace_placeholders.py "Hello World" "input_document.docx"
The output document will be saved as input_document_modified.docx.
