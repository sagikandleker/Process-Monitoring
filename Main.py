import os
import sys
import psutil
import time
from Process_Details import ProcessDetails

from time import gmtime, strftime
   
log_file = open('processList.csv', 'a+')
status_file = open('Status_Log.csv', 'a+')
name = os.getenv('COMPUTERNAME')
y = {}
m = {}
first_flag = True
start_scan = 0
end_scan = 0
#log_file_infected = When the file touched
#status_file_infected = When the file touched

def getCurrentTime():
    
    """
        Return the date and time is now
    """
    return strftime("%d/%m/%Y %H:%M:%S")

def getCurrentDate():
    return strftime("%d/%m/%Y")
    
def write_LogFile():
    
    """ 
        Write Processes information to LogFile.txt
        Example -
        "05/04/2018 10:23:45 DESKTOP-HB3DSMF 17/03/2018 20:32:38 System Idle Process 0"
    """
    
    print 'Writing LogFile'
    for key in y:
        log_file.write(y[key] + '\n')
        
    print 'Finish to Writing to LogFile'
    log_file.flush()
    
def read_LogFile(start = 0, end =0):
    print 'Reading LogFile'
    for line in log_file:
        print line
        
    print 'Finish to Read the LogFile'
    
def write_StatusFile(process_name, process_status):
    
    """
        Write information about the processes that changed.
        Example -
        "05/04/2018 10:23:58 DESKTOP-HB3DSMF 05/04/2018 10:23:52 ts3client_win64.exe 3084 is Opened"
    """
    
    print 'Writing StatusFile\n'
    
    print (process_name+' is '+process_status+'\n')
    status_file.write(process_name+' is '+process_status+'\n')
    
    print 'Finish to Writing to StatusFile'
    status_file.flush()

def read_StatusFile():
    
    """ Read information about processes that changed. """
    
    print 'Read StatusFile'
    print 'Finish to Read the StatusFile'
    
def getInfo(start, end):
    pass

def infectedTesting():
    pass

def compare(y,m):
    
    """
        Compare between Old Processes sampling to New Processes sampling.
        And find if Process closed or opened in the sampling range.
    
    """
    
    # This loop will find if Process is Closed.
    for i in y:
        if i not in m:
            write_StatusFile(y[i], 'Closed')
    
    # This loop will find if Process is Opened. 
    for i in m:
        if i not in y:
            write_StatusFile(m[i], 'Opened')
    
def swap(y, m):
    
    """
        Move all the values of Process from m (The new sampling processes) to y (The new sampling processes).
        First, clear y. 
        Second, fill y with values from m.
        Finally, clear m.
        
    """
    
    print 'Start to swap from m to y'
    y.clear()
    
    for i in m:
        temp = m[i]
        y[i] = temp
    
    m.clear()
    
    print 'Finish to swap'
    
def monitor(samplingTime):
    
    """
        Main loop for application.
    """
    
    build_Dictionary(y)
    
    while 1:
        
        print '-------------------------'
        write_LogFile()
        time.sleep(samplingTime)
        build_Dictionary(m)
        compare(y,m)
        swap(y, m)

def time_Format(create_time):
    fixed_create_time = create_time[8:10]+'/'+create_time[5:7]+'/'+create_time[0:4]+' '+create_time[11:20]
    return fixed_create_time

def check_Create_Time(k):
    create_time = psutil._pprint_secs(k.create_time())
    if len(create_time) >= 19:
        return time_Format(create_time)
    else:
        return getCurrentDate() +' '+ create_time
    
def build_Dictionary(value):
    
    """
        Build Dictionary with information about the processes sampling.
        Structure of the dictionary -
            Key = PID Number
            Value = ProcessDetails struct. (Read more about the struct information)
        
        Example, "{0: '05/04/2018 10:36:10 DESKTOP-HB3DSMF 17/03/2018 20:32:38 System Idle Process 0}"
        
    """
    
    for i in psutil.pids():
        try:
            k = psutil.Process(i)
            
            real_create_time = check_Create_Time(k)
                
            if k.status() == 'running':
                
                x = ProcessDetails(getCurrentTime(), name, real_create_time, k.name(), str(i), k.status())
                value[i] = x.getAll()
        except Exception:
            print('Exeption Catch!')
    
#samplingTime = input('Enter sample time: \n')
samplingTime = 10
monitor(samplingTime)
log_file.close()
status_file.flush()
status_file.close()


    