import wmi

def change_ip_address(new_ip, subnet_mask):
    c = wmi.WMI()

    network_config = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    for config in network_config:
        try:
            result = config.EnableStatic(IPAddress=[new_ip], SubnetMask=[subnet_mask])
            if result[0] == 0:
                print("IP address changed successfully.")
            else:
                print("Failed to change IP address.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Set the new IP address and subnet mask
new_ip_address = "192.168.0.100"  # Replace with an unused IP address on your LAN
subnet_mask = "255.255.255.0"    # Replace with the appropriate subnet mask

# Call the function to change the IP address
change_ip_address(new_ip_address, subnet_mask)