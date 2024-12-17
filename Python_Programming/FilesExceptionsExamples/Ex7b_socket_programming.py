# An example script to connect to Google using socket programming with exception handling

import socket # socket module
import sys  # sys module

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created.")

except socket.error as err:
    print ("Socket creation failed with error %s" %(err))


# default port for socket
port = 8080
try:
    host_ip = socket.gethostbyname('www.Google.com')
except socket.gaierror:
    # this means could not resolve the host
    print ("There was an error resolving the host.")
    sys.exit()

try:
    # connecting to the server
    s.connect((host_ip, port))
    print ("The socket has successfully connected to Google.")
except: print("Connection fails.")
