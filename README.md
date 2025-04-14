# 🎵 Music Genre Classification using GTZAN Dataset 🎶

This project aims to classify music genres using audio features extracted from the GTZAN dataset. The classification is performed using machine learning techniques such as Convolutional Neural Networks (CNNs) on the Mel Spectrograms of the audio data. 🧑‍💻🎧

## 📋 Table of Contents
1. [Project Description](#project-description)
2. [Dataset](#dataset)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [How to Run](#how-to-run)
7. [Model Training](#model-training)
8. [Acknowledgements](#acknowledgements)

## 📝 Project Description
The goal of this project is to build a machine learning model that can predict the genre of a song based on its audio features. The GTZAN dataset, a collection of 1,000 audio tracks categorized into 10 genres, is used for training and evaluation. 🎼

Steps involved:
1. **Data Preprocessing** 🧹: The audio files are converted into Mel Spectrograms, a time-frequency representation of the audio signal.
2. **Model Architecture** 🏗️: A Convolutional Neural Network (CNN) is trained on the Mel Spectrograms to classify the audio into one of 10 genres.
3. **Evaluation** 📊: The trained model is evaluated on the test set using metrics such as accuracy and loss.

## 📊 Dataset
The GTZAN dataset consists of 1,000 audio tracks (30 seconds each), divided into 10 genres:
1. Blues 🎸
2. Classical 🎻
3. Country 🤠
4. Disco 🪩
5. Hip-hop 🎤
6. Jazz 🎷
7. Metal 🤘
8. Pop 🎤
9. Reggae 🌴
10. Rock 🎸

Each genre contains 100 tracks, with a sample rate of 22,050 Hz and mono audio. 🎧

Dataset link: [GTZAN Dataset](http://marsyas.info/downloads/datasets.html) 🌐

## 🧑‍💻 Requirements
- Python 3.x 🐍
- TensorFlow 2.x 🧠
- Keras 💪
- Librosa (for audio processing) 🎧
- Matplotlib (for visualization) 📈
- Numpy (for numerical operations) 🔢
- Scikit-learn (for model evaluation) 🧪
- Pandas (for data manipulation) 🧑‍💻

To install the dependencies, run:

```bash
pip install -r requirements.txt

---

🛠️ Installation
Clone the repository:

    git clone https://github.com/your-username/music-genre-classification.git
    cd music-genre-classification

---

▶️ How to Run

    To run the project locally, follow these steps:
    Clone the repository and install the dependencies (see above).
    Run the Streamlit app to classify music genres:

    streamlit run Music_genre_app.py

---

🎉 Acknowledgements

    The GTZAN dataset is used for this project. 🎶
    Libraries used include TensorFlow, Librosa, and Matplotlib. 💻
    Special thanks to the community for their contributions to music genre classification! 🙌

---


---

This README.md file is designed to be informative, clear, and fun with the use of emojis. It also includes sections for installation, usage, and model training, making it easy for others to understand and run the project.
