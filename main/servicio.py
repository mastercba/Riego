# servicio.py


from machine import Pin, I2C
from time import sleep
from . import ulcd1602


adc = Pin(36, Pin.IN, Pin.PULL_UP)                    # ADC 36
WT = Pin(25, Pin.OUT, value=1)                    # Water Tank
RG = Pin(26, Pin.OUT, value=1)                         # RieGo
MZ = Pin(27, Pin.OUT, value=1)                        # MeZcla
NT = Pin(14, Pin.OUT, value=1)                     # NuTre A&B
i2cR = I2C(-1, sda=Pin(18), scl=Pin(19), freq=400000)# i2c Pin
lcdR = ulcd1602.LCD1602(i2cR)                    # LCD1602 OBJ


class Riegos:
    def __init__(self):
        print('start rutinas....')
        #rutinaRiego()

# ---------------------------------------------------------
def llenarTanque():
    print('llenamos tanque de agua')
    dog = 1
    num = 0
    WT.off()
    sleep(2)
    while adc.value() == 0:            # 0:vacio
        print("{}vacio".format(adc.value()))
        dog = dog + 1
        print(dog)
        sleep(2) #2
        if dog == 50:
            if num == 2:
                print('FAIL!')
                lcdR.puts("no", 2, 1)
                return False       #tanque vacio
            num=num+1
            dog=1
            WT.on()
            sleep(10)
            WT.off()
    WT.on()
    sleep(2)
    print('ok')
    lcdR.puts("ok", 2, 1)    
    return True                    #tanque lleno
# ---------------------------------------------------------
def mezclar():
    print('mezclar tanques')
    MZ.off()                             # MZ ON
    sleep(240)# en segundos
    MZ.on()                             # MZ OFF
# ---------------------------------------------------------  
def riego():
    print('riego')
    RG.off()                             # RG ON
    sleep(360)#60=1minuto
    RG.on()                             # RG OFF
# ---------------------------------------------------------