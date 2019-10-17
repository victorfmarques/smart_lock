import RPi.GPIO as gpio
import I2C_LCD_driver
import socket
import fcntl
import struct
import time
import menu_lcd

UP = 16
DOWN = 21
LEFT = 20
RIGHT = 12
control = 0

#Inicializa os GPIOs
gpio.setmode(gpio.BCM)
gpio.setup(UP, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(DOWN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(LEFT, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(RIGHT, gpio.IN, pull_up_down = gpio.PUD_DOWN)
#gpio.add_event_detect(DOWN, gpio.RISING, callback=menu_lcd.main)

#Inicializa display LCD I2C
lcdi2c = I2C_LCD_driver.lcd()

#Exibe informacoes iniciais
lcdi2c.lcd_display_string("  SMART LOCK", 1,1)
lcdi2c.lcd_display_string("Security System", 2,1)
time.sleep(3)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

def main():
    try:     
        while True:
            #Mostra a data no display
            lcdi2c.lcd_clear()
            lcdi2c.lcd_display_string("IP", 1)
            lcdi2c.lcd_display_string(get_ip_address('wlan0'), 1,3)
            lcdi2c.lcd_display_string("Data: %s" %time.strftime("%d/%m/%y"), 2,1)
            gpio.wait_for_edge(DOWN, gpio.FALLING) 
            menu_lcd.main()
    except KeyboardInterrupt:     
    #except Exception:
            lcdi2c.lcd_clear()
            gpio.cleanup()
            exit()
    
main()    
    
