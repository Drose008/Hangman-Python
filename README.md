# Hangman-Python
Python based Hangman game with difficulty levels, dataset integration, hint, and  CLI gameplay.

## 🚀 Features

* 🎯 Difficulty levels (Easy, Normal, Hard)
* 📊 Word selection using dataset
* 💡 One-time hint system
* 🎮 Interactive command-line (CLI) gameplay
* 🔁 Replay option after game ends


## 🛠️ Tech Stack

* Python
* Pandas


## 📊 Dataset

Word dataset derived from the English words dataset on Kaggle, processed using Pandas for word selection and difficulty-based filtering.

**Source:** (https://www.kaggle.com/datasets/jiprud/words-en)

## 📁 Project Structure


hangman-python/
│── hangman.py
│── README.md
│── .gitignore
│── words.csv



## ▶️ How to Run
git clone https://github.com/Drose008/hangman-python.git
Navigate to the folder: cd hangman-python
Run the game: python hangman.py

## 💡 How It Works

* The game selects a random word from a dataset
* Words are filtered based on difficulty levels
* The player guesses letters with limited attempts
* A one-time hint reveals a hidden letter
* ASCII visuals display the hangman progress


## ✨ Future Improvements

* GUI version using Tkinter
* Score tracking system
* Better dataset organization using CEFR levels (A1–C1)
* Rare hint trigger (only in hard mode) showing word meaning
* Fewer letters revealed in hard mode


## 👩‍💻 Author

Built as part of learning Python and improving problem-solving skills.

