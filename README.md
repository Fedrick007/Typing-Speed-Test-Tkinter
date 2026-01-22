# ⌨️ Typing Speed Test – Tkinter

A desktop typing speed test application built using **Python** and **Tkinter**.  
This project measures typing speed and accuracy using real-world typing test logic, similar to popular online typing platforms.

---

## ✨ Features

- 🟢 Real-time character-level feedback (correct / incorrect typing)
- ⚡ Accurate Words Per Minute (WPM) calculation
- 🎯 Accuracy percentage calculation
- 🔄 Continuous text input model
- ⏱️ Timer-based test (60 seconds)
- 🎨 Clean and simple GUI
- 🧩 Modular Object-Oriented Programming (OOP) structure

---

## 🧠 Measurement Logic

The application uses standard industry formulas:

📌 **WPM**  
(Correct Characters ÷ 5) ÷ Elapsed Time (minutes)

📌 **Accuracy**  
(Correct Characters ÷ Total Typed Characters) × 100

Typing measurement starts from the **first keystroke** and uses **actual elapsed time**, ensuring realistic results.

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 🖥️ Tkinter (GUI)
- 🧱 Object-Oriented Programming (OOP)

---

## 📁 Project Structure

typing-speed-test/  
├── main.py        (Entry point)  
├── engine.py      (Typing logic & metrics)  
├── timer.py       (Timer handling)  
└── ui.py          (GUI and controller)

---

## ▶️ How to Run

1️⃣ Clone the repository  
git clone https://github.com/your-username/typing-speed-test-tkinter.git

2️⃣ Navigate to the project folder  
cd typing-speed-test-tkinter

3️⃣ Run the application  
python main.py

---

## 📌 Key Learnings

- 🔁 Event-driven GUI programming with Tkinter
- 🧠 Importance of correct measurement assumptions
- 🧩 Separation of UI and logic using OOP
- 🐞 Debugging real-world logic errors

---

## 🚀 Future Improvements

- 🌙 Dark mode UI
- ♾️ Infinite text generation
- 🗄️ Typing history with SQLite
- 📈 Real-time WPM graph
- 📝 Word-level highlighting

---

## 📄 License

This project is open-source and available for learning and educational purposes.
