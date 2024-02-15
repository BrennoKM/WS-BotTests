import ctypes
import readM as rm


process_name = "warspear.exe"

process_id = rm.find_process_by_name(process_name)

def map_id():
    # variable: 2 bytes
    # "warspear.exe"+007C7E50
    # offsets: 108 250 E
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x108, 0x250, 0xE]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def map_x():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 108 250 8
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x108, 0x250, 0x8]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def map_y():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 108 250 A
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x108, 0x250, 0xA]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def map_layer():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 108 250 C
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x108, 0x250, 0xC]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def map_qnt_player():
    # variable: 4 bytes
    # base: "warspear.exe"+007C03B0
    # offsets: C 20 4
    base_address = 0x400000 + 0x007C03B0
    offsets = [0xC, 0x20, 0x4]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_id():
    # variable: 4 bytes
    # base: "warspear.exe"+007C03B0
    # offsets: 170 12A4
    base_address = 0x400000 + 0x007C03B0
    offsets = [0x170, 0x12A4]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_name():
    # variable: unicode string
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 58
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x58]
    # variable_type = ctypes.c_uint32()   #unicode string
    value_from_memory = rm.read_unicode_memory_with_offsets(process_id, base_address, offsets)

    return value_from_memory

def player_health():
    # variable: 4 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 100
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x100]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_max_health():
    # variable: 4 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 104
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x104]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_mana():
    # variable: 4 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 108
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x108]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_max_mana():
    # variable: 4 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 10C
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x10C]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_x():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 2F8 4C 2B4 C4 114
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x2F8, 0x4C, 0x2B4, 0xC4, 0x114]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_y():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 2F8 4C 2B4 C4 116
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x2F8, 0x4C, 0x2B4, 0xC4, 0x116]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_x_des():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 2F8 4C 2B4 C4 118
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x2F8, 0x4C, 0x2B4, 0xC4, 0x118]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_x_des():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 2F8 4C 2B4 C4 11A
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x2F8, 0x4C, 0x2B4, 0xC4, 0x11A]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def player_is_moving():
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 10 2F8 4C 2B4 C4 134
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x2F8, 0x4C, 0x2B4, 0xC4, 0x134]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def cursor_x():
    # variable: 2 bytes
    # base: "warspear.exe"+007C03B0
    # offsets: 28 10 4 304 64
    base_address = 0x400000 + 0x007C03B0
    offsets = [0x28, 0x10, 0x4, 0x304, 0x64]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def cursor_y():
    # variable: 2 bytes
    # base: "warspear.exe"+007C03B0
    # offsets: 28 10 4 304 66
    base_address = 0x400000 + 0x007C03B0
    offsets = [0x28, 0x10, 0x4, 0x304, 0x66]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def cursor_flag():
    # variable: 2 bytes
    # base: "warspear.exe"+007C03B0
    # offsets: 28 10 4 304 6C
    base_address = 0x400000 + 0x007C03B0
    offsets = [0x28, 0x10, 0x4, 0x304, 0x6C]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def mob_health(index = 0x0):
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 c 0 8 4 14 100
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0xC, 0x0, 0x8, 0x4, 0x14, 0x100+(0x328*index)]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def mob_max_health(index = 0x0):
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 c 0 8 4 14 100
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0xC, 0x0, 0x8, 0x4, 0x14, 0x104+(0x328*index)]
    variable_type = ctypes.c_uint32()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def mob_x(index = 0x0):
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 c 0 8 4 14 100
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0xC, 0x0, 0x8, 0x4, 0x14, 0x114+(0x328*index)]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory

def mob_y(index = 0x0):
    # variable: 2 bytes
    # base: "warspear.exe"+007C7E50
    # offsets: 0 c 0 8 4 14 100
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0xC, 0x0, 0x8, 0x4, 0x14, 0x116+(0x328*index)]
    variable_type = ctypes.c_uint16()
    value_from_memory = rm.read_memory_with_offSets(process_id, variable_type, base_address, offsets)

    return value_from_memory



# print(map_id())
# print(map_x())
# print(map_y())
# print(map_layer())
# print(player_id())
# print(player_name())
# print(player_health())
# print(player_max_health())
# print(player_mana())
# print(player_max_mana())
# print(player_x())
# print(player_y())
# print(player_is_moving())
# print(cursor_x())
# print(cursor_y())
# print(cursor_flag())
