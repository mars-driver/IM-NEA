# ACCESSES: GUI

from GUI.gui import GUI_main

# CONSTANTS
HOMEHOST = "192.168.1.122"
SCHOOLHOST = "10.56.80.140"
LOCALHOST = "127.0.0.1"
DADHOST = "127.0.1.1"
GRANNYHOST = "192.168.1.138"
MARSHOST = "10.77.32.14"
MY_PORT = 13108

GUI_main(SCHOOLHOST, MY_PORT)

#todo: working on disconnecting from chat room & being able to reconnect (i think i got it?)