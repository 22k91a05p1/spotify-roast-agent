# 🔥 Spotify Roast Agent - AI Music Critic

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CrewAI](https://img.shields.io/badge/AI-CrewAI-orange)
![Llama 3](https://img.shields.io/badge/Model-Llama_3-purple)

**A Generative AI application that uses multi-agent orchestration to analyze your Spotify listening history and ruthlessly roast your music taste.**

This project demonstrates the use of **Agentic AI workflows** to connect real-time user data (Spotify API) with Large Language Models (Groq/Llama-3) to create personalized, context-aware content.

---

## 🚀 Features

* **OAuth 2.0 Authentication:** Securely logs in users via their personal Spotify accounts.
* **Real-Time Data Fetching:** Retrieves long-term top artists and listening habits using the Spotify Web API.
* **AI Agent Workflow:** Uses **CrewAI** to define a "Mean Music Critic" agent with a specific persona and goal.
* **Low-Latency Inference:** Powered by **Groq** (Llama-3-70b) for near-instant roast generation.
* **Text-to-Speech (TTS):** Generates immediate audio feedback using `gTTS` so the agent *speaks* the roast to you.
* **Interactive UI:** Built with **Streamlit** for a responsive and clean web interface.

---

## 🛠️ Tech Stack

* **Language:** Python
* **AI Framework:** [CrewAI](https://crewai.com) (Multi-Agent Orchestration)
* **LLM Engine:** [Groq](https://groq.com) (Llama-3-70b-Versatile)
* **Data Source:** [Spotify Web API](https://developer.spotify.com/documentation/web-api) (`spotipy`)
* **Frontend:** Streamlit
* **Audio:** gTTS (Google Text-to-Speech)

---

## 🏗️ Architecture

1.  **User Login:** The app uses `spotipy` to handle the OAuth handshake.
2.  **Data Ingestion:** Fetches the user's `top_artists` (time_range='long_term').
3.  **Agent Processing:**
    * The **Researcher Agent** (LLM) receives the list of artists.
    * The **Task** instructs the agent to analyze the specific combination of artists and generate a humorous, insulting critique.
4.  **Output Generation:** The text result is displayed on the UI and simultaneously converted to an MP3 audio file.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/22k91a05p1/spotify-roast-agent.git]([https://github.com/22k91a05p1e/spotify-roast-agent.git](https://github.com/22k91a05p1/spotify-roast-agent))
cd spotify-roast-agent


 2. Install Dependencies
Bash

pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory and add your API keys:

Ini, TOML

SPOTIPY_CLIENT_ID="your_spotify_client_id"
SPOTIPY_CLIENT_SECRET="your_spotify_client_secret"
SPOTIPY_REDIRECT_URI="http://localhost:8501"  # Or your deployed URL
GROQ_API_KEY="your_groq_api_key"
Note: To get these keys, you must create an app on the Spotify Developer Dashboard and an API key on Groq Cloud.

4. Run the App Locally
Bash

streamlit run app.py
📸 Screenshots
(<img width="1920" height="1340" alt="spotifyRoast" src="https://github.com/user-attachments/assets/2f386b42-406d-41da-b8b1-5bd86b7709d5" />


"Oh joy, a music connoisseur who thinks Justin Bieber is the epitome of artistic genius..."

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

Built with 💻 and ☕ by Sairam


### **How to use this:**

    * Change `(https://spotify-roast-sairam3639.streamlit.app/)`.
    * Change `(https://github.com/22k91a05p1/spotify-roast-agent).
    * Change `Sairam tupakula` at the bottom to **Sairam Tupakula**.
    **Push it to GitHub:**
    ```bash
    git add README.md
    git commit -m "Add professional README"
    git push
    ```
