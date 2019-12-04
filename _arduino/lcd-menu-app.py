import RPi.GPIO as gpio
import I2C_LCD_driver
import socket
import fcntl
import struct
import time
import menu_lcd
import fingerprint
import threading

f = fingerprint.Fingerprint()
finger_flag = True

#Inicializa display LCD I2C
lcdi2c = I2C_LCD_driver.lcd()

#Exibe informacoes iniciais
lcdi2c.lcd_display_string("  SMART LOCK", 1,1)
lcdi2c.lcd_display_string("Security System", 2,1)
time.sleep(3)

def finger_thread_function():
    global finger_flag
    while True:
        if (f.valida_digital() and finger_flag == True):
            menu_lcd.open_door()
        if (finger_flag == False):
            return
        time.sleep(1)
        
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

def main():
    try:
        finger_thread = threading.Thread(target=finger_thread_function)
        finger_thread.start()
        while True:
            #Mostra a data no display
            lcdi2c.lcd_clear()
            lcdi2c.lcd_display_string("IP", 1)
            lcdi2c.lcd_display_string(get_ip_address('wlan0'), 1,3)
            lcdi2c.lcd_display_string("Data: %s" %time.strftime("%d/%m/%y"), 2,1)
            if (menu_lcd.enter_menu()):
                menu_lcd.main()
            time.sleep(1) 
    except KeyboardInterrupt:     
    #except Exception:
            finger_flag = False
            finger_thread.join()
            lcdi2c.lcd_clear()
            gpio.cleanup()
            exit()
    
main()    
    
