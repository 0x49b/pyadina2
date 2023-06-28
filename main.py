import webview
from printing.Printing import Printing
import json
import sqlite3


class Api:
    config = {}
    db = None
    cur = None

    def __init__(self, config):
        self.cancel_heavy_stuff_flag = False
        self.config = config

    def getConfig(self):
        return self.config

    def placeOrder(self, order):
        print(order)
        self.store_order(order)
        printing = Printing()
        printing.print_customer_receipt()

    def store_order(self, order):
        logfile = open("orders.txt", "a")
        logfile.write(order + "\n")
        logfile.close()


if __name__ == '__main__':
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)
        print("Read Config successful")

    api = Api(config["piadina"])
    window = webview.create_window('Pyadina', 'index.html',
                                   js_api=api,
                                   width=config["system"]["width"],
                                   height=config["system"]["height"],
                                   frameless=json.loads(config["system"]["frameless"].lower()),
                                   fullscreen=json.loads(config["system"]["fullscreen"].lower()))

    webview.start(debug=json.loads(config["system"]["debug"].lower()))
