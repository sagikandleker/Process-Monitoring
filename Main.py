import os
import sys
import psutil
import time
import datetime

from datetime import datetime
from Process_Details import *
from Write_CSV_File import *
from time import gmtime, strftime

computer_name = os.getenv('COMPUTERNAME')
modified_time = ""

def getCurrentTime():
    
    """ Return the date and time is now. """
    return strftime("%d/%m/%Y %H:%M:%S")

def getCurrentDate():
    
    """ Return the date is now. """
    return strftime("%d/%m/%Y")
  
def read_LogFile(event_1, event_2, filename):
    
        i = 0
        with open(filename, 'r') as f:
            event_1_dict = {}
            event_2_dict = {}
            array = []
            
            for line in f:
                array.append(line.split(","))
    
                if(event_1 == array[i][2] or event_2 == array[i][2]):
                    
                        if(event_1 == array[i][2]):
                            event_1_dict[array[i][0]] = array[i]
                        else:
                            event_2_dict[array[i][0]] = array[i]
                        
                i = i+1
         
        
        if(len(event_1_dict) == 0 and len(event_2_dict) == 0):
            print "Your date and time didn't found"
            sys.exit(1)
        
        elif(len(event_1_dict) == 0 or len(event_2_dict) == 0):
            if(len(event_1_dict) == 0):
                print "Your first date and time didn't found"
                sys.exit(1)
            else:
                print "Your second date and time didn't found"
                sys.exit(1)
                
        compare_2(event_1_dict, event_2_dict)
            
        f.close()

def compare_1(status_file, old_sample, new_sample):
    
    """
        Compare between Old Processes sampling to New Processes sampling.
        And find if Process closed or opened in the sampling range. 
    """
    
    # This loop will find if Process is Closed.
    for i in old_sample:
        if i not in new_sample:
            write_StatusFile(status_file, old_sample[i], 'Closed')
    
    # This loop will find if Process is Opened. 
    for i in new_sample:
        if i not in old_sample:
            write_StatusFile(status_file, new_sample[i], 'Opened')
    
def swap(old_sample, new_sample):
    
    """ 
        Move all the values of Process from new_sample (The new sampling processes) to old_sample (The new sampling processes).
        First, clear old_sample. 
        Second, fill old_sample with values from new_sample.
        Finally, clear new_sample.
    """
    
    old_sample.clear()
    
    for i in new_sample:
        temp = new_sample[i]
        old_sample[i] = temp
    
    new_sample.clear()
    
def monitor(samplingTime):
    
    """ Main loop for application. """

    exiting_File()
    log_file = open('processList.csv', 'a+')
    status_file = open('Status_Log.csv', 'a+')
    old_sample = {}
    new_sample = {}
    build_Dictionary(old_sample)
    try:
        while 1:
            print '-------------------------'
            write_LogFile(old_sample, log_file)
            
            time.sleep(samplingTime)
            build_Dictionary(new_sample)
            compare_1(status_file, old_sample, new_sample)
            swap(old_sample, new_sample)
    except KeyboardInterrupt:
        sys.exit(1)

def compare_2(event_1_dict, event_2_dict):
     
    # This loop will find if Process is Closed.    
    for i in event_1_dict:
        if i not in event_2_dict:
            event_1_dict[i][5] = 'Closed'
            print event_1_dict[i]
            
    
    # This loop will find if Process is Opened. 
    for i in event_2_dict:
        if i not in event_1_dict:
            event_2_dict[i][5] = 'Opened'
            print event_2_dict[i]
    
def time_Format(create_time):
    fixed_create_time = create_time[8:10]+'/'+create_time[5:7]+'/'+create_time[0:4]+' '+create_time[11:20]
    return fixed_create_time

def check_Creation_Time(k):
    create_time = psutil._pprint_secs(k.create_time())
    if len(create_time) >= 19:
        return time_Format(create_time)
    else:
        return getCurrentDate() +' '+ create_time
    
def modification_date(path_file):
    ans = os.path.getmtime(path_file)
    infectedTesting(ans);
    modified_time = ans
    return datetime.datetime.fromtimestamp(ans)

def exiting_File():
    
    """
        Checking if the files is was created.
        If not, Create the file and write Headers.
    
    """
    
    if(not(os.path.isfile('.'+"//processList.csv"))):
        log_file = open('processList.csv', 'a+')
        write_Headers(log_file)
    else:
        log_file = open('processList.csv', 'a+')
            
    if(not(os.path.isfile('.'+"//Status_Log.csv"))):
        status_file = open('Status_Log.csv', 'a+')
        write_Headers(status_file)
    else:
        status_file = open('Status_Log.csv', 'a+')


def build_Dictionary(value):
    
    """
        Build Dictionary with information about the processes sampling.
        Structure of the dictionary -
            Key = PID Number
            Value = ProcessDetails struct. (Read more about the struct information)
        
        Example, "{0: '0 System Idle Process 05/04/2018 10:36:10 17/03/2018 20:32:38 DESKTOP-HB3DSMF running}"   
    """
    current_time = getCurrentTime()
    
    for i in psutil.pids():
        try:
            k = psutil.Process(i)
            
            real_create_time = check_Creation_Time(k)
            
            if k.status() == 'running':
                   
                x = ProcessDetails(str(i), k.name(), current_time, real_create_time, computer_name, k.status())
                value[i] = x
                
        except Exception:
            pass

def accepted_Value(value):
    
    """ Making sure that input is 0,1,2 integer value. """
    
    counter = 0

    while value.isdigit() == False:
        if(value == 'quit'):
            print("The program closed.")
            sys.exit(1)
        else:
            if(counter > 5):
                print("You are blocked!")
                sys.exit(1)
            value = raw_input("Your input is wrong! try again: ")
            counter += 1
    return int(value)

def integer_Value(value):
    
    """ Making sure that input is integer value. """
    
    counter = 0
    
    while value.isdigit() == False:
        if(value == 'quit'):
            print("The program closed.")
            sys.exit(1)
        else:
            if(counter > 5):
                print "You are blocked!"
                sys.exit(1)
            value = raw_input("Your input is wrong! try again: ")
            counter += 1
    return int(value)

def pattern_Value(value):
    
    """ Making sure that input is format of date and time. """
    
    counter = 0
    
    while True:
        if(value == 'quit'):
            print("The program closed.")
            sys.exit(1)
        try:
            datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
            return value
        except ValueError:
            if(counter > 5):
                print("Your are blocked!")
                sys.exit(1)
            value = raw_input("Your input is wrong! try again: ")
            counter += 1
            
def file_Found():
    if(not(os.path.isfile('.'+"//processList.csv"))):
        print "The file is not was created, Please make sure that program ran before on Process Monitoring. (Restart and press 1)"
        sys.exit(1)
                  
def Interface():
    
    """ Interface for user """
      
    flag = True
    print("Hello! This is a Processes Monitoring program.\n")
    
    while flag:
        ans = accepted_Value(raw_input("Press 1 for starting processes monitoring || Press 2 for inserting time samples || Press 0 or quit for exit Anywhere: "))
        
        
        
        if(ans == 0):
            print("The program closed.")
            flag = False
            sys.exit(1)
            
        elif(ans == 1):
            samplingTime = integer_Value(raw_input("Write time for sampling (Example, 10. The program take sampling every 10 seconds): "))
        
            print("The program started working, every %d seconds the program take sampling of your computer processes." % samplingTime)
            print("For each 2 samples, a comparison is made.")
            print("We will report for you for each changes with the processes.")
            print("You can take a look on the files - ProcessList.csv and Status_Log.csv")

            monitor(samplingTime)
            log_file.close()
            status_file.close()
        
        elif(ans == 2):
            event_1 = pattern_Value(raw_input("Write the date and time for the first event you want to compare (Example, 13/04/2018 12:35:29): "))
            event_2 = pattern_Value(raw_input("Write the date and time for the second event you want to compare (Example, 14/04/2018 22:49:18): "))
            
            file_Found()
            
            print("The program starting work")
            print("First sample time is: %s" % event_1)
            print("Second sample time is: %s" % event_2)
            print '-------------------------'
            
            filename = '.'+'//processList.csv'
            read_LogFile(event_1, event_2, filename)
            flag = False

Interface()
