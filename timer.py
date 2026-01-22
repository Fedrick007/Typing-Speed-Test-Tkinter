import time

class TestTimer:
    def __init__(self, limit_seconds: int = 60):
        self.limit = limit_seconds
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def elapsed_seconds(self) -> float:
        return time.time() - self.start_time

    def elapsed_minutes(self) -> float:
        return self.elapsed_seconds() / 60

    def remaining_seconds(self) -> int:
        return max(0, int(self.limit - self.elapsed_seconds()))

    def is_finished(self) -> bool:
        return self.elapsed_seconds() >= self.limit
