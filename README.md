# Gemini AI Content Filtering Bot

This Python script interacts with the **Google Gemini API** to generate AI-based responses. It includes a **content filtering system** to prevent inappropriate outputs by checking responses against a predefined list of flagged words.

## Features
- Uses **Google Gemini API** for text generation.
- Loads API key securely from a `.env` file.
- Reads a **filter word list** from a file to detect inappropriate content.
- Provides real-time responses to user queries.

## Requirements
- Python 3.8+
- `google-generativeai`
- `python-dotenv`

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file:
     ```plaintext
     GEMINI_API_KEY=your_api_key_here
     PATH=path_to_inappropriate_words_file.txt
     ```
   - Ensure the `PATH` points to a file containing inappropriate words (one per line).

## Usage
Run the script using:
```bash
python script.py
```
Enter a prompt, and the AI will generate a response. If the response contains flagged words, it will be censored.

## File Structure
```
/your-project
│── .env
│── main.py
│── requirements.txt
│── word_list.txt  # (File with inappropriate words)
```

## Troubleshooting
- If you receive **"API key not found"**, check that `.env` contains `GEMINI_API_KEY`.
- If **responses are not being filtered**, ensure `PATH` in `.env` points to a valid file.
- If an **error occurs with the Gemini API**, check your API quota and credentials.

## License
MIT License. Feel free to modify and use.

---

