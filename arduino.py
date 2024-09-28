import os
try:
    import pyfirmata
except:
    os.system('pip install pyfirmata')
    import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')
servo = board.get_pin('d:9:s')
servo.write(90)
servo.write(180)
servo.write(0)
board.exit()