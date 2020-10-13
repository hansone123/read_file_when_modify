import os
import time
import threading

def follow(name, buffer:list):
    current = open(name, "r")
    last_mtime = os.fstat(current.fileno()).st_mtime
    while True:
        while True:
            content = current.read()
            if not content:
                break
            buffer.clear()
            buffer.append(content)

        try:
            if os.stat(name).st_mtime != last_mtime:
                new = open(name, 'r')
                current.close()
                current = new
                last_mtime = os.fstat(current.fileno()).st_mtime
                continue
        except IOError:
            pass
        time.sleep(0.1)
        
def test(fname, buffer):
    while True:
        print('test')
        time.sleep(1)
    
if __name__ == '__main__':
    
    fname = "logfile.txt"
    buffer = []
    t = threading.Thread(target=follow, args=(fname, buffer,), daemon=True)
    t.start()
    while True:
        if len(buffer) >0:
            print(buffer[0], end='')
        time.sleep(1)