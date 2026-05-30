import ipaddress

def subnet_calc(ip_cidr):
    network = ipaddress.ip_network(ip_cidr, strict=False)
    
    print(f"\nInput:       {ip_cidr}")
    print(f"Network:       {network.network_address}")
    print(f"Broadcast:     {network.broadcast_address}")
    print(f"Subnet Mask:   {network.netmask}")
    print(f"Usable Range:  {network.network_address + 1} - {network.broadcast_address - 1}")
    print(f"Usable Hosts:  {network.num_addresses - 2}")

while True:
    user_input = input("Enter IP/CIDR (or 'quit' to exit): ")

    if user_input == "quit":
        break

    subnet_calc(user_input)

# Made on 5/30/2026
# Helpful Subnet Calculator in case you forget how to find usable hosts, ranges, net/broad, etc.
# May not be 100% functional; WIP