
# ClearSpeak: Pronunciation Evaluation and Feedback System

ClearSpeak is an interactive application designed to help users improve their pronunciation by evaluating spoken words against reference text. It uses advanced speech recognition, phoneme analysis, and pitch detection to provide detailed feedback on pronunciation accuracy and fluency.

---

## Features

- **Speech Recognition**: Transcribes user speech into text using Google Speech Recognition API.  
- **Phoneme Analysis**: Converts text into phonemes and compares them with reference phonemes to detect pronunciation errors.  
- **Pitch Extraction**: Analyzes the pitch of recorded audio to assess tonal accuracy.  
- **Similarity Scoring**: Calculates a similarity score between the user's speech and the reference text.  
- **Feedback Mechanism**: Provides actionable feedback on pronunciation and highlights differences at the phoneme level.  
- **Interactive UI**: A user-friendly interface built with Tkinter for seamless user interaction.  
- **Dataset Integration**: Dynamically loads reference data (text and pitch) from an external dataset.

---

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.8+
- Libraries:
  - `speech_recognition`
  - `librosa`
  - `pygame`
  - `nltk`
  - `pandas`
  - `requests`
  - `tkinter`
- Dataset: Ensure the reference dataset (`dataset2.xlsx`) is placed in the project directory.

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/clearspeak.git
   cd clearspeak
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Download NLTK data:  
   ```bash
   python -m nltk.downloader cmudict
   ```

4. Place the dataset (`dataset2.xlsx`) in the project directory.

---

## Usage

1. Run the application:  
   ```bash
   python clearspeak.py
   ```

2. Follow the on-screen instructions:  
   - Click **Start** to begin the evaluation.
   - Speak the displayed reference text after pressing OK.
   - View detailed feedback on your pronunciation accuracy.

3. To exit, click the **Quit** button.

---

## Project Structure

```
ClearSpeak/
│
├── dataset2.xlsx         # Reference dataset containing text and pitch data
├── clearspeak.py         # Main application script
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

---

## Future Enhancements

- **Multilingual Support**: Add support for multiple languages and accents.
- **Custom Feedback**: Provide suggestions for improvement based on detected errors.
- **Mobile Version**: Develop a mobile app for on-the-go pronunciation training.
- **Gamification**: Introduce gamified elements to enhance user engagement.

---

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Google Speech Recognition API](https://pypi.org/project/SpeechRecognition/)
- [Librosa](https://librosa.org/)
- [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [StreamElements Text-to-Speech](https://streamelements.com/)

---
