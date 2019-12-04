import time
import I2C_LCD_driver
import RPi.GPIO as gpio
import fingerprint
from pad4pi import rpi_gpio
from enum import Enum

class STATE(Enum):
    TELA_1 = 1
    TELA_2 = 2
    TELA_3 = 3
    TELA_4 = 4
    TELA_5 = 5
    TELA_6 = 6
state = STATE.TELA_1

#Inicializa display LCD I2C
lcdi2c = I2C_LCD_driver.lcd()

control_debug = True
is_pressed_var = False

str_menu_1 = "Cadastrar novo"
str_menu_2 = "Apagar usuario"
str_menu_3 = "Verificar banco"
str_menu_4 = "Apagar banco"
str_menu_5 = "Abrir porta"
str_menu_6 = "Fechar porta"

PIN_DOOR = 21

#Inicializa os GPIOs
gpio.setmode(gpio.BCM)
gpio.setup(PIN_DOOR, gpio.OUT)
gpio.output(PIN_DOOR, gpio.LOW)

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [4, 17, 27, 22] # BCM numbering
COL_PINS = [18, 23, 24, 25] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

last_key_var = 0

UP = KEYPAD[0][3]
DOWN = KEYPAD[1][3]
ESC = KEYPAD[2][3]
ENTER = KEYPAD[3][3]

botao = 0

def printKey(key):
  print(key)
  
def last_key(key):
    global last_key_var
    last_key_var = key
    return last_key_var

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(last_key)

def enter_menu():
    global KEYPAD, botao
    #print last_key_var
    if (last_key_var == KEYPAD[3][0]):
        return True
    else:
        return False
    
def generic_method():
    return True

def open_door():
     gpio.output(PIN_DOOR, gpio.HIGH)
     #time.sleep(3)
     #gpio.output(PIN_DOOR, gpio.LOW)   

    
def close_door():
     gpio.output(PIN_DOOR, gpio.LOW)   
     
def button_test(button_direction):
    if (botao == button_direction):
    #if (last_key_var == button_direction):
        return True
    else:
        return False
        
def print_screen(string_a, string_b, cursor_pos_x, cursor_pos_y):
    lcdi2c.lcd_clear()
    lcdi2c.lcd_display_string(">", cursor_pos_x, cursor_pos_y)
    lcdi2c.lcd_display_string(string_a, 1, 1)
    lcdi2c.lcd_display_string(string_b, 2, 1)

def update_screen(cursor_pos_x, cursor_pos_y):
    lcdi2c.lcd_clear()
    lcdi2c.lcd_display_string(">", cursor_pos_x, cursor_pos_y)


def is_pressed():
    global botao
    #if(gpio.input(ROW_PINS[0]) == 0):
    if (gpio.event_detected(ROW_PINS[0]) and gpio.input(ROW_PINS[0]) == 0): 
        botao = UP
        return True
    #elif (gpio.input(ROW_PINS[1]) == 0):
    elif (gpio.event_detected(ROW_PINS[1])and gpio.input(ROW_PINS[1]) == 0):
        botao = DOWN
        return True 
    #elif (gpio.input(ROW_PINS[2]) == 0):
    elif (gpio.event_detected(ROW_PINS[2])and gpio.input(ROW_PINS[2]) == 0):
        botao = ESC
        return True
    #elif (gpio.input(ROW_PINS[3]) == 0):
    elif (gpio.event_detected(ROW_PINS[3])and gpio.input(ROW_PINS[3]) == 0):
        botao = ENTER
        return True 
    else:
        return False
        
def state_first_screen(string_a, string_b, string_c, string_d, state_up, state_down, method_to_run):
    global state, control_debug, is_pressed_var

    print_screen(string_a, string_b, 1, 0)
    
    is_pressed_var = False
    while (is_pressed_var == False):
        is_pressed_var = is_pressed()

    if (button_test(DOWN)):
        update_screen(2, 0)
        state = state_down
            
    elif (button_test(UP)):
        print_screen(string_c, string_d, 2, 0)
        state = state_up
            
    elif (button_test(ESC)):
        #sai do menu
        control_debug = False
        return
    elif (button_test(ENTER)):
        method_to_run()
        return    
    
def state_second_screen(string_a, string_b, string_c, string_d, state_up, state_down, method_to_run):
    global state, control_debug, is_pressed_var

    print_screen(string_a, string_b, 2, 0)

    is_pressed_var = False
    while (is_pressed_var == False):
        is_pressed_var = is_pressed()

    if (button_test(DOWN)):
        print_screen(string_c, string_d, 1, 0)
        state = state_down
            
    elif (button_test(UP)):
        update_screen(1, 0)
        state = state_up
            
    elif (button_test(ESC)):
        #sai do menu
        control_debug = False
        return
    elif (button_test(ENTER)):   
        method_to_run()
        return       

def menu_state_machine():
    global state
    if (state == STATE.TELA_1):
        state_first_screen(str_menu_1, str_menu_2, str_menu_5, str_menu_6, STATE.TELA_6, STATE.TELA_2, generic_method)
    
    elif (state == STATE.TELA_2):
        state_second_screen(str_menu_1, str_menu_2, str_menu_3, str_menu_4, STATE.TELA_1, STATE.TELA_3, generic_method)
        
    elif (state == STATE.TELA_3): 
        state_first_screen(str_menu_3, str_menu_4, str_menu_1, str_menu_2, STATE.TELA_2, STATE.TELA_4, generic_method)                       

    elif (state == STATE.TELA_4):
        state_second_screen(str_menu_3, str_menu_4, str_menu_5, str_menu_6, STATE.TELA_3, STATE.TELA_5, generic_method)
                
    elif (state == STATE.TELA_5):
        state_first_screen(str_menu_5, str_menu_6, str_menu_3, str_menu_4, STATE.TELA_4, STATE.TELA_6, open_door)

    elif (state == STATE.TELA_6):
        state_second_screen(str_menu_5, str_menu_6, str_menu_1, str_menu_2, STATE.TELA_5, STATE.TELA_1, close_door)
    else:
        return                                      
    
def main():
    global control_debug
    while (control_debug != False):
        menu_state_machine()
    control_debug = True    
    
         