import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        print "Be careful! Your folder is Infected"