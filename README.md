<div align="center">
  <img src="https://github.com/IQLynxAI/TubeTalk/blob/f78d2f6ba71313c52a8f9c5f9a1607f67ef2c625/images/1.png" alt="App Screenshot 1" width="45%" />
  <img src="https://github.com/IQLynxAI/TubeTalk/blob/f78d2f6ba71313c52a8f9c5f9a1607f67ef2c625/images/2.png" alt="App Screenshot 2" width="45%" />
</div>

# **TalkToTube**

🎥 **YouTube Video Q&A with AI** is a Streamlit-based application that allows users to ask questions about YouTube videos. The app uses AI models like Whisper for transcription, Sentence Transformers for embeddings, FAISS for semantic search, and Gemini for generating answers. It’s a powerful tool for extracting insights from video content.

---

## **Features**

- **YouTube Video Processing**:
  - Download audio from YouTube videos.
  - Transcribe audio using OpenAI's Whisper model.
  - Generate a summary of the video using BART.

- **Semantic Search**:
  - Use FAISS and BM25 for hybrid search to retrieve relevant parts of the transcript.
  - Combine search results with Gemini to generate accurate answers.

- **Interactive UI**:
  - Built with Streamlit for a user-friendly interface.
  - Users can input a YouTube URL, process the video, and ask questions.

- **Caching**:
  - Store video embeddings and metadata locally to avoid reprocessing the same video.

---

## **Technologies Used**

- **AI Models**:
  - Whisper (OpenAI) for audio transcription.
  - Sentence Transformers for text embeddings.
  - BART (Facebook) for text summarization.
  - Gemini (Google) for generating answers.

- **Libraries**:
  - Streamlit for the web interface.
  - FAISS for vector similarity search.
  - BM25 for keyword-based search.
  - yt-dlp for downloading YouTube audio.
  - Transformers for summarization and embeddings.

- **Other Tools**:
  - NLTK for text tokenization.
  - Pickle for caching embeddings.
  - Logging for tracking app activity.

---

## **Setup Instructions**

### **1. Prerequisites**

- Python 3.8 or higher.
- A Gemini API key (get it from [Google AI Studio](https://aistudio.google.com/)).

### **2. Clone the Repository**

```bash
git clone https://github.com/IQLynxAI/TubeTalk.git
cd TubeTalk
```

### **3. Install Dependencies**

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

Set google api key in gemini.py file
- genai.configure(api_key="api_key")

```

### **5. Download NLTK Data**

Download the necessary NLTK data for text tokenization:

```bash
python -c "import nltk; nltk.download('punkt')"
```

---

## **Running the Application**

1. Start the Streamlit app:

   ```bash
   streamlit run tubetalk/main.py
   ```

2. Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

3. Enter a YouTube video URL in the input box and click **Process Video**.

4. Once the video is processed, you can ask questions about the video in the chat interface.

---

## **Project Structure**

```
TubeTalk/
│
├── tubetalk/                      # Main application code
│   ├── __init__.py
│   ├── main.py               # Streamlit app entry point
│   ├── models/               # AI models and utilities
│   │   ├── __init__.py
│   │   ├── whisper_model.py  # Whisper transcription logic
│   │   ├── embedding_model.py # SentenceTransformer embeddings
│   │   ├── summarizer.py     # BART summarization logic
│   │   └── gemini.py         # Gemini API interaction
│   ├── utils/                # Utility functions
│   │   ├── __init__.py
│   │   ├── downloader.py     # YouTube audio downloader
│   │   ├── chunking.py       # Semantic chunking logic
│   │   ├── faiss_utils.py    # FAISS vector database utilities
│   │   └── logger.py         # Logging setup
│   ├── data/                 # Data storage (embeddings, logs, etc.)
│       ├── embeddings.pkl    # FAISS embeddings cache
│       └── app.log           # Application logs
│   
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in Git
```

---

## **Usage**

### **1. Process a YouTube Video**

- Enter a YouTube video URL in the input box.
- Click **Process Video**.
- The app will download the audio, transcribe it, and generate a summary.

### **2. Ask Questions**

- After processing the video, you can ask questions about its content.
- The app will retrieve relevant parts of the transcript and generate an answer using Gemini.

---

## **Caching**

- The app caches video embeddings and metadata in the `data/` directory.
- If you process the same video again, the app will load the cached data instead of reprocessing it.

---

## **Logs**

- Application logs are stored in `data/app.log`.
- Logs include details about video processing, user queries, and errors.

---

## **Contributing**

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- OpenAI for the Whisper model.
- Hugging Face for the Transformers library.
- Google for the Gemini API.
- Streamlit for the amazing UI framework.

---

## **Contact**

For questions or feedback, feel free to reach out:

- **Name**: IQLynxAI
- **Email**: contact@iqlynxai.com
- **GitHub**: [IQLynxAI](https://github.com/IQLynxAI)
- **Linkedin**: [IQLynxAI](https://www.linkedin.com/company/iqlynxai/)
- **Instagram**: [IQLynxAI](https://www.instagram.com/iqlynx.ai/)

---