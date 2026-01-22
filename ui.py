import tkinter as tk

class TypingUI:
    def __init__(self, root, text, engine, timer):
        self.root = root
        self.engine = engine
        self.timer = timer

        self.running = False
        self.finished = False

        self.root.title("Typing Speed Test")
        self.root.geometry("900x540")
        self.root.resizable(False, False)

        # Title
        tk.Label(
            root, text="Typing Speed Test",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=12)

        # Display text
        self.display = tk.Text(
            root, height=4, width=95,
            font=("Consolas", 16),
            wrap="word",
            bd=0
        )
        self.display.pack(pady=8)
        self.display.insert("1.0", text)
        self.display.config(state="disabled")

        self.display.tag_config("correct", foreground="green")
        self.display.tag_config("wrong", foreground="red")

        # Input
        self.input_box = tk.Text(
            root, height=7, width=95,
            font=("Consolas", 14),
            wrap="word"
        )
        self.input_box.pack(pady=12)

        self.input_box.bind("<KeyPress>", self.start)
        self.input_box.bind("<KeyRelease>", self.on_type)

        # Timer
        self.timer_label = tk.Label(root, text="Time: 60s")
        self.timer_label.pack()

        # Result
        self.result_label = tk.Label(
            root, font=("Segoe UI", 14, "bold")
        )
        self.result_label.pack(pady=10)

        # Button
        tk.Button(
            root, text="Start / Restart",
            command=self.reset,
            width=15
        ).pack(pady=8)

    # ---------- CONTROL ----------
    def start(self, event):
        if not self.running and not self.finished:
            self.running = True
            self.timer.start()
            self.update_timer()

    def update_timer(self):
        if self.finished:
            return

        remaining = self.timer.remaining_seconds()
        self.timer_label.config(text=f"Time: {remaining}s")

        if remaining > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.finish()

    def on_type(self, event):
        if not self.running or self.finished:
            return

        typed = self.input_box.get("1.0", tk.END).rstrip()

        self.display.config(state="normal")
        self.display.tag_remove("correct", "1.0", tk.END)
        self.display.tag_remove("wrong", "1.0", tk.END)

        for index, correct in self.engine.compare(typed):
            tag = "correct" if correct else "wrong"
            self.display.tag_add(tag, f"1.{index}", f"1.{index+1}")

        self.display.config(state="disabled")

    def finish(self):
        self.running = False
        self.finished = True

        typed = self.input_box.get("1.0", tk.END).rstrip()
        correct = self.engine.correct_chars(typed)

        wpm = self.engine.wpm(correct, self.timer.elapsed_minutes())
        acc = self.engine.accuracy(correct, len(typed))

        self.timer_label.config(text="Time Over")
        self.result_label.config(
            text=f"WPM: {wpm} | Accuracy: {acc:.2f}%"
        )

    def reset(self):
        self.running = False
        self.finished = False

        self.input_box.delete("1.0", tk.END)
        self.display.config(state="normal")
        self.display.tag_remove("correct", "1.0", tk.END)
        self.display.tag_remove("wrong", "1.0", tk.END)
        self.display.config(state="disabled")

        self.timer_label.config(text="Time: 60s")
        self.result_label.config(text="")
