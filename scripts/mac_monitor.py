#!/usr/bin/env python3

import json
import socket
import netifaces
import subprocess
import time
from datetime import datetime

LOG_FILE = "/var/ossec/logs/mac_monitor.log"

INTERFACE = None

for iface in netifaces.interfaces():
    if iface == "lo":
        continue
    try:
        addr = netifaces.ifaddresses(iface)
        if netifaces.AF_LINK in addr:
            INTERFACE = iface
            break
    except:
        pass

if INTERFACE is None:
    print("No network interface found.")
    exit()


def get_mac():
    return netifaces.ifaddresses(INTERFACE)[netifaces.AF_LINK][0]["addr"]


def get_ip():
    try:
        return netifaces.ifaddresses(INTERFACE)[netifaces.AF_INET][0]["addr"]
    except:
        return "Unknown"


def get_gateway():
    try:
        gws = netifaces.gateways()
        return gws["default"][netifaces.AF_INET][0]
    except:
        return "Unknown"


def get_dns():
    try:
        with open("/etc/resolv.conf") as f:
            for line in f:
                if line.startswith("nameserver"):
                    return line.split()[1]
    except:
        pass
    return "Unknown"


hostname = socket.gethostname()
vendor = subprocess.getoutput(
    "cat /sys/class/net/{}/address".format(INTERFACE)
)

old_mac = get_mac()
change_count = 0

print("Monitoring MAC address on", INTERFACE)
print("Current MAC:", old_mac)

while True:

    current = get_mac()

    if current != old_mac:

        change_count += 1

        event = {
            "event": "MAC_INVESTIGATION",
            "timestamp": datetime.now().isoformat(),
            "hostname": hostname,
            "interface": INTERFACE,
            "ip_address": get_ip(),
            "default_gateway": get_gateway(),
            "dns_server": get_dns(),
            "old_mac": old_mac,
            "new_mac": current,
            "permanent_mac": old_mac,
            "vendor": vendor,
            "randomized": "YES",
            "change_count": change_count
        }

        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")

        print(json.dumps(event, indent=4))

        old_mac = current

    time.sleep(5)
                     
