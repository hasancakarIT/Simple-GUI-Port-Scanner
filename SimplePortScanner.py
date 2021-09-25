#imports socket library
import socket
#establishes network connectivity
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#user inputs
host = input("Enter target IP of scan: ")
print("Now enter the range of ports to be scanned.")
firstPort = int(input("Initial port to be scanned: "))
lastPort = int(input("Last port to be scanned: "))
#sets the range of user insputs
portRange = range(firstPort, lastPort)
port = portRange[0]
#prints range of scans
print("Port scan range:",firstPort,"-",lastPort)
#function for port scan
def portScan(port):
    #while the port is less than or equal to the final port
    while lastPort >= port:
        #if failure to connect
        if s.connect_ex((host, port)):
            print(str(port) + ": Closed")
        #if successfully connects
        else:
            print(str(port) + ": Open")
        #incrementally increases port
        port = int(port + 1)
#calls function
portScan(port)
