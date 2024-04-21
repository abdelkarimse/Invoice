# Invoice Field Extractor
![Invoice Field Extractor Logo]("818.jpg")
This is a Flask web application that extracts fields from uploaded PDF invoices using spaCy for NLP processing.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd invoice-field-extractor
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the spaCy English language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open a web browser and go to `http://localhost:5000`.

3. Upload a PDF invoice using the provided form.

4. The application will extract fields such as Invoice Number, Description, Quantity, Price, etc., from the uploaded PDF invoice.

## Dependencies

- Flask: Web framework for building the application.
- PyMuPDF: Library for parsing PDF files.
- spaCy: NLP library for text processing.
- Other dependencies specified in `requirements.txt`.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
