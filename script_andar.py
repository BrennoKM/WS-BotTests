import addres
import key
import pyautogui as pg


pg.sleep(2)

while addres.map_x() != 117:
    if addres.cursor_flag() != 4: 
        while addres.cursor_x() != 27:
            if addres.map_x() != 117:
                key.press_key(key.VK_RIGHT)
                if addres.cursor_flag() == 13:
                    key.press_key(key.VK_RETURN)
        if addres.player_x() != 27:
            key.press_key(key.VK_DOWN)
    key.press_key(key.VK_RETURN)    




