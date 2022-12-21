scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")
# Output was:
#Found a service on 192.168.3.10 at 80
#Found a service on 192.168.3.11 at 443
#Found a service on 192.168.3.55 at 22