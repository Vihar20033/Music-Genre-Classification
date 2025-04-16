import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm

# Constants
DATA_PATH = "genres"
SAMPLES_PER_TRACK = 660000  # 30 seconds * 22050 Hz

# Function to extract Mel spectrogram
def extract_features(file_path, max_len=660000):
    try:
        audio, sr = librosa.load(file_path, duration=30)
        if len(audio) < max_len:
            audio = np.pad(audio, (0, max_len - len(audio)))
        melspec = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128)
        log_melspec = librosa.power_to_db(melspec)
        return log_melspec
    except Exception as e:
        print(f"Error with {file_path}: {e}")
        return None

# Load data
def load_data():
    genres = os.listdir(DATA_PATH)
    X, y = [], []

    for genre in genres:
        genre_path = os.path.join(DATA_PATH, genre)
        if not os.path.isdir(genre_path):
            continue
        for filename in tqdm(os.listdir(genre_path), desc=f"Processing {genre}"):
            if filename.endswith(".wav"):
                file_path = os.path.join(genre_path, filename)
                features = extract_features(file_path)
                if features is not None:
                    X.append(features)
                    y.append(genre)
    return np.array(X), np.array(y)

# Load and preprocess
X, y = load_data()
X = X[..., np.newaxis]  # Add channel dimension
print(f"Feature shape: {X.shape}")

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_cat = to_categorical(y_encoded)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=42)

# CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=X_train.shape[1:]),
    MaxPooling2D((2, 2)),
    Dropout(0.3),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.3),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(np.unique(y)), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train model
history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

# Save model
model.save("music_genre_cnn_model.h5")
print("Model saved successfully!")
