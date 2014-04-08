# Weqaar A. Janjua <weqaar.janjua@sensorflock.com>, 24 MAR 2014
# 
# Structures for Frame and Command Definitions for PELCO-D

class libpelco_structs():

	# Frame format:		|synch byte|address|command1|command2|data1|data2|checksum|
	# Bytes 2 - 6 are Payload Bytes
	_frame = {
		   'synch_byte':'\xFF',		# Synch Byte, always FF		-	1 byte
		   'address':	'\x00',		# Address			-	1 byte
		   'command1':	'\x00',		# Command1			-	1 byte
		   'command2':	'\x00', 	# Command2			-	1 byte
		   'data1':	'\x00', 	# Data1	(PAN SPEED):		-	1 byte
		   'data2':	'\x00', 	# Data2	(TILT SPEED):		- 	1 byte 
		   'checksum':	'\x00'		# Checksum:			-       1 byte
		 }


	# Format: Command Hex Code
	_function_code = {
			  'DOWN':	'\x10',
			  'UP':		'\x08',	
			  'LEFT':	'\x04',
			  'RIGHT':	'\x02',
			  'UP-RIGHT':	'\x0A',
			  'DOWN-RIGHT':	'\x12',
			  'UP-LEFT':	'\x0C',
			  'DOWN-LEFT':	'\x14',
			  'STOP':	'\x00'
			}

# END 
