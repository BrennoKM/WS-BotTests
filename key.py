import ctypes
import time


VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_RETURN = 0x0D
VK_Q = 0x51
VK_NUMPAD1 = 0x61

target_process_name = "Warspear Online"
hwnd = ctypes.windll.user32.FindWindowW(None, target_process_name)

def press_key(key_code):
    ctypes.windll.user32.PostMessageW(hwnd, 0x100, key_code, 0)  # WM_KEYDOWN
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(hwnd, 0x101, key_code, 0)  # WM_KEYUP


def press_keyW(key_code):
    ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(key_code, 0, 0x2, 0) 


if __name__ == "__main__":
    press_key(VK_LEFT)
    