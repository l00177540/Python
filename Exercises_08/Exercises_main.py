from Exercise_devices import Firewall
from Exercise_devices import Switch
from Exercise_devices import LoadBalancer

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch10 = Switch("switch10")
# Verify a CRC
switch10.calculate_crc("dummy data")

# Create a load balancer instance
loadbalancer12 = LoadBalancer("loadbalancer12")
# Verify a CRC
loadbalancer12.calculate_crc("dummy data")
