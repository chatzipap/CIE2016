'''
Σηματοδότης ρυθμιζόμενος ανά ώρα και ημέρα
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

# Συνάρτηση λειτουργίας σηματοδότη
def trafficLight(tRed, tGreen):
        red.on()
        sleep(tRed - 2)
        buzzer.on()
        sleep(2)
        buzzer.off()
        red.off()
        green.on()
        sleep(tGreen)
        green.off()
        orange.on()
        sleep(2)
        orange.off()
# Λίστες χρόνων
normal = [15,7] # Λίστα με χρόνους κανονικής ροής οχημάτων
high = [13,9] # Λίστα με χρόνους αυξημενης ροής οχημάτων

# Επαναληπτική διαδικασία
while True:
    cHour = datetime.today().hour # cHour = τρέχουσα ώρα
    cDay = datetime.today().weekday() # cDay = τρέχουσα ημέρα της εβδομάδας, 0=Δευτέρα
    if cHour in [7,15,23] and cDay not in [5,6] :
        # Αυξημένη ροή αυτοκινήτων
        trafficLight(*high)
        print ('high')
    else:   
        # Κανονική ροή αυτοκινήτων
         trafficLight(*normal)
         print ('normal')
    
     

        
    

    
