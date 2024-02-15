import psutil
import ctypes
import struct

def find_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None

def read_memory(process_id, address, variable_type):
    process_handle = ctypes.windll.kernel32.OpenProcess(0x10 | 0x20, False, process_id)
    # value = ctypes.c_uint32()
    value = variable_type
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, ctypes.byref(value), ctypes.sizeof(value), None)
    ctypes.windll.kernel32.CloseHandle(process_handle)
    return value.value

def read_memory_with_offSets(process_id, variable_type, base_address, offsets=[]):
    # final_address = base_address
    final_address = read_memory(process_id, base_address, ctypes.c_int32())
    # print(hex(final_address))
    if offsets:
        for offset in offsets[:-1]:
            final_address += offset
            final_address = read_memory(process_id, final_address, ctypes.c_int32())
        final_address += offsets[-1]
    value_from_memory = read_memory(process_id, final_address, variable_type)
    return value_from_memory

process_name = "warspear.exe"

process_id = find_process_by_name(process_name)
if process_id is not None:
    print(f"Processo {process_name} encontrado (PID: {process_id})")

    base_address = 0x400000 + 0x007C7E50
    # base_address = 0x12A5B640
    offsets = [0, 0x10, 0x100]
    # offsets = []


    variable_type = ctypes.c_uint32()
    # final_address = read_memory(process_id, base_address, variable_type)

    # for offset in offsets[:-1]:
    #     final_address += offset
    #     final_address = read_memory(process_id, final_address, variable_type)
    # final_address += offsets[-1]
    
    value_from_memory = read_memory_with_offSets(process_id, variable_type, base_address, offsets)


    print("Valor lido da memória:", value_from_memory)
else:
    print(f"Processo {process_name} não encontrado.")


# base_address = 0x400000 + 0x007C7E50
# offsets = [0x108, 0x250, 0xE]
# variable_type = ctypes.c_uint32()
# value_from_memory = read_memory_with_offSets(process_id, variable_type, base_address, offsets)
# print(value_from_memory)


base_address = 0x400000 + 0x007C7E50
offsets = [0x108, 0x250, 0x8]
variable_type = ctypes.c_uint16()
value_from_memory = read_memory_with_offSets(process_id, variable_type, base_address, offsets)
# value_from_memory = read_2bytes_memory_with_offsets(process_id, base_address, offsets)
# print(value_from_memory)

print(read_memory(process_id, 0x12CA5990, ctypes.c_int16()))
