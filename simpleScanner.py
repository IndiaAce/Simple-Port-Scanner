#! add your directory here

"""
PLEASE ONLY USE THIS PORT SCANNER FOR ETHICAL PURPOSES ONLY. 
I'M UPLOADING MY ETHICAL HACKING JOURNEY TO GITHUB TO TRACK MY PROCESS.
"""
import sys
import socket
from datetime import datetime

count = 0

rangeOne = input('Enter your port range start \n e.g. "50": ')
rangeTwo = input('Enter your port range end \n e.g. "85": ')

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print('INVALID AMOUNT OF ARGUMENTS.')
	print('Syntax: python3 scanner.py <ip>')
	
#Add a pretty banner
print('-' * 50)
print('Scanning target '+ target)
print('Time started: '+ str(datetime.now()))
print('-' * 50)

try:
	for port in range(int(rangeOne), int(rangeTwo)):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		#This will timeout the scanner after 1 second on each port (saves lots of time)
		result = s.connect_ex((target,port)) #returns an error indicator 
		if result == 0:
			count += 1
			print('Port {} is open'.format(port))
		s.close()
		
except KeyboardInterrupt:
	print('\nExiting program.')
	sys.exit()
	#If user hits 'ctr c' the program will exit at any time
	
except socket.gaierror:
	print('Hostname could not be resolved.')
	sys.exit()
	#If the host can't be found the program will exit
	
except socket.error:
	print('Could not establish server connection.')
	sys.exit()
	#If the server can't be found the program will exit 

#Add a pretty closer banner
print('-' * 50)
print('Succesfully scanned ' + target + '!')
print('Scanner found ' + str(count) + ' ports open')
print('-' * 50)
