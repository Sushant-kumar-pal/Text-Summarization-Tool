import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import math
import logging

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))

class TextSummarizer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.summarizer = self

    def preprocess_text(self, text):
        """Preprocess the input text by removing special characters and converting to lowercase."""
        text = text.lower()
        return text

    def calculate_sentence_scores(self, text):
        """Calculate scores for each sentence based on word frequency."""
        sentences = sent_tokenize(text)
        word_frequencies = defaultdict(int)
        
        # Calculate word frequencies
        for sentence in sentences:
            words = word_tokenize(sentence)
            for word in words:
                if word not in STOP_WORDS:
                    word_frequencies[word] += 1

        # Calculate maximum frequency
        max_freq = max(word_frequencies.values()) if word_frequencies else 1
        
        # Calculate sentence scores
        sentence_scores = defaultdict(float)
        for i, sentence in enumerate(sentences):
            words = word_tokenize(sentence)
            for word in words:
                if word in word_frequencies:
                    sentence_scores[i] += (word_frequencies[word] / max_freq)
            sentence_scores[i] = math.log1p(sentence_scores[i])  # Apply log transformation

        return sentences, sentence_scores

    def summarize(self, text, summary_length=3):
        """Generate a summary of the given text."""
        try:
            # Preprocess text
            text = self.preprocess_text(text)
            
            # Calculate sentence scores
            sentences, sentence_scores = self.calculate_sentence_scores(text)
            
            # Sort sentences by score
            ranked_sentences = sorted(
                sentence_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            # Select top sentences
            selected_sentences = sorted(
                [ranked_sentences[i][0] for i in range(min(summary_length, len(ranked_sentences)))]
            )
            
            # Generate summary
            summary = " ".join([sentences[i] for i in selected_sentences])
            
            self.logger.info(f"Generated summary with length: {len(selected_sentences)}")
            return summary
            
        except Exception as e:
            self.logger.error(f"Error in summarization: {str(e)}")
            return "Error generating summary: " + str(e)

    def preprocess_text(self, text):
        """Preprocess the input text by removing special characters and converting to lowercase."""
        text = text.lower()
        return text

    def calculate_sentence_scores(self, text):
        """Calculate scores for each sentence based on word frequency."""
        sentences = sent_tokenize(text)
        word_frequencies = defaultdict(int)
        
        # Calculate word frequencies
        for sentence in sentences:
            words = word_tokenize(sentence)
            for word in words:
                if word not in STOP_WORDS:
                    word_frequencies[word] += 1

        # Calculate maximum frequency
        max_freq = max(word_frequencies.values()) if word_frequencies else 1
        
        # Calculate sentence scores
        sentence_scores = defaultdict(float)
        for i, sentence in enumerate(sentences):
            words = word_tokenize(sentence)
            for word in words:
                if word in word_frequencies:
                    sentence_scores[i] += (word_frequencies[word] / max_freq)
            sentence_scores[i] = math.log1p(sentence_scores[i])  # Apply log transformation

        return sentences, sentence_scores

    def summarize(self, text, summary_length=3):
        """Generate a summary of the given text."""
        try:
            # Preprocess text
            text = self.preprocess_text(text)
            
            # Calculate sentence scores
            sentences, sentence_scores = self.calculate_sentence_scores(text)
            
            # Sort sentences by score
            ranked_sentences = sorted(
                sentence_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            # Select top sentences
            selected_sentences = sorted(
                [ranked_sentences[i][0] for i in range(min(summary_length, len(ranked_sentences)))]
            )
            
            # Generate summary
            summary = " ".join([sentences[i] for i in selected_sentences])
            
            self.logger.info(f"Generated summary with length: {len(selected_sentences)}")
            return summary
            
        except Exception as e:
            self.logger.error(f"Error in summarization: {str(e)}")
            return "Error generating summary: " + str(e)
