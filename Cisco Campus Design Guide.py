vtp mode transparent
spanning-tree mode rapid-pvst
udld enable
errdisable recovery cause all
port-channel load-balance src-dst-ip
ip name-server 8.8.8.8
no ip http server
ip http secure-server

snmp-server community python01 RO
snmp-server community python02 RW

ntp server 87.81.181.2
ntp update-calendar

vlan 100
 name DATA
vlan 101
 name Voice
vlan 102
 name Test
 
interface vlan 1
 description In-band Management

ip default-gateway 192.168.122.120
ip dhcp snooping vlan 100,101

no ip dhcp snooping information option
ip dhcp snooping
ip arp inspection vlan 100,101
spanning-tree portfast bpduguard default


interface GigabitEthernet2/1
switchport
no shutdown
switchport access vlan 100
switchport voice vlan 101
switchport host
switchport port-security maximum 2
switchport port-security aging time 2
switchport port-security aging type inactivity
switchport port-security violation restrict
ip arp inspection limit rate 100
ip dhcp snooping limit rate 100
ip verify source

interface GigabitEthernet2/2
switchport
no shutdown
switchport access vlan 100
switchport voice vlan 101
switchport host
switchport port-security maximum 2
switchport port-security aging time 2
switchport port-security aging type inactivity
switchport port-security violation restrict
ip arp inspection limit rate 100
ip dhcp snooping limit rate 100
ip verify source

interface GigabitEthernet2/3
switchport
no shutdown
switchport access vlan 100
switchport voice vlan 101
switchport host
switchport port-security maximum 2
switchport port-security aging time 2
switchport port-security aging type inactivity
switchport port-security violation restrict
ip arp inspection limit rate 100
ip dhcp snooping limit rate 100
ip verify source
end


wr

show clock


 
