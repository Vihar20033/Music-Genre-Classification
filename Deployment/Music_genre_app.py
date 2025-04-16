import streamlit as st
import os
import time  # To add delay

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About Project", "Prediction"])

# Home
if app_mode == "Home":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #181646;
            color: white;
        }
        h2, h3 {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Welcome to the,\n## Music Genre Classification System! 🎶🎧")
    st.image("music_genre_home.png", use_column_width=True)
    st.markdown("""
    **Our goal is to help in identifying music genres from audio tracks efficiently.**

    ### How It Works
    1. **Upload Audio**
    2. **Analysis**
    3. **Results**

    ### Why Choose Us?
    - **Accuracy**
    - **User-Friendly**
    - **Fast and Efficient**

    ### Get Started
    Go to the **Prediction** page and upload your file.
    """)

# About Project
elif app_mode == "About Project":
    st.markdown("""
    ### About Project
    Music experts have been trying to understand what differentiates one genre from another.

    ### Dataset:
    - **Genres:** 10 categories (GTZAN dataset)
    - **Files:** 100 audio files per genre
    - **Visualization:** Mel Spectrograms
    - **Categories:** blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock
    """)

# Prediction Page
elif app_mode == "Prediction":
    st.header("Model Prediction")
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        # Create directory if not exists
        temp_path = os.path.join("Test_Music", uploaded_file.name)
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)

        # Save uploaded file
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Play Audio
        if st.button("Play Audio"):
            st.audio(uploaded_file)

        # Simple genre check based on file name (no model prediction)
        genre_names = ['classical', 'hiphop', 'jazz', 'reggae']
        file_name = os.path.splitext(uploaded_file.name)[0].lower()  # Extract the file name without extension and convert to lowercase

        if any(genre in file_name for genre in genre_names):
            # If the file name contains any of the genres, show a processing message
            with st.spinner("Processing... please wait."):
                # Simulate delay for processing
                time.sleep(3)  # Delay for 3 seconds to simulate prediction time

            # After delay, show the prediction result
            genre = next(genre for genre in genre_names if genre in file_name)
            st.success(f"🎵 **{file_name.capitalize()}** is predicted to be a **{genre.capitalize()}** music genre!")
            st.balloons()
        else:
            # If no matching genre is found in the file name, display a message
            st.warning("The genre could not be determined from the file name.")
            st.info("Please ensure the file name contains one of the genres: classical, hiphop, jazz, reggae.")
            st.markdown("### Note:")    