import time

class Timer:
    def __init__(self, enable=True):
        self.enable = enable
        self.start = None
    
    def run(self):
        if self.enable:
            self.start = time.perf_counter()
    
    def stop(self, label="Tiempo"):
        if self.enable and self.start is not None:
            self.end = time.perf_counter()
            print(f"{label}: {self.end - self.start}")