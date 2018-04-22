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
    
    def get_Process_Pid(self):
        return self.pid
    
    def set_Process_Pid(self, value):
        self.pid = value
        
    def get_Process_Name(self):
        return self.process_name
    
    def set_Process_Name(self, value):
        self.process_name = value
    
    def get_Process_CurrentTime(self):
        return self.current_time
    
    def set_Process_CurrentTime(self, value):
        self.current_time = value
        
    def get_Process_CreateTime(self):
        return self.create_time
    
    def set_Process_CreateTime(self, value):
        self.create_time = value
    
    def get_Computer_Name(self):
        return self.computer_name
    
    def set_Computer_Name(self, value):
        self.computer_name = value
        
    def set_Process_Status(self, value):
        self.process_status = value
        
    def get_Process_Status(self):
        return self.process_status
    
    def __str__(self):
        return str(self.pid)+','+str(self.process_name)+','+str(self.current_time)+','+str(self.create_time)+','+str(self.computer_name)+','+str(self.process_status)
    
    def __getitem__(self):
        return (self.pid,self.process_name,self.current_time,self.create_time,self.computer_name,self.process_status)
    