import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.total_paused_time = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        if self.start_time is not None:
            self.paused_time = time.time()

    def resume(self):
        if self.paused_time is not None:
            self.total_paused_time += time.time() - self.paused_time
            self.paused_time = None

    def stop(self):
        if self.start_time is not None:
            end_time = time.time()
            elapsed_time = end_time - self.start_time - self.total_paused_time
            print(f'Elapsed time: {elapsed_time:.2f} seconds')
            self.start_time = None
            self.paused_time = None
            self.total_paused_time = 0
            
my_timer = Timer()
my_timer.start()
input()
my_timer.stop()