from datetime import datetime

class CheckTime():
    """To be instantiated and its methods called for the purpose of doing something at a given minute time interval"""

    def __init__(self):
        self.current_time = datetime.now()
        self.time_elapsed = 0
    
    def get_time(self):
        return self.current_time.minute
    
    def set_time(self):
        self.current_time = datetime.now()
    
    def get_time_elapsed(self):
        return self.time_elapsed
    
    def set_time_elapsed(self, time):
        self.time_elapsed = time

    def check_time(self, limit):
        """@limit will be used to set the rate at which the stock api is checked.
        @limit should be an integer and represent minutes.
        """

        old_minutes = self.get_time()
        new_time = datetime.now()
        new_minutes = new_time.minute

        self.set_time_elapsed(abs(new_minutes - old_minutes))

        if self.get_time_elapsed() >= int(limit):
            self.set_time_elapsed(0)
            return True
