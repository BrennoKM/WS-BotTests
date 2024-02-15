import addres
import pyautogui as pg

# if True:
while True:
    print("\n\nMapa Info")
    print(addres.map_id())
    print(addres.map_x())
    print(addres.map_y())
    print(addres.map_layer())
    print(addres.map_qnt_player())
    pg.sleep(2)