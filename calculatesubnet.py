# Subnet Calculator

def subnet_calculator(ip, subnet_bits):
    # Convert IP to binary
    ip_octets = [int(octet) for octet in ip.split('.')]
    ip_binary = ''.join(f'{octet:08b}' for octet in ip_octets)

    # Calculate subnet mask
    subnet_mask_binary = '1' * subnet_bits + '0' * (32 - subnet_bits)
    subnet_mask_octets = [int(subnet_mask_binary[i:i+8], 2) for i in range(0, 32, 8)]
    subnet_mask = '.'.join(map(str, subnet_mask_octets))

    # Calculate network address
    network_binary = ip_binary[:subnet_bits] + '0' * (32 - subnet_bits)
    network_octets = [int(network_binary[i:i+8], 2) for i in range(0, 32, 8)]
    network_address = '.'.join(map(str, network_octets))

    # Calculate broadcast address
    broadcast_binary = ip_binary[:subnet_bits] + '1' * (32 - subnet_bits)
    broadcast_octets = [int(broadcast_binary[i:i+8], 2) for i in range(0, 32, 8)]
    broadcast_address = '.'.join(map(str, broadcast_octets))

    # Calculate usable host range
    first_usable_host = network_octets[:3] + [network_octets[3] + 1]
    last_usable_host = broadcast_octets[:3] + [broadcast_octets[3] - 1]

    # Return results as a dictionary
    return {
        "ip_address": ip,
        "cidr_notation": f"/{subnet_bits}",
        "subnet_mask": subnet_mask,
        "network_address": network_address,
        "broadcast_address": broadcast_address,
        "usable_host_range": f"{'.'.join(map(str, first_usable_host))} - {'.'.join(map(str, last_usable_host))}",
        "total_usable_hosts": 2 ** (32 - subnet_bits) - 2
    }

def conver_to_cidr(ip, subnet_mask):
    # Convert subnet mask to CIDR notation
    subnet_bits = sum(bin(int(octet)).count('1') for octet in subnet_mask.split('.'))  # Count the number of 1's in the mask
    return ip, subnet_bits  # Return the IP and subnet bits

def are_ips_in_same_range(ip1, subnet_mask1, ip2, subnet_mask2):
    # Convert both IPs and subnet masks to CIDR notation
    ip1, subnet_bits1 = conver_to_cidr(ip1, subnet_mask1)
    ip2, subnet_bits2 = conver_to_cidr(ip2, subnet_mask2)

    # Calculate network addresses and broadcast addresses for both IPs
    network1 = subnet_calculator(ip1, subnet_bits1)["network_address"]
    broadcast1 = subnet_calculator(ip1, subnet_bits1)["broadcast_address"]

    network2 = subnet_calculator(ip2, subnet_bits2)["network_address"]
    broadcast2 = subnet_calculator(ip2, subnet_bits2)["broadcast_address"]

    # Check if IP1 is within the range of IP2's network
    ip1_in_range_of_ip2 = network2 <= ip1 <= broadcast2

    # Check if IP2 is within the range of IP1's network
    ip2_in_range_of_ip1 = network1 <= ip2 <= broadcast1

    # Return True if both conditions are met
    return ip1_in_range_of_ip2 and ip2_in_range_of_ip1
