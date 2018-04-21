import os
import sys
import psutil
import time
from time import gmtime, strftime

class ProcessDetails:
    
    """
        This struct of Process with the Details about him (for each process).
    """
    
    pid = 0
    process_name = ''
    current_time = ''
    create_time = ''
    computer_name = ''
    process_status = ''
    
    def getAll(self):
        return (self.pid,self.process_name,self.current_time,self.create_time,self.computer_name,self.process_status)
    
    def __init__(self, pid, process_name, current_time, create_time, computer_name, process_status):
        self.pid = pid
        self.process_name = process_name
        self.current_time = current_time
        self.create_time = create_time
        self.computer_name = computer_name
        self.process_status = process_status
    
    def __str__(self):
        return self.pid+','+self.process_name+','+self.current_time+','+self.create_time+','+self.computer_name+','+self.process_status
    
    def setStatus(self, s):
        self.process_status = s
        
    def getStatus(self):
        return self.process_status
    
    def getPid(self):
        return self.pid
    
    def getName(self):
        return self.process_name
    
    def setCurrentTime(self, t):
        self.current_time = t
        
    def __getitem__(self):
        return (self.pid,self.process_name,self.current_time,self.create_time,self.computer_name,self.process_status)
    