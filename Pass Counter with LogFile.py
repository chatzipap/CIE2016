'''
Μετρητής διελεύσεων
by tchatz
'''

from gpiozero import LED, DistanceSensor
from time import sleep
from datetime import datetime

# Αντιστοίχιση στοιχείων και ακίδων GPIO
red = LED(27)
orange = LED(19)
green=LED(5)
buzzer = LED(10)

sensor = DistanceSensor(echo=16, trigger=20)

# Αρχικοποίηση καταστάσεων στοιχείων
red.off()
orange.off()
green.off()
sleep(1)
print ('calibrating distance.')
# Calibrating Start Up Distamce
sum = 0
for i in range(10):
        d = int(sensor.distance * 100)
        sum += d
        sleep(0.5)
state=0        
default = sum /10	# Default Distance
count = 0			# Passing Through Counts
print ('Default=', default)
fo = open('log.txt','a')
try:
        while True:
                d = int(sensor.distance * 100)
                if abs(d-default) <= 2 :
                        state = 0
                sleep(0.2)
                if abs(d-default) > 2 and state ==0:
                        count += 1
                        red.on() ; buzzer.on();
                        sleep(0.1) 
                        buzzer.off();red.off()
                        now = datetime.now()
                        rec = ','.join([str(item) for item in [now,d,count]])
                        rec = str(datetime.now()) + ',' + str(d) + ',' + str(count)
                        print (rec)
                        fo.write(rec + '\n')
                        state = 1

except:
        print ('I/O Error')
finally :
        fo.close()
        print('The End')

        
    

    
