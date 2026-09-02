# ACCESSES: GUI

from GUI.gui import GUI_main

# CONSTANTS
homehost = "192.168.1.122"
schoolhost = "10.56.81.120"
localhost = "127.0.0.1"
dadhost = "127.0.1.1"
grannyhost = "192.168.1.138"
my_port = 13108

GUI_main(schoolhost, my_port)