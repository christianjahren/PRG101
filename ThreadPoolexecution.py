import logging
import threading
import random
import concurrent.futures
import time

class Arithmetic:
    def __init__(self):
        self.total = 0
        self._lock = threading.Lock()

    def add(self,num1,num2):
        logging.info(f"Current total = {self.total}")
        result = num1 + num2
        logging.info(f"Calculating {num1} + {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total + result}")
        self.total += result

    def subtract(self,num1,num2):
        logging.info(f"Current total = {self.total}")
        result = num1 - num2
        logging.info(f"Calculating {num1} - {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total + result}")
        self.total += result

    def multiplay(self,num1,num2):
        logging.info(f"Current total = {self.total}")
        result = num1 * num2
        logging.info(f"Calculating {num1} * {num2} = {result}")
        logging.info(f"New total = {self.total} + {result} = {self.total + result}")
        self.total += result

    def run(self,name):
        logging.info(f"Thread {name} about to lock.")

        with self._lock:
            logging.info(f"Thread {name} has locked.")
            a = random.randint(0, 101)
            b = random.randint(0, 101)
            method_list = [self.add,self.subtract,self.multiplay]
            self.total += random.choice(method_list)(a,b)
            time.sleep(0.5)
            logging.info(f"Thread {name} about to release.")
        logging.info(f"Thread {name} has released!!")

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.info("Main: Before thread")

prg = Arithmetic()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for index in range(10):
        executor.submit(prg.run,index)

logging.info("Done")
logging.info(f"End total: {prg.total}")