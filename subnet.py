def subnet_calculator():
    """
    Calculate the subnet mask and CIDR notation for a given IP address and subnet mask.
    """
    ip = "10.0.1.10"
    subnet_mask = "255.255.255.0"
    ip_parts = ip.split('.') #Splits the IP Address into a list of the 4 octets
    subnet_parts = subnet_mask.split('.') #Splits the Subnet Mask into a list of the 4 octets
    ip_parts = [int(part) for part in ip_parts] #Converts the octets to integers
    subnet_parts = [int(part) for part in subnet_parts] #Converts the octets to integers
    octet1 = ip_parts[0] #First octet of the IP Address
    octet2 = ip_parts[1] #Second octet of the IP Address
    octet3 = ip_parts[2] #Third octet of the IP Address
    octet4 = ip_parts[3] #Fourth octet of the IP Address
    subnet1 = subnet_parts[0] #First octet of the Subnet Mask
    subnet2 = subnet_parts[1] #Second octet of the Subnet Mask
    subnet3 = subnet_parts[2] #Third octet of the Subnet Mask
    subnet4 = subnet_parts[3] #Fourth octet of the Subnet Mask

    # Calculate the CIDR notation
    cidr = 0
    print(bin(subnet_parts[0])[2:])
    print(bin(subnet_parts[1])[2:])
    print(bin(subnet_parts[2])[2:])
    print(bin(subnet_parts[3])[2:])
    for part in subnet_parts:
        # Count the number of 1's in the binary representation of the subnet mask
        cidr += bin(part).count('1')

        # Isolate octets that contain 1's

    

    
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"CIDR Notation: /{cidr}")        


subnet_calculator()