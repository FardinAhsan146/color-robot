#Compass Test script by Fardin
# Using the qmc5883l library 
import time
import qmc5883l

mag_sens = qmc5883l.QMC5883L()

if __name__ == '__main__':

	try:
		while 1:
			x, y, z = mag_sens.get_magnet()
			print(f'x heading = {x*100}, y heading = {y*100}')
			time.sleep(2)


	except KeyboardInterrupt:
		print('Stop')



