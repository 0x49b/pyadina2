import threading
import time
import sys
import random
import webview

from printing.Printing import Printing


class Api:
    config = {
        0: {
            "name": "Han",
            "image": "food.png"
        },
        1: {
            "name": "Padme",
            "image": "food.png"
        },
        2: {
            "name": "Obi-Wan",
            "image": "food.png"
        }
    }

    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response

    def getConfig(self):
        return self.config

    def getRandomNumber(self):
        response = {
            'message': 'Here is a random number courtesy of bola randint: {0}'.format(random.randint(0, 100000000))
        }
        return response

    def doHeavyStuff(self):
        time.sleep(0.1)  # sleep to prevent from the ui thread from freezing for a moment
        now = time.time()
        self.cancel_heavy_stuff_flag = False
        for i in range(0, 1000000):
            _ = i * random.randint(0, 1000)
            if self.cancel_heavy_stuff_flag:
                response = {'message': 'Operation cancelled'}
                break
        else:
            then = time.time()
            response = {
                'message': 'Operation took {0:.1f} seconds on the thread {1}'.format((then - now),
                                                                                     threading.current_thread())
            }
        return response

    def cancelHeavyStuff(self):
        time.sleep(0.1)
        self.cancel_heavy_stuff_flag = True

    def sayHelloTo(self, name):
        response = {
            'message': 'Hello {0}!'.format(name)
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')

    def placeOrder(self, order):
        print(order)
        printing = Printing()
        printing.print_customer_receipt()


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Pyadina', 'index.html', js_api=api, width=800, height=480)
    webview.start()
