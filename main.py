import speech_recognition as sr
from difflib import SequenceMatcher
import pandas as pd
import random
import os
import librosa
import nltk
import requests
from io import BytesIO
import pygame
import tkinter as tk
from tkinter import messagebox

nltk.download('cmudict')
from nltk.corpus import cmudict

# Function for text-to-speech
def speak(text):
    api_url = "https://api.streamelements.com/kappa/v2/speech"
    params = {'voice': 'Brian', 'text': text.strip()}
    response = requests.get(api_url, params=params) 
    if response.status_code == 200: 
        pygame.mixer.init()
        pygame.mixer.music.load(BytesIO(response.content))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)
    else:
        print(f"Error: {response.status_code}")

# Function to compare similarity between two strings
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Function to extract pitch from audio
def extract_pitch(audio_path):
    y, sr = librosa.load(audio_path)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    return pitches, magnitudes

# Function to get audio duration
def get_audio_duration(audio_path):
    y, sr = librosa.load(audio_path)
    duration = librosa.get_duration(y=y, sr=sr)
    return duration

# Function to convert text to phonemes
def text_to_phonemes(text):
    d = cmudict.dict()
    words = text.lower().split()
    phonemes = []
    for word in words:
        if word in d:
            phonemes.extend(d[word][0])
        else:
            phonemes.append(word)
    return " ".join(phonemes)

# Function to compare phonemes
def compare_phonemes(reference_phonemes, recognized_phonemes):
    matcher = SequenceMatcher(None, reference_phonemes, recognized_phonemes)
    differences = list(matcher.get_opcodes())
    return differences

# Main function that handles speech recognition, phoneme comparison, and pitch comparison
def recognize_and_compare(reference_text, reference_med_pitch, reference_std_pitch):
    recognizer = sr.Recognizer()
    
    # Convert reference text to phonemes
    reference_phonemes = text_to_phonemes(reference_text)
    
    speak(reference_text)  # Read out the reference text
    messagebox.showinfo("Speak", "Press OK and say the text.")
    
    # Record audio
    with sr.Microphone() as source:
        print("\tSay something...")
        audio = recognizer.listen(source, timeout=5)

    temp_wav_path = "temp.wav"
    with open(temp_wav_path, "wb") as temp_wav:
        temp_wav.write(audio.get_wav_data())

    try:
        # Perform speech recognition
        recognized_text = recognizer.recognize_google(audio)
        
        # Extract pitch information from recorded audio
        pitches, _ = extract_pitch(temp_wav_path)

        # Calculate similarity between recognized text and reference text
        similarity_score = similarity(recognized_text.lower(), reference_text.lower())

        # Adjust the threshold based on pitch difference
        abs_pitch_diff = abs(pitches.mean() - reference_med_pitch)
        if abs_pitch_diff > 10:
            similarity_reduction = 0.3
        elif abs_pitch_diff > 6:
            similarity_reduction = 0.2
        elif abs_pitch_diff > 4:
            similarity_reduction = 0.1
        else:
            similarity_reduction = 0.0

        similarity_score -= similarity_reduction

        # Get audio duration
        duration = get_audio_duration(temp_wav_path)

        # Convert recognized text to phonemes
        recognized_phonemes = text_to_phonemes(recognized_text)

        # Compare phonemes and detect mistakes
        differences = compare_phonemes(reference_phonemes, recognized_phonemes)

        # Display results
        result_text = f"Similarity Score: {round(similarity_score, 2)}\nAudio Duration: {round(duration, 2)} seconds\nPhoneme Differences: {differences}"
        if similarity_score >= 0.8:
            result_text += "\nExactly correct!"
        elif similarity_score >= 0.6:
            result_text += "\nNearly correct!"
        elif similarity_score >= 0.4:
            result_text += "\nSlightly correct."
        else:
            result_text += "\nWrong."
        
        messagebox.showinfo("Result", result_text)

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service: {e}")
    finally:
        os.remove(temp_wav_path)

# Function to load random reference text and pitch from the dataset
def load_reference_data():
    random_row = df.sample(1)
    reference_text = random_row['spelling'].values[0]
    reference_med_pitch = random_row['mean_pitch'].values[0]
    reference_std_pitch = random_row['std_pitch'].values[0]
    recognize_and_compare(reference_text, reference_med_pitch, reference_std_pitch)

# Initialize Tkinter window
root = tk.Tk()
root.title("ClearSpeak")

# Load dataset
excel_file_path = r"dataset2 (1).xlsx"
df = pd.read_excel(excel_file_path)

# Check if DataFrame is valid
if not df.empty and 'mean_pitch' in df.columns:
    tk.Label(root, text="Press the button to start pronunciation evaluation").pack(pady=20)
    
    start_button = tk.Button(root, text="Start", command=load_reference_data)
    start_button.pack(pady=10)
    
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)
    
else:
    messagebox.showerror("Error", "The dataset is empty or missing required columns.")

# Run the Tkinter event loop
root.mainloop()
