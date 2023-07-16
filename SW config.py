
enable

conf t

hostname S2

enable password cisco

username rohan password 0 cisco

interface Vlan1
 no sh
 ip address 192.168.122.134 255.255.255.0

line vty 0 4
 login local
 transport input all
 end

wr



R1 192.168.122.122
S1 192.168.122.120
S2 192.168.122.132
S3 192.168.122.133




