# Student Database Application System - Backend

A robust, modular backend application for a Student Database Management System built using FastAPI, featuring full CRUD operations, Google Gemini API integration, a LangGraph workflow, and ChromaDB vector database capabilities[cite: 1].

## 🌐 Live Links
* API Root: https://ai-ml-project-1-gj7r.onrender.com
* Interactive Swagger Documentation: https://ai-ml-project-1-gj7r.onrender.com/docs[cite: 1]

---

## 🚀 Core Project Features
* Modular Architecture: Clean separation of concerns with dedicated files for routing, database models, CRUD operations, and AI chatbot workflows[cite: 1].
* CRUD Operations: Fully functional Create, Read, Update, and Delete endpoints for student database records[cite: 1].
* AI Chatbot Integration: Powered by the Google Gemini API and structured through a LangGraph workflow to safely query student data context[cite: 1].
* Vector Database: Uses ChromaDB for similarity search and retrieval capabilities[cite: 1].
* Interactive Documentation: Fully accessible via FastAPI's automatic Swagger/OpenAPI documentation interface (/docs)[cite: 1].

---

## 🛠️ Recommended Technology Stack
* Backend Framework: Python + FastAPI[cite: 1]
* API Documentation: FastAPI Swagger / OpenAPI Docs[cite: 1]
* AI Model API: Google Gemini API[cite: 1]
* AI Workflow: LangGraph[cite: 1]
* Database: Python data structures / SQL modular schema[cite: 1]
* Vector Database: ChromaDB[cite: 1]
* Version Control: Git + GitHub[cite: 1]
* Deployment: Render (Containerized web service)[cite: 1]

---

## ⚙️ Local Setup & Installation

1. Clone the repository:
   git clone <your-github-repo-url>
   cd student-backend

2. Create and activate a virtual environment:
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure Environment Variables:
   Create a .env file in the root directory and add your Gemini API key:
   GEMINI_API_KEY=your_actual_gemini_api_key_here

5. Run the Application Locally:
   uvicorn main:app --reload
   Open your browser and navigate to http://127.0.0.1:8000/docs to test the APIs[cite: 1].

---

## 🧠 Vector Database Technical Justification
ChromaDB was selected for this project's retrieval and semantic-search architecture. It provides:
* Zero-config local persistence: Perfect for lightweight backend environments and rapid deployment.
* Seamless Python integration: Native compatibility with LangGraph and embedding workflows.
* Low resource overhead: High scalability and development simplicity without complex external server requirements[cite: 1].
