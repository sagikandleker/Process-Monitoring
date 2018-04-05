import os
import sys
import psutil
import time
from time import gmtime, strftime

class ProcessDetails:
    
    """
        This struct of Process with the Details about him (for each process).
    """
    
    def getAll(self):
        return self.current_time +' '+ self.computer_name +' '+ self.create_time +' '+ self.process_name +' '+ self.pid
    
    def __init__(self, cut, con, crt, prn, pid, status):
        self.current_time = cut
        self.computer_name = con
        self.create_time = crt
        self.process_name = prn
        self.pid = pid
        self.status = status
        
        
    def getCurrent(self):
        return str(self.current_time)
    
    def getComputerName(self):
        return str(self.computer_name)
    
    def getStatus(self):
        return str(self.status)
    
    def setStatus(self, value):
        self.status = value