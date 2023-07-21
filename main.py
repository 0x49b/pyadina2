from datetime import date, datetime
import time
import webview
from printing.Printing import Printing
import json
import sqlite3

from storage.Storage import Storage



class Api:
    config = {}
    db = None
    cur = None
    storage = None
    printing = None

    def __init__(self, config):
        self.cancel_heavy_stuff_flag = False
        self.config = config
        self.printing = Printing(config)
        self.storage = Storage()

    def getConfig(self):
        return self.config

    def placeOrder(self, order):
        order_number = self.storage.get_current_order() + 1
        order_json = json.loads(order)

        today = date.today()
        time = datetime.now()
        d = today.strftime("%d.%m.%Y")
        h = time.strftime("%H:%M:%S.%f")

        print("{} order N° {}".format(order, order_number))

        self.storage.add_order([order_number, order_json["0"], order_json["1"], order_json["2"], order, h, d])
        self.printing.print_receipt(order_json, order_number, True, 'customer.pdf')
        import time
        time.sleep(2.5)
        self.printing.print_receipt(order_json, order_number, False, 'kitchen.pdf')


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
