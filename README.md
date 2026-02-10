# ☂️ Umbrella Corp: AI Onboarding Assistant

A high-fidelity Retrieval-Augmented Generation (RAG) application designed to onboard new employees into Umbrella Corporation. This project features a **local-first privacy layer** using Ollama for document embeddings and Google's Gemini for advanced reasoning.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

## ✨ Features
- **Privacy-First RAG**: Uses `nomic-embed-text` via Ollama to process sensitive company policies locally.
- **Hybrid Intelligence**: Combines local vector storage (ChromaDB) with Gemini 1.5 Flash for high-speed, accurate responses.
- **Dynamic Employee Context**: Simulates personalized onboarding by injecting unique employee data into the assistant's memory.
- **Robust Architecture**: Built with a clear separation of concerns using custom `Assistant` and `AssistantGUI` classes.
- **Developer Observability**: Integrated with LangSmith for full trace visibility.

## 🛠️ Tech Stack
- **Orchestration**: LangChain
- **LLM**: Google Gemini 1.5 Flash
- **Embeddings**: Ollama (`nomic-embed-text`)
- **Vector Database**: ChromaDB
- **Frontend**: Streamlit

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and running.

### 2. Prepare Local Models
Open your terminal and pull the required embedding model:
```
ollama pull nomic-embed-text
```
### 3. Setup Environment
Clone the repository and install dependencies:
```bash
git clone [https://github.com/yourusername/umbrella-corp-onboarding.git](https://github.com/aryasah/umbrella-corp-onboarding.git)
cd umbrella-corp-onboarding
pip install -r requirements.txt
```

Create a .env file in the root directory:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_PROJECT=umbrella-onboarding
```
### 4. Run the Application
Start the Ollama server if it isn't running (ollama serve), then launch the UI:
```bash
streamlit run main.py
```