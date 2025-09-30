# AI Writing Assistant
A single-page application (SPA) that rephrases user input into different writing styles (Professional, Casual, Polite, and Social-Media). The project demonstrates full-stack development, AI API integration, containerization, and a clean user experience.

## 🚀 Features
- Input any text and rephrase it into multiple styles.
- Styles supported: Professional, Casual, Polite, Social-Media.\
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
3. Build and start the containers
   
        docker compose up --build
5. Once the containers are running, open your browser and navigate to:
   
        http://127.0.0.1:5001/

## 📝 Assumptions
- The app uses Ollama as the LLM backend, running inside Docker.   
- Backend and Ollama communicate over Docker’s internal network.
- The frontend connects to the backend at port 5001.
- No external API keys are required to run this project locally.
- Tested on macOS and Linux with Docker Desktop.

## 🔧 Tech Stack
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python (Flask)
- LLM: Ollama
- Containerization: Docker (Leveraging Docker Compose)
