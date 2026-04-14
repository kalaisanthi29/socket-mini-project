import socket

hostname = "example.com"

ip = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip}")
