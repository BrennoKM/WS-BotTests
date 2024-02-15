import addres
import key
import pyautogui as pg


pg.sleep(2)

def reiniciar_x_y():
    while addres.cursor_x() != 0:
        key.press_key(key.VK_LEFT)
    while addres.cursor_y() != 0:
        key.press_key(key.VK_UP)

def atacar():
    while addres.cursor_flag() != 10 and addres.cursor_flag() == 8:
        key.press_key(key.press_key(key.VK_RETURN))
        pg.sleep(1)
        if addres.player_max_mana() > 30:
            key.press_key(key.VK_NUMPAD1)
        if addres.cursor_flag() == 10:
            key.press_key(key.VK_RETURN)
            pg.sleep(5)
            key.press_key(key.VK_RETURN)

def x_esq():
    while addres.cursor_x() <= 9:
        if addres.cursor_flag() == 8 or addres.cursor_flag() == 10:
            atacar()
            pg.sleep(2)
        key.press_key(key.VK_RIGHT)

def x_dir():
    while addres.cursor_x() != 0:
        if addres.cursor_flag() == 8 or addres.cursor_flag() == 10:
            atacar()
            pg.sleep(1)
        key.press_key(key.VK_LEFT)

def verificar_area_descendo():
    while addres.cursor_y() < 10:
        x_esq()
        key.press_key(key.VK_DOWN)
        x_dir()
        key.press_key(key.VK_DOWN)

def verificar_area_subindo():
    while addres.cursor_y() > 0:
        x_dir()
        key.press_key(key.VK_UP)
        x_esq()
        key.press_key(key.VK_UP)
        
pg.sleep(2)
while True:
    # reiniciar_x_y()
    verificar_area_descendo()
    verificar_area_subindo()