# Hangman-Python
Python based Hangman game with difficulty levels, dataset integration, hint, and  CLI gameplay.

Features
  🎯 Difficulty levels (Easy, Normal, Hard)
  📊 Word selection using dataset
  💡 One-time hint system
  🎮 Interactive command-line gameplay
  🔁 Replay option after game ends
  
🛠️ Tech Stack
Python
Pandas
📊 Dataset
Kaggle dataset

Word dataset derived from the CEFR-levelled English texts dataset on Kaggle, processed using Pandas for dynamic word selection and difficulty-based filtering.

Source: https://www.kaggle.com/datasets/amontgomerie/cefr-levelled-english-texts

📁 Project Structure
hangman-python/
│── hangman.py
│── README.md
│── .gitignore
│── words.csv

▶️ How to Run
Clone the repository: 
git clone https://github.com/your-username/hangman-python.git
Navigate to the folder:
cd hangman-python
Run the game:
python hangman.py

💡 How It Works
   The game selects a random word from a dataset
   Words are filtered based on difficulty levels
   The player guesses letters with limited attempts
   A one-time hint reveals a hidden letter 
   ASCII visuals display the hangman progress
  
✨ Future Improvements
GUI version using Tkinter
Score tracking system
Better dataset and sorted by CEFR levels (A1–C1) for vocab practice
Rare hint trigger (only in hard mode) that tells you the meaning of the word
Few letters given in hard mode 

Author
Built as part of learning Python and improving problem-solving skills.
