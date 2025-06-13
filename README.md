# Text Summarization Tool

A powerful text summarization tool that uses Python's NLTK and spaCy libraries to create concise summaries from large text inputs.

## Features

- Modern web-based interface with Flask
- Paste or upload text for summarization
- Customizable summary length (1-20 sentences)
- Editable summary output
- File export functionality
- Docker support for easy deployment
- Production-ready configuration

## Installation

### Using Docker (Recommended)

1. Install Docker and Docker Compose
2. Clone the repository
3. Build and run the container:
```bash
docker-compose up --build
```

The application will be available at http://localhost:5000

### Local Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. Run the application:
```bash
python web_app.py
```

## Usage

1. Open the application in your web browser
2. Paste or upload text content
3. Adjust the summary length using the slider
4. Click "Summarize" to generate a summary
5. Edit the summary if needed
6. Export the summary to a file

## Project Structure

```
TextSummarizationTool/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── web_app.py
├── summarizer.py
└── README.md
```

## Technologies Used

- Python 3.11+
- Flask
- NLTK
- spaCy
- Docker
- Gunicorn
- HTML/CSS/JavaScript

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
