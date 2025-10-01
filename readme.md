# AI Writing Assistant
A single-page application (SPA) that rephrases user input into different writing styles (Professional, Casual, Polite, and Social-Media). The project demonstrates full-stack development, AI API integration, containerization, and a clean user experience.

## 🚀 Features
- Input any text and rephrase it into multiple styles.
- Styles supported: Professional, Casual, Polite, Social-Media.
- Real-time streaming output as the model generates responses.
- Cancel button to stop an in-progress request.
- Clean, production-like UI using modern frontend practices.
- Fully containerized with Docker Compose for easy setup.

## 📦 Setup & Run Instructions  
### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed.

### Steps
1. Clone the repository
   
         git clone https://github.com/<your-username>/ai-writing-assistant.git
         cd ai-writing-assistant
2. Add your OpenAPI key to the .env file

         OPENAI_API_KEY = '...'
4. Build and start the containers
   
         docker compose up --build
5. Once the containers are running, open your browser and navigate to:
   
        http://127.0.0.1:5001/

## 📝 Assumptions
- The application supports two LLM providers:
  - **Ollama**, running as a local service within Docker Compose  
  - **OpenAI**, using the OpenAI API (requires an API key if enabled)
- The backend communicates with Ollama over Docker’s internal network.
- The frontend interacts with the backend through port **5001**.
- Running with Ollama does **not** require any external API keys.
- The project has been tested on macOS and Linux using Docker Desktop.

## 🔧 Tech Stack
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python (Flask)
- LLM: Ollama, OpenAI
- Containerization: Docker (Leveraging Docker Compose)
