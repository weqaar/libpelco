import serial
import sys
from commands_struct_PELCO import *


class PELCO_Functions():

	def __init__(self):
		global commands_struct 
		commands_struct = libpelco_structs()

	# Returns: tuple (command, length of command)
	# Input: Address (optional), command2, pan_speed, tilt_speed
	def _construct_cmd(self, _command2, _pan_speed, _tilt_speed, _address = '\x01', _command1 = '\x00'):

		# DEBUG
		print "DEBUG _construct_cmd: " + str(_command2) + " " + str(_pan_speed) + " " + str(_tilt_speed) + "\n"

		# Synch Byte
		commands_struct._frame['synch_byte'] = commands_struct._frame['synch_byte']
		
		# Address
		commands_struct._frame['address'] = _address

		# Command1
		commands_struct._frame['command1'] = _command1

		# Command2
		if _command2 not in commands_struct._function_code:
			print  str(_command2) + " not in commands_struct._function_code\n"
			return False
		else:
			commands_struct._frame['command2'] = commands_struct._function_code[_command2]
			print "_command2 is: " + commands_struct._frame['command2'].encode('hex') + "\n"

		# Data1: Pan Speed
		print "_pan_speed is: " + str(_pan_speed) + "\n"
		_hex_pan_speed = hex(_pan_speed)[2:]
		if len(_hex_pan_speed) is 1:
			_hex_byte_pan = '0' + _hex_pan_speed
		else:
        		_hex_byte_pan = _hex_pan_speed
		commands_struct._frame['data1'] = _hex_byte_pan.decode('hex')

		# Data2: Tilt Speed
		_hex_tilt_speed = hex(_tilt_speed)[2:]
		if len(_hex_tilt_speed) is 1:
			_hex_byte_tilt = '0' + _hex_tilt_speed
		else:
        		_hex_byte_tilt = _hex_tilt_speed
		commands_struct._frame['data2'] = _hex_byte_tilt.decode('hex')

		# Checksum
		_payload_bytes = commands_struct._frame['address'] + commands_struct._frame['command1'] + \
				 commands_struct._frame['command2'] + \
				 commands_struct._frame['data1'] + commands_struct._frame['data2']

		#_checksum = hex(self.checksum256(_payload_bytes))[2:].decode('hex')
		_checksum = hex(self.checksum256(_payload_bytes))[2:]
		if len(_checksum) is 1:
			_corrected_checksum = '0' + _checksum
		else:
        		_corrected_checksum = _checksum
		commands_struct._frame['checksum'] = _corrected_checksum.decode('hex')

		print "_checksum is: " + commands_struct._frame['checksum'] + "\n"

		# assemble command
		_cmd = commands_struct._frame['synch_byte'] + _payload_bytes + commands_struct._frame['checksum']

		print "Final _cmd: \n"
		for i in commands_struct._frame:
			print i + " : " + commands_struct._frame[i].encode('hex')
		print "\n"

		return (_cmd, None) 


	############ Commands #################################################################

	### STOP #############################################
	# 
	def pantilt_stop(self):
		retval = self._construct_cmd('STOP', 0, 0)
		return retval


	### UP ############################################### 

	def pantilt_up_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('UP', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_up_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval


	### UP-RIGHT #########################################

	def pantilt_up_right_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('UP-RIGHT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_up_right_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### UP-LEFT #########################################

	def pantilt_up_left_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('UP-LEFT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_up_left_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### DOWN #########################################

	def pantilt_down_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('DOWN', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_down_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### DOWN-RIGHT #########################################

	def pantilt_down_right_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('DOWN-RIGHT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_down_right_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### DOWN-LEFT #########################################

	def pantilt_down_left_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('DOWN-LEFT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_down_left_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### LEFT #########################################

	def pantilt_left_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('LEFT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_left_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	### RIGHT #########################################

	def pantilt_right_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('RIGHT', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_right_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval


	### PAUSE #########################################

	def pantilt_pause_pressed(self, _pan_tilt_speed):
		retval = self._construct_cmd('PAUSE', int(_pan_tilt_speed[0]), int(_pan_tilt_speed[1]))
		return retval

	def pantilt_pause_released(self, _pan_tilt_speed):
		retval = self.pantilt_stop()
		return retval

	############ Supporting Functions #############

	def checksum256(self, _str):
		return reduce(lambda x,y:x+y, map(ord, _str)) % 256

# EOF
