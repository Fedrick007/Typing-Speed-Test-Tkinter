import tkinter as tk
from engine import TypingEngine
from timer import TestTimer
from ui import TypingUI

TEXT = (
    "Software engineering is a discipline that combines logical thinking, creativity, "
    "and consistent practice. Developers write code to solve real world problems, "
    "build reliable systems, and improve user experiences. Typing efficiently helps "
    "programmers work faster, reduce mistakes, and focus more on problem solving rather "
    "than mechanics. Regular typing practice builds speed, accuracy, and long term confidence."
)

if __name__ == "__main__":
    root = tk.Tk()

    engine = TypingEngine(TEXT)
    timer = TestTimer(60)
    TypingUI(root, TEXT, engine, timer)

    root.mainloop()
