from dothat import lcd
from dothat import backlight
from dothat import touch
import time
lcd.clear()


print('''Santa Tracker!

Built by appledeej on Github.

Press CTRL + C to exit.''')

backlight.rgb(255, 0, 0)
backlight.update
time.sleep(1)
backlight.rgb(0, 255, 0)
backlight.update
time.sleep(1)
backlight.rgb(0, 0, 255)
backlight.update
lcd.set_cursor_position(1, 1) #Startup/splash screen.
lcd.write("Santa Tracker")
lcd.set_cursor_position(1, 2)
lcd.write("appledeej")
lcd.set_cursor_position(1, 0)
lcd.write("Version 0.1")

lcd.clear
backlight.rgb(255, 0, 0)
backlight.update

lcd.set_cursor_position(1, 1)
lcd.write("Santa map: N/A")
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker!")
lcd.write("Santa Flys Soon")
time.sleep(300)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")   #Base template for all countrys
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: South Pacific")

time.sleep(600)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")   
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: New Zealand")

time.sleep(1800)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")  
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: Australia")

time.sleep(1800)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")  
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: Japan")

time.sleep(1800)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")  
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: General Asia")

time.sleep(2700)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")  
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: General Africa")

time.sleep(1800)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Tracker")  
lcd.set_cursor_position(1, 1)
lcd.write("Santa map: Turkey")

time.sleep(300)

lcd.clear()
lcd.set_cursor_position(1, 0)
lcd.write("Santa Is Getting Close! Get into bed!")

while True:
    backlight.off()
    backlight.update
    time.sleep(2)
    backlight.rgb(255, 0, 0)
    









    


