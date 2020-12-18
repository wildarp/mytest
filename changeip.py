import ipaddress

net = ipaddress.IPv4Network('192.168.0.1/28')
iprange = net.hosts()

for addr in iprange:
    print(addr)
