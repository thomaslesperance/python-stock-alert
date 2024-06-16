"""Exports class to be used by other scripts for setting and checking a minute time interval
"""
from datetime import datetime

class Timer():
    """To be instantiated and its methods called for the purpose of doing something at a given minute time interval"""

    def __init__(self):
        self.current_minutes = datetime.now().minute
    
    def get_current_minutes(self):
        return self.current_minutes
    
    def set_current_minutes(self):
        self.current_minutes = datetime.now().minute

    def check_current_minutes(self, limit):
        """@limit will be used to set the rate at which the stock api is checked.
        @limit should be an integer and represent minutes.
        """

        time_elapsed = abs(datetime.now().minute - self.get_current_minutes())

        if time_elapsed >= int(limit):
            return True
