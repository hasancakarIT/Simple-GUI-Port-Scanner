#imports libraries
import socket
from tkinter import *
from tkinter import ttk

#scan variables
firstPort = 1
lastPort = 1024
log = []
portRange = []
target = 'localhost'

#establishes network connectivity
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#GUI interface
def scanner():
    #interface settings#
    #set up GUI interface
    GUI = Tk()
    #window box title
    GUI.title("Simple Port Scanner")
    #GUI size
    GUI.geometry("450x600")
    #GUI elements#
    #target IP entry
    Label(GUI, text="Enter target to scan and port range below:", font="Helvetica 12").pack()
    targetBox = Entry(GUI)
    #port range
    #first port to be scanned
    firstPortBox = Entry(GUI, text = 1)
    #last port to be scanned
    lastPortBox = Entry(GUI, text = 1023)
    #scrolling ouput box
    output = Listbox(GUI, width=50, height=20)
    #sets the range of user insputs
    #function for port scan
    def portScan():
        #deletes any previous list content
        output.delete(0,'end')
        #sets variables
        firstPort = int(firstPortBox.get())
        lastPort = int(lastPortBox.get())
        target = socket.gethostbyname(str(targetBox.get()))
        #establishes range of ports
        portRange = range(firstPort, lastPort)
        #variable for defining current port
        port = portRange[0]
        #while the port is less than or equal to the final port
        while int(lastPort) >= port:
            #if failure to connect
            if s.connect_ex((target, port)):
                output.insert(port, str(port) + ": Closed")
            else:
                output.insert(port, str(port) + ": Open")
            #incrementally increases port
            port = int(port + 1)
    #portscan button
    targetBox.pack(pady=5)
    firstPortBox.pack(pady=5)
    lastPortBox.pack(pady=5)
    scanButton = Button(GUI, text="Scan", command=lambda: portScan()).pack(pady=5)
    output.pack(pady=5)
    #loop for running GUI#
    GUI.mainloop()

#calls function to run program
scanner()
