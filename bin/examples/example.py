'''
Created on Apr 7, 2013

@author: mbertram
'''
import stirplate, time


""" connect to the stir plate."""
device = stirplate.stirPlate()

device.connect()
#device.Off()

""" Set stir plate speed in RPM."""
device.set_stir_speed(800)
""" Turn stir plate on."""
device.On()


time.sleep(60)

""" Turn stir plate off."""
device.Off()