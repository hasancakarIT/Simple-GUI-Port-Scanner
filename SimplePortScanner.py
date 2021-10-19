#imports libraries
import socket
from tkinter import *
from tkinter import ttk

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
    target = targetBox.get()
    #port range
    firstPort = IntVar(GUI, 1)
    lastPort = IntVar(GUI, 1023)
    #first port to be scanned
    firstPortBox = Entry(GUI, textvariable=firstPort)
    #last port to be scanned
    lastPortBox = Entry(GUI, textvariable=lastPort)
    #scrolling ouput box
    output = Listbox(GUI, width=50, height=20)
    #sets the range of user insputs
    portRange = range(int(firstPortBox.get()), int(lastPortBox.get()))
    port = portRange[0]
    #function for port scan
    def portScan(port):
        #deletes any previous list content
        output.delete(0,'end')
        s.bind((target, port))
        #while the port is less than or equal to the final port
        while int(lastPortBox.get()) >= port:
            #if failure to connect
            if s.connect((s.bind((target, port)))):
                output.insert(port, str(port) + ": Open")
                None
            #if successfully connects
            elif s.connect_ex((target, port)):
                output.insert(port, str(port) + ": Open")
            #incrementally increases port
            port = int(port + 1)
    #portscan button
    targetBox.pack(pady=5)
    firstPortBox.pack(pady=5)
    lastPortBox.pack(pady=5)
    scanButton = Button(GUI, text="Scan", command=lambda: portScan(port)).pack(pady=5)
    output.pack(pady=5)
    #loop for running GUI#
    GUI.mainloop()

#calls function to run program
scanner()
