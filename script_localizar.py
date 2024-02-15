import addres
import key
import pyautogui as pg


pg.sleep(2)

def localizar_x(i):
    while addres.cursor_x() != addres.mob_x(i):
        x = addres.mob_x(i)
        # print(f'{addres.mob_x(i)} mob x')
        if x < addres.cursor_x():
            if addres.cursor_flag() == 13:
                key.press_key(key.VK_RETURN)
            key.press_key(key.VK_LEFT)
        else:
            if addres.cursor_flag() == 13:
                key.press_key(key.VK_RETURN)
            key.press_key(key.VK_RIGHT)

def localizar_y(i):
    while addres.cursor_y() != addres.mob_y(i):
        y = addres.mob_y(i)
        # print(f'{addres.mob_y(i)} mob y')
        if y > addres.cursor_y():
            if addres.cursor_flag() == 13:
                key.press_key(key.VK_RETURN)
            key.press_key(key.VK_DOWN)
        else:
            if addres.cursor_flag() == 13:
                key.press_key(key.VK_RETURN)
            key.press_key(key.VK_UP)

def atacar(i):
    if addres.cursor_flag() == 8 or addres.cursor_flag() == 10:
        while addres.cursor_flag() != 10 and addres.cursor_flag() == 8:
            key.press_key(key.VK_RETURN)
            pg.sleep(1)
            if addres.player_max_mana() > 30:
                key.press_key(key.VK_Q)
            if addres.cursor_flag() == 10:
                key.press_key(key.VK_RETURN)
                pg.sleep(5)
                key.press_key(key.VK_RETURN)

def farmar(vida_max):
    for i in range(999):
        print(f'{i} range     {addres.mob_health(i)} vida')
        if addres.mob_health(i) <= vida_max:
            if addres.mob_max_health(i) == vida_max:
                while addres.mob_health(i) >= 0 and addres.mob_health(i) <= vida_max and addres.mob_max_health(i) == vida_max:
                    print(f'{i} range     {addres.mob_health(i)} vida')
                    if addres.mob_max_health(i) != vida_max:
                        print('             diferente')
                        # break
                    if addres.mob_health(i) <= vida_max:
                        if addres.mob_max_health(i) == vida_max:
                            localizar_x(i)
                            localizar_y(i)
                            atacar(i)
                                         
# vida_max = 203
# vida_max = 181
vida_max = 278
# vida_max = 400
# vida_max = 751
farmar(vida_max)