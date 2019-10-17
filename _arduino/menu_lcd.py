import time
from enum import Enum
class STATE(Enum):
    TELA_1 = 1
    TELA_2 = 2
    TELA_3 = 3
    TELA_4 = 4
    TELA_5 = 5
    TELA_6 = 6

if __name__ == "__main__":
    class BUTTON(Enum):
        UP = 1
        DOWN = 2
        ESC = 3
        ENTER = 4
    botao = BUTTON.DOWN.value
else:
    import I2C_LCD_driver
    import RPi.GPIO as gpio
    botao = 0
    UP = 16
    DOWN = 21
    ESC = 20
    ENTER = 12
    PIN_DOOR = 18

    #Inicializa os GPIOs
    gpio.setmode(gpio.BCM)
    gpio.setup(UP, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    gpio.setup(DOWN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    gpio.setup(ESC, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    gpio.setup(ENTER, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    
    gpio.add_event_detect(UP, gpio.RISING)
    gpio.add_event_detect(DOWN, gpio.RISING)
    gpio.add_event_detect(ESC, gpio.RISING)
    gpio.add_event_detect(ENTER, gpio.RISING)
    
    gpio.setup(PIN_DOOR, gpio.OUT)
    gpio.output(PIN_DOOR, gpio.LOW)
    #Inicializa display LCD I2C
    lcdi2c = I2C_LCD_driver.lcd()


state = STATE.TELA_1
control_debug = True
is_pressed_var = False
str_menu_1 = "Cadastrar novo"
str_menu_2 = "Apagar usuario"
str_menu_3 = "Verificar banco"
str_menu_4 = "Apagar banco"
str_menu_5 = "Abrir porta"
str_menu_6 = "Fechar porta"

def debounce(direction):
     counter = 0
     if (gpio.input(direction) == 1):
         counter = 1
     time.sleep(0.1)
     if (gpio.input(direction) == 1):
         counter += 1
         return True
     else:
         return False

def disable_events():
     gpio.remove_event_detect(UP)
     gpio.remove_event_detect(DOWN)
     gpio.remove_event_detect(ESC)
     gpio.remove_event_detect(ENTER)

def enable_events():
     gpio.add_event_detect(UP, gpio.RISING)
     gpio.add_event_detect(DOWN, gpio.RISING)
     gpio.add_event_detect(ESC, gpio.RISING)
     gpio.add_event_detect(ENTER, gpio.RISING)

def generic_method():
    return True

def open_door():
     gpio.output(PIN_DOOR, gpio.HIGH)
     time.sleep(3)
     gpio.output(PIN_DOOR, gpio.LOW)   

    
def close_door():
     gpio.output(PIN_DOOR, gpio.LOW)   

def button_test(button_direction):
    global botao
    if __name__ == "__main__":
        if (botao == BUTTON.button_direction.value):
            return True
        else:
            return False
    else:
        if (botao == button_direction):
            return True
        else:
            return False

def print_screen(string_a, string_b, cursor_pos_x, cursor_pos_y):
    if __name__ == "__main__":
        print (string_a)
        print (string_b)
    else:
        lcdi2c.lcd_clear()
        lcdi2c.lcd_display_string(">", cursor_pos_x, cursor_pos_y)
        lcdi2c.lcd_display_string(string_a, 1, 1)
        lcdi2c.lcd_display_string(string_b, 2, 1)

def update_screen(cursor_pos_x, cursor_pos_y):
    if __name__ == "__main__":
        print (cursor_pos_x)
        print (cursor_pos_y)

    else:
        lcdi2c.lcd_clear()
        lcdi2c.lcd_display_string(">", cursor_pos_x, cursor_pos_y)

def is_pressed():
    global botao
    if __name__ == "__main__":
        botao = input ("UP 1, DOWN 2, ESC 3 e ENTER 4\n")
        if(botao == BUTTON.UP.value  or botao == BUTTON.DOWN.value or botao == BUTTON.ESC.value or botao == BUTTON.ENTER.value):
            return True 
        else:
            return False
    else:
        global UP, DOWN, ESC, ENTER
        
        #if (gpio.event_detected(UP) or gpio.event_detected(DOWN) or gpio.event_detected(ESC) or gpio.event_detected(ENTER)):
        if(gpio.input(UP) == 0):
        #if (gpio.event_detected(UP)): 
            #disable_events()
            #if (debounce(UP)):
                botao = UP
                #enable_events()
                return True
            #enable_events()
        elif (gpio.input(DOWN) == 0):
        #elif (gpio.event_detected(DOWN)):
            #disable_events()
            #if (debounce(DOWN)):
                botao = DOWN
                #enable_events()
                return True 
            #enable_events()
        elif (gpio.input(ESC) == 0):
        #elif (gpio.event_detected(ESC)):
            #disable_events()
            #if (debounce(ESC)):
                botao = ESC
                #enable_events()
                return True
            #enable_events()
        elif (gpio.input(ENTER) == 0):
        #elif (gpio.event_detected(ENTER)):
            #disable_events()
            #if (debounce(ENTER)):
                 botao = ENTER
                 #enable_events()
                 return True 
            #enable_events()
        else:
            return False
        
        

def state_first_screen(string_a, string_b, string_c, string_d, state_up, state_down, method_to_run):
    global state, control_debug, is_pressed_var
    is_pressed_var = False
    
    print_screen(string_a, string_b, 1, 0)
    while (is_pressed_var == False):
        is_pressed_var = is_pressed()

    if (button_test(DOWN)):
        #muda para TELA_2
        update_screen(2, 0)
        state = state_down
            
    elif (button_test(UP)):
        #muda para TELA_6
        print_screen(string_c, string_d, 2, 0)
        state = state_up
            
    elif (button_test(ESC)):
        #sai do menu
        control_debug = False
        return
    elif (button_test(ENTER)):   
        #executa CADASTRO NOVO USUARIO  
        method_to_run()
        #control_debug = False
        return    
    
def state_second_screen(string_a, string_b, string_c, string_d, state_up, state_down, method_to_run):
    global state, control_debug, is_pressed_var
    is_pressed_var = False
    
    print_screen(string_a, string_b, 2, 0)
    while (is_pressed_var == False):
        is_pressed_var = is_pressed()

    if (button_test(DOWN)):
        #muda para TELA_2
        print_screen(string_c, string_d, 1, 0)
        state = state_down
            
    elif (button_test(UP)):
        #muda para TELA_6
        update_screen(1, 0)
        update_screen
        state = state_up
            
    elif (button_test(ESC)):
        #sai do menu
        control_debug = False
        return
    elif (button_test(ENTER)):   
        #executa CADASTRO NOVO USUARIO
        method_to_run()
        #control_debug = False
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
    
def main_debug():
    global control_debug
    while (control_debug != False):
        menu_state_machine()

def main():
    global control_debug
    while (control_debug != False):
        menu_state_machine()
    control_debug = True    

if __name__ == "__main__": 
    main_debug()
    
    
         