import ctypes
import psutil

def find_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None

def read_unicode_memory(process_id, address, max_length=256):
    process_handle = ctypes.windll.kernel32.OpenProcess(0x10 | 0x20, False, process_id)
    
    buffer = ctypes.create_unicode_buffer(max_length)
    read_bytes = ctypes.c_ulong(0)
    
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, buffer, max_length * ctypes.sizeof(ctypes.c_wchar), ctypes.byref(read_bytes))
    
    ctypes.windll.kernel32.CloseHandle(process_handle)
    
    # Retorna a string Unicode com base na quantidade de bytes lidos
    return buffer.value[:read_bytes.value]

def read_unicode_memory_with_offsets(process_id, base_address, offsets=[], max_length=256):
    final_address = base_address
    
    if offsets:
        for offset in offsets:
            # Converte o resultado para um número antes de adicionar o offset
            final_address = int(read_unicode_memory(process_id, final_address)) + offset
    
    # Lê a string Unicode do endereço final
    value_from_memory = read_unicode_memory(process_id, final_address, max_length)
    
    return value_from_memory

# Exemplo de uso
nome_processo = "warspear.exe"
id_processo = find_process_by_name(nome_processo)

if id_processo:
    base_address = 0x400000 + 0x007C7E50
    offsets = [0x0, 0x10, 0x58]
    resultado = read_unicode_memory_with_offsets(id_processo, base_address, offsets)
    print("String da memória:", resultado)
else:
    print(f"Processo '{nome_processo}' não encontrado.")
