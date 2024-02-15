import psutil
import ctypes
import info

def find_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None

def read_memory(process_id, address, variable_type):
    process_handle = ctypes.windll.kernel32.OpenProcess(0x10 | 0x20, False, process_id)
    # value = ctypes.c_uint16()
    value = variable_type
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, ctypes.byref(value), ctypes.sizeof(value), None)
    ctypes.windll.kernel32.CloseHandle(process_handle)
    return value.value

def read_unicode_memory(process_id, address, max_length=256):
    process_handle = ctypes.windll.kernel32.OpenProcess(0x10 | 0x20, False, process_id)
    buffer = ctypes.create_unicode_buffer(max_length)
    read_bytes = ctypes.c_ulong(0)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, buffer, max_length * ctypes.sizeof(ctypes.c_wchar), ctypes.byref(read_bytes))
    ctypes.windll.kernel32.CloseHandle(process_handle)
    return buffer.value[:read_bytes.value]

def find_final_addres(process_id, base_address, offsets=[]):
    final_address = read_memory(process_id, base_address, ctypes.c_int32())
    if offsets:
        for offset in offsets[:-1]:
            final_address += offset
            final_address = read_memory(process_id, final_address, ctypes.c_int32())
        final_address += offsets[-1]
    return final_address

def read_memory_with_offSets(process_id, variable_type, base_address, offsets=[]):
    final_address = find_final_addres(process_id, base_address, offsets)
    value_from_memory = read_memory(process_id, final_address, variable_type)
    return value_from_memory

def read_unicode_memory_with_offsets(process_id, base_address, offsets=[], max_length=256):
    final_address = find_final_addres(process_id, base_address, offsets)
    value_from_memory = read_unicode_memory(process_id, final_address, max_length)
    return value_from_memory

