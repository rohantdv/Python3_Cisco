This is an example of how to config SSH on Cisco Switch:
    
    
enable
cisco
config t
username rohan pass cisco
username rohan priv 15

line vty 0 4
login local
transport input all

ip domain-name cciepython.com
crypto key generate rsa
1024

end
wr
