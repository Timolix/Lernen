import threading
import time

class myThread(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name

    def run(self):
        print("Starte", self.iD)
        time.sleep(self.iD*3)
        print("Beende", self.iD)

t1 = myThread(1, "t1")
t2 = myThread(2, "t2")

t1.start()
t2.start()

print("Beende Main")