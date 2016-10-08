from gpiozero import LED
from time import sleep

# Αντιστοίχιση στοιχείων και ακίδων GPIO
red = LED(27)
orange = LED(19)
green=LED(5)
buzzer = LED(10)

# Αρχικοποίηση καταστάσεων στοιχείων
red.off()
orange.off()
green.off()
sleep(1)

# Επαναληπτική διαδικασία
while True:
    red.on() 
    sleep(15)
    red.off()
    green.on()
    sleep(7)
    green.off()
    orange.on()
    sleep(2)
    orange.off()
    
    

    
