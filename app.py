import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from gtts import gTTS
import tempfile

# 1. Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 2. Page Config
st.set_page_config(page_title="Spotify Roast Agent", page_icon="🔥")
st.title("🔥 Spotify Roast Agent")
st.write("I will judge your music taste. Harshly.")

# 3. Setup Spotify Auth
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read",
    cache_path=".spotify_cache"
)

# --- AUTH LOGIC ---
if 'code' in st.query_params:
    code = st.query_params['code']
    try:
        sp_oauth.get_access_token(code)
        st.query_params.clear()
        st.rerun()
    except Exception as e:
        st.error(f"Error saving token: {e}")

if not sp_oauth.validate_token(sp_oauth.cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    st.info("Login to Spotify to get started.")
    st.link_button("Login with Spotify", auth_url)
else:
    # --- APP LOGIC ---
    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        user = sp.current_user()
        st.success(f"Logged in as: **{user['display_name']}**")
        
        # 1. Get Top Artists
        top_artists = sp.current_user_top_artists(limit=10, time_range='long_term')
        if not top_artists['items']:
            top_artists = sp.current_user_top_artists(limit=10, time_range='short_term')

        if top_artists['items']:
            artist_names = [item['name'] for item in top_artists['items']]
            artist_list_str = ", ".join(artist_names)
            
            st.subheader("Your Top Artists:")
            st.write(artist_list_str)
            
            st.divider()
            
            # 2. The Roast Button
            if st.button("🔥 ROAST MY TASTE 🔥", type="primary"):
                with st.spinner("Analyzing your terrible taste..."):
                    
                    # --- AI AGENT SETUP ---
                    my_llm = LLM(
                        model="groq/llama-3.3-70b-versatile",
                        api_key=GROQ_API_KEY
                    )

                    roaster = Agent(
                        role='Mean Music Critic',
                        goal='Roast the user based on their specific music taste',
                        backstory="You are an elitist music snob. You hate everything mainstream. You are rude, funny, and sarcastic.",
                        llm=my_llm,
                        verbose=True
                    )

                    task = Task(
                        description=f"The user listens to these artists: {artist_list_str}. Roast them hard. Keep it under 100 words so it can be spoken easily.",
                        expected_output="A funny, mean, short paragraph roast.",
                        agent=roaster
                    )

                    crew = Crew(agents=[roaster], tasks=[task])
                    result = crew.kickoff()
                    
                    # --- DISPLAY RESULT ---
                    st.success("Analysis Complete!")
                    st.markdown(f"### 💀 The Verdict:")
                    st.write(result.raw)

                    # --- TEXT TO SPEECH ---
                    st.info("🔊 Generating Audio...")
                    try:
                        tts = gTTS(text=result.raw, lang='en')
                        # Create a temp file to store the audio
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                            tts.save(fp.name)
                            st.audio(fp.name, format="audio/mp3")
                    except Exception as e:
                        st.error(f"Audio generation failed: {e}")
                    
        else:
            st.warning("No listening history found!")

    except Exception as e:
        st.error(f"An error occurred: {e}")
        if os.path.exists(".spotify_cache"):
            os.remove(".spotify_cache")
        st.link_button("Retry Login", sp_oauth.get_authorize_url())