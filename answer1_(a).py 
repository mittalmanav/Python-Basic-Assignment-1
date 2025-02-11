# Q1. Write a Python program to perform the following: 
# Validate a given public IP address to check if it follows the correct format (IPv4).
ip= input("enter the ip address")

def valid_ipv4(ip):
    parts = ip.split(".")
    
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    
    return True

def public_ip(ip):
    if not valid_ipv4(ip):
        return False 

    parts = list(map(int, ip.split(".")))

 
    if (parts[0] == 10) or (parts[0] == 172 and 16 <= parts[1] <= 31) or (parts[0] == 192 and parts[1] == 168) or (parts[0] == 127) or (parts[0] == 169 and parts[1] == 254):
        return False 

    return True 
print(valid_ipv4(ip))