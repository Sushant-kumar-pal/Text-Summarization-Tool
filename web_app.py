from flask import Flask, render_template, request, jsonify
from summarizer import TextSummarizer
import logging
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        length = data.get('length', 3)

        if not text:
            return jsonify({'success': False, 'error': 'No text provided'})

        # Initialize summarizer
        summarizer = TextSummarizer()
        
        # Generate summary
        summary = summarizer.summarizer.summarize(text, length)
        
        logging.info(f"Generated summary for text with length: {length}")
        return jsonify({'success': True, 'summary': summary})

    except Exception as e:
        logging.error(f"Error generating summary: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/summarize_url', methods=['POST'])
def summarize_url():
    try:
        data = request.get_json()
        url = data.get('url', '')

        if not url:
            return jsonify({'success': False, 'error': 'No URL provided'})

        # Fetch content from URL
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return jsonify({'success': False, 'error': f'Failed to fetch URL: {response.status_code}'})

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content
        text = ''
        for paragraph in soup.find_all(['p', 'h1', 'h2', 'h3']):
            text += paragraph.get_text() + ' '
        
        # Clean text
        text = re.sub(r'\s+', ' ', text).strip()
        
        if not text:
            return jsonify({'success': False, 'error': 'No text content found in URL'})

        # Generate summary (default to 3 sentences)
        summarizer = TextSummarizer()
        summary = summarizer.summarizer.summarize(text, 3)
        
        return jsonify({
            'success': True,
            'summary': summary
        })

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL content: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500
    except Exception as e:
        logging.error(f"Error processing URL content: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
