import logging
import threading
import time

class Arithmetic:
    def __init__(self):
        self.total = 0

    def add(self,num1,num2):
        result = num1 + num2
        logging.info(f"Total = {self.total}")
        logging.info(f"Adding {num1} and {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total+result}\n")
        self.total += result

    def subtract(self,num1,num2):
        result = num1 - num2
        logging.info(f"Total = {self.total}")
        logging.info(f"Subtracting {num1} and {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total + result}\n")
        self.total += result

    def multiplay(self,num1,num2):
        result = num1 * num2
        logging.info(f"Total = {self.total}")
        logging.info(f"Multiplaying {num1} and {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total + result}\n")
        self.total += result

    def run(self):
        t1 = threading.Thread(target=self.add,args=(10,10))
        t1.start()
        t1.join()

        t2 = threading.Thread(target=self.subtract,args=(10,5))
        t2.start()
        t2.join()

        t3 = threading.Thread(target=self.multiplay,args=(5,5))
        t3.start()
        t3.join()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.info("Main: Before thread.\n")

# create an object and run the threads
a = Arithmetic()
a.run()

logging.info("Done")
