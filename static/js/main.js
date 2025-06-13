async function summarizeText() {
    try {
        const urlInput = document.getElementById('urlInput');
        const inputText = document.getElementById('inputText').value.trim();
        const summaryLength = document.getElementById('summaryLength').value;

        if (urlInput.style.display !== 'none') {
            // If URL input is visible, fetch URL content first
            const url = urlInput.value.trim();
            if (!url) {
                alert('Please enter a URL');
                return;
            }

            const response = await axios.post('/summarize_url', {
                url: url
            });

            if (response.data.success) {
                document.getElementById('inputText').value = response.data.content;
                // Automatically summarize after fetching URL content
                summarizeText();
                return;
            } else {
                alert('Error fetching URL content: ' + response.data.error);
                return;
            }
        }

        if (!inputText) {
            alert('Please enter or upload some text to summarize.');
            return;
        }

        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: inputText,
                length: parseInt(summaryLength)
            })
        });

        const data = await response.json();
        if (data.success) {
            document.getElementById('summaryText').value = data.summary;
            document.getElementById('exportBtn').disabled = false;
        } else {
            alert('Error generating summary: ' + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while generating the summary.');
    }
}

function handleFileUpload() {
    document.getElementById('fileInput').click();
}

function handleFileSelect() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('inputText').value = e.target.result;
        };
        reader.readAsText(file);
    }
}

function handleURLInput() {
    const urlInput = document.getElementById('urlInput');
    const fileInput = document.getElementById('fileInput');
    const fileButton = document.querySelector('button[onclick="handleFileUpload()"]');
    const urlButton = document.querySelector('button[onclick="handleURLInput()"]');
    const urlSummarizeBtn = document.getElementById('urlSummarizeBtn');
    const urlSummaryOptions = document.getElementById('urlSummaryOptions');
    
    if (urlInput.style.display === 'none') {
        urlInput.style.display = 'block';
        fileInput.style.display = 'none';
        fileButton.style.display = 'none';
        urlButton.innerHTML = 'Cancel URL';
        urlSummarizeBtn.style.display = 'inline-block';
        urlSummaryOptions.style.display = 'block';
    } else {
        urlInput.style.display = 'none';
        fileInput.style.display = 'block';
        fileButton.style.display = 'inline-block';
        urlButton.innerHTML = 'Enter URL';
        urlInput.value = '';
        urlSummarizeBtn.style.display = 'none';
        urlSummaryOptions.style.display = 'none';
    }
}

async function summarizeURL() {
    try {
        const url = document.getElementById('urlInput').value.trim();
        if (!url) {
            alert('Please enter a URL');
            return;
        }

        // Fetch URL content and summarize
        const response = await axios.post('/summarize_url', { url: url });

        if (response.data.success) {
            // Display the summary directly
            document.getElementById('summaryText').value = response.data.summary;
            document.getElementById('exportBtn').disabled = false;
        } else {
            alert('Error fetching URL content: ' + response.data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching URL content.');
    }
}

function exportSummary() {
    const summary = document.getElementById('summaryText').value;
    if (!summary) {
        alert('No summary to export.');
        return;
    }

    const blob = new Blob([summary], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'summary.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

function clearText() {
    document.getElementById('inputText').value = '';
    document.getElementById('summaryText').value = '';
    document.getElementById('exportBtn').disabled = true;
}
