print(" \033[1;32;40m                   +----------------------------------------------------------------+ ")
print(" \033[1;32;40m                   |  ____                         __  __                           | ")
print(" \033[1;32;40m                   | /\  _`\                      /\ \/\ \                          | ")        
print(" \033[1;32;40m                   | \ \,\L\_\     __      ___    \_\ \ \ \___      __      ___     | ")
print(" \033[1;32;40m                   |  \/_\__ \   /'__`\  /' _ `\  /'_` \ \  _ `\  /'__`\  /' _ `\   | ")
print(" \033[1;32;40m                   |    /\ \L\ \/\ \L\.\_/\ \/\ \/\ \L\ \ \ \ \ \/\ \L\.\_/\ \/\ \  | ")
print(" \033[1;32;40m                   |    \ `\____\ \__/.\_\ \_\ \_\ \___,_\ \_\ \_\ \__/.\_\ \_\ \_\ | ")
print(" \033[1;32;40m                   |     \/_____/\/__/\/_/\/_/\/_/\/__,_ /\/_/\/_/\/__/\/_/\/_/\/_/ | ")
print(" \033[1;32;40m                   |     >>>>>>>>>>>>Developed By Ayush Ranjan Rout<<<<<<<<<<<      | ")                                    
print(" \033[1;32;40m                   +----------------------------------------------------------------+ ")


import sys
import time
import socket
import threading

usage = "python sandhan.py TARGET START_PORT END_PORT"


start_time = time.time()

if(len(sys.argv) !=4):
	print(usage)
	sys.exit() 

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
      print ("Name Resolution Error")
      sys.exit()	
    
start_port =int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Your Target:",target)

def scan_port(port):

  #print("Scaning Ports:",port)
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(10)
  conn = s.connect_ex((target, port))
  if(not conn):
      print("\033[1;31;40m PORT {} is OPEN " .format(port))
  s.close()

for port in range(start_port, end_port+1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.daemon = True 
    thread.start()


end_time = time.time()	

print (' \033[1;32;40m                              +-------------------------------------+           ')
print (" \033[1;32;40m                              |           Scanning finished         |           ")
print (' \033[1;32;40m                              +-------------------------------------+           ')	
      


