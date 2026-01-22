class TypingEngine:
    def __init__(self, reference_text: str):
        self.text = reference_text

    def compare(self, typed: str):
        """
        Returns list of (index, is_correct)
        """
        return [
            (i, typed[i] == self.text[i])
            for i in range(min(len(typed), len(self.text)))
        ]

    def correct_chars(self, typed: str) -> int:
        return sum(
            1 for i, c in enumerate(typed)
            if i < len(self.text) and c == self.text[i]
        )

    def wpm(self, correct_chars: int, minutes: float) -> int:
        if minutes <= 0:
            return 0
        return int((correct_chars / 5) / minutes)

    def accuracy(self, correct_chars: int, total_chars: int) -> float:
        if total_chars == 0:
            return 0.0
        return (correct_chars / total_chars) * 100
