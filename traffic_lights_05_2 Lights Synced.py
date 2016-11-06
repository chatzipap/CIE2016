'''
Δύο φωτεινοί σηματοδότες συγχρονισμένοι
'''

from gpiozero import LED
from time import sleep
from datetime import datetime

# Αντιστοίχιση στοιχείων και ακίδων GPIO
# 1ος & 2ος φωτεινός σηματοδότης
red = ( LED(27),  LED(21) )
orange = ( LED(19),  LED(13) )
green=( LED(5), LED(22) )
buzzer =  LED(10)

print ('Starting Traffic Lights Sequence...')
# Αρχικοποίηση καταστάσεων στοιχείων
red[0].off() ; red[1].on()
orange[0].off() ; orange[1].off()
green[0].on() ; green[1].off()
sleep(5)

# Συνάρτηση λειτουργίας buzzer
def buzzerRing(t):
    buzzer.on()
    sleep(t)
    buzzer.off()
# Συνάρτηση Λειτουργίας Πορτοκαλί Φαναριού
def orangeLight(num,t):
    orange[num].on()
    sleep(t)
    buzzerRing(t)
    orange[num].off()

# Συνάρτηση λειτουργίας σηματοδότη
def trafficLight(tRed, tGreen):
    red[1].on() ; green[1].off() ; red[0].off() ; green[0].on()
    print ('Vehicles Run on Factory ...')
    sleep(tRed - tRed / 10)
    orangeLight(0,tRed/10)
    # buzzerRing()
    red[1].off() ; green[1].on() ; red[0].on() ; green[0].off()
    print ('Vehicles Run On HighWay')
    sleep(tGreen)
    orangeLight(1,tRed/10)
    green[1].off()
# Κύρια Επαναληπτική Διαδικασία
while True :
        trafficLight(10,5)


        
    

    
