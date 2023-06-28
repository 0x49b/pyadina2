import os
from fpdf import FPDF
import qrcode

'''
sudo apt-get update && sudo apt-get install cups cups-client lpr

import os
os.system("lpr -P printer_name printMe.txt")

# Printer Name
# ZJ-58
'''


class Printing(object):
    def __init__(self):
        print("starting printer")

    def print_customer_receipt(self):
        filename = 'order.pdf'

        pdf = FPDF('P', 'mm')
        pdf.add_page()
        pdf.image('./static/logo.jpeg', w=35, h=35, x=6, y=5)
        #pdf.set_font('Arial', 'B', 24)
        num = '#42'
        swi = pdf.get_string_width(num)
        pdf.set_y(48)
        pdf.set_x((52 / 2) - (swi / 2))
        pdf.cell(w=43, h=0, txt=num)
        pdf.image('./static/instagram.jpeg', w=5, h=5, x=0, y=55)
        # pdf.set_font('Arial', '', 12)
        pdf.set_y(57.5)
        pdf.set_x(6)
        ist = 'neophytbadenfahrt'
        iwi = pdf.get_string_width(ist)
        pdf.cell(w=iwi, h=0, txt=ist)
        pdf.write('\n\n\n')
        pdf.output(filename, 'F')

        os.system("lpr -P ZJ-58 " + filename)
        # subprocess.run(["lp", filename])
