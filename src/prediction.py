def predict_genre(file_path, model, label_encoder):
    features = extract_features(file_path)
    if features is not None:
        features = features[np.newaxis, ..., np.newaxis]
        prediction = model.predict(features)
        genre = label_encoder.inverse_transform([np.argmax(prediction)])
        return genre[0]
    return "Error loading audio"

# Example
# from tensorflow.keras.models import load_model
# model = load_model("music_genre_cnn_model.h5")
# print(predict_genre("test_audio.wav", model, le))
