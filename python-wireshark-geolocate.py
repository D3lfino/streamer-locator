from geolite2 import geolite2

import socket
import subprocess

cmd = r"/usr/bin/tshark"
# C:\Program Files\Wireshark\tshark.exe -i 6
# Get wireshark working on the 6th interface, which was Ethernet on Windows.

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
my_ip = socket.gethostbyname(socket.gethostname())

reader = geolite2.reader()


def get_ip_location(ip):
    location = reader.get(ip)

    try:
        country = location["country"]["names"]["en"]
    except:
        country = "Unknown"

    try:
        subdivision = location["subdivisions"][0]["names"]["en"]
    except:
        subdivision = "Unknown"

    try:
        city = location["city"]["names"]["en"]
    except:
        city = "Unknown"

    return country, subdivision, city


register = []
ip_f = None
for line in iter(process.stdout.readline, b""):

    columns = str(line).split(" ")

    # r"\xe2\x86\x92"
    if "\\xe2\\x86\\x92" in columns and "UDP" in columns:
        src_ip = columns[columns.index("\\xe2\\x86\\x92") - 1]

        if src_ip in my_ip or src_ip == ip_f:
            continue

        try:
            ip_f = src_ip
            country, sub, city = get_ip_location(src_ip)
            if (country, sub, city) != register:
                print(">>> " + src_ip + ", " + country + ", " + sub + ", " + city)
        except:
            try:
                real_ip = socket.gethostbyname(src_ip)
                ip_f = real_ip
                country, sub, city = get_ip_location(real_ip)
                if (country, sub, city) != register:
                    print(">>> " + real_ip + ", " + country + ", " + sub + ", " + city)
            except:
                ip_f = None
                print("Not found")

# If you get Not Found or None, you can simply search for an ip
# location site and paste the ip that you get in the terminal there.
