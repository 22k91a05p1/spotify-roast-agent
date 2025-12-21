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
git clone [https://github.com/22k91a05p1/spotify-roast-agent.git](https://github.com/22k91a05p1/spotify-roast-agent.git)
cd spotify-roast-agent
