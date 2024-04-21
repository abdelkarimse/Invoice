import os
import fitz  # PyMuPDF
import spacy
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Configure a folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the fields you want to extract
invoice_fields = {
    "Invoice Number": "",
    "Description": "",
    "Quantity": "",
    "Price": "",
    "Provider Name": "",
    "Fiscal Stamp": "",
    "Fiscal Registration Number": "",
    "Shipping Costs": ""
}


def extract_text_using_fitz(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text


def extract_invoice_field_value(text):
    # Process the text using spaCy
    doc = nlp(text)

    # Initialize a dictionary to store detected entities
    detected_entities = {}

    # Iterate through entities and check if they match any invoice field
    for ent in doc.ents:
        for field_name, field_value in invoice_fields.items():
            if field_name.lower() in ent.text.lower():
                # Update the detected entity for the corresponding field
                detected_entities[field_name] = ent.text

    # Return the detected entities
    return detected_entities


@app.route("/")
def index():
    # Rendering index page
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        # Save the uploaded file to UPLOAD_FOLDER
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text from the PDF file
        extracted_text = extract_text_using_fitz(file_path)

        # Detect invoice field values using NLP
        detected_entities = extract_invoice_field_value(extracted_text)

        # Update invoice fields with detected values
        for field_name, field_value in detected_entities.items():
            invoice_fields[field_name] = field_value

        # Redirect to result page
        return redirect(url_for('result'))
    else:
        return "No file was uploaded"


@app.route("/result")
def result():
    # Rendering result page with invoice fields
    return render_template("result.html", invoice_fields=invoice_fields)


# Run the flask application
if __name__ == '__main__':
    app.run(debug=True)
