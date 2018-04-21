import os
import sys
from time import gmtime, strftime
from Process_Details import ProcessDetails


def write_Headers(filename):
    """ Write Headers to the file """
     
    filename.write('PID,Process Name,Writing Time,Creating Time,Using By,Status\n')

def write_LogFile(old_sample, log_file):
    
    """ 
        Write Processes information to LogFile.txt
        Example -
        "05/04/2018 10:23:45 DESKTOP-HB3DSMF 17/03/2018 20:32:38 System Idle Process 0"
    """

    for key in old_sample:
        log_file.write(str(old_sample[key]) + '\n')

    log_file.flush()

def write_StatusFile(status_file, process_details, process_status):
    
    """
        Write information about the processes that changed.
        Example - "05/04/2018 10:23:58 DESKTOP-HB3DSMF 05/04/2018 10:23:52 ts3client_win64.exe 3084 Opened"
    """
    
    process_details.setStatus(process_status)
    interfacePrint(process_details.getPid(), process_details.getName(), process_details.getStatus())
    print strftime("%d/%m/%Y %H:%M:%S")
    if(process_status == 'Closed'):
        process_details.setCurrentTime(strftime("%d/%m/%Y %H:%M:%S"))
    
    status_file.write(str(process_details)+'\n')
    process_details.setStatus('running')
    
    status_file.flush()

def interfacePrint(pid, process_name, process_status):
    print str(pid) +" | "+ str(process_name) +" | "+ str(process_status)

