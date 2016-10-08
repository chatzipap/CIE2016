'''
Σηματοδότης ρυθμιζόμενος ανά ώρα
by tchatz
'''
from gpiozero import LED
from time import sleep
from datetime import datetime

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
    cHour = datetime.today().hour # cHour = τρέχουσα ώρα
    if  cHour == 7 or cHour == 15 or cHour == 23 :
        # Αυξημένη ροή αυτοκινήτων
        red.on()
        sleep(11)
        buzzer.on()
        sleep(2)
        buzzer.off()
        red.off()
        green.on()
        sleep(9)
        green.off()
        orange.on()
        sleep(2)
        orange.off()
    else :
        # Κανονική ροή αυτοκινήτων
        red.on()
        sleep(13)
        buzzer.on()
        sleep(2)
        buzzer.off()
        red.off()
        green.on()
        sleep(7)
        green.off()
        orange.on()
        sleep(2)
        orange.off()

        
    

    
