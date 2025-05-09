# Subnet Calculator

def subnet_calculator(ip, subnet_bits):
    # Convert IP to binary
    ip_octets = [int(octet) for octet in ip.split('.')]  # Split IP into octets and convert to integers
    ip_binary = ''.join(f'{octet:08b}' for octet in ip_octets)  # Convert each octet to binary and join them

    # Calculate subnet mask
    subnet_mask_binary = '1' * subnet_bits + '0' * (32 - subnet_bits)  # Create binary subnet mask
    subnet_mask_octets = [int(subnet_mask_binary[i:i+8], 2) for i in range(0, 32, 8)]  # Convert binary mask to octets
    subnet_mask = '.'.join(map(str, subnet_mask_octets))  # Join octets into a dotted-decimal format

    # Calculate network address
    network_binary = ip_binary[:subnet_bits] + '0' * (32 - subnet_bits)  # Set host bits to 0
    network_octets = [int(network_binary[i:i+8], 2) for i in range(0, 32, 8)]  # Convert binary to octets
    network_address = '.'.join(map(str, network_octets))  # Join octets into a dotted-decimal format

    # Calculate broadcast address
    broadcast_binary = ip_binary[:subnet_bits] + '1' * (32 - subnet_bits)  # Set host bits to 1
    broadcast_octets = [int(broadcast_binary[i:i+8], 2) for i in range(0, 32, 8)]  # Convert binary to octets
    broadcast_address = '.'.join(map(str, broadcast_octets))  # Join octets into a dotted-decimal format

    # Calculate usable host range
    first_usable_host = network_octets[:3] + [network_octets[3] + 1]  # First usable host is network + 1
    last_usable_host = broadcast_octets[:3] + [broadcast_octets[3] - 1]  # Last usable host is broadcast - 1

    # Print results
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Usable Host Range: {'.'.join(map(str, first_usable_host))} - {'.'.join(map(str, last_usable_host))}")
    print(f"Total Usable Hosts: {2 ** (32 - subnet_bits) - 2}")

def conver_to_cidr():
    # Prompt user for IP address and subnet mask
    ip = input("Enter the IP address: ")
    subnet_mask = input("Enter the subnet mask: ")
    # Convert subnet mask to CIDR notation
    subnet_bits = sum(bin(int(octet)).count('1') for octet in subnet_mask.split('.'))  # Count the number of 1's in the mask
    print(f"CIDR Notation: {ip}/{subnet_bits}")  # Display CIDR notation
    return ip, subnet_bits  # Return the IP and subnet bits

# Main execution
ip, subnet_bits = conver_to_cidr()  # Get IP and subnet bits from user
subnet_calculator(ip, subnet_bits)  # Pass them to the subnet calculator