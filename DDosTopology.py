#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c1=net.addController(name='c1',
                      controller=Controller,
                      protocol='tcp',
                      port=6634)

    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h49 = net.addHost('h49', cls=Host, ip='10.0.0.49', defaultRoute=None)
    h31 = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    h33 = net.addHost('h33', cls=Host, ip='10.0.0.33', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h37 = net.addHost('h37', cls=Host, ip='10.0.0.37', defaultRoute=None)
    h59 = net.addHost('h59', cls=Host, ip='10.0.0.59', defaultRoute=None)
    h42 = net.addHost('h42', cls=Host, ip='10.0.0.42', defaultRoute=None)
    h50 = net.addHost('h50', cls=Host, ip='10.0.0.50', defaultRoute=None)
    h36 = net.addHost('h36', cls=Host, ip='10.0.0.36', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h62 = net.addHost('h62', cls=Host, ip='10.0.0.62', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h57 = net.addHost('h57', cls=Host, ip='10.0.0.57', defaultRoute=None)
    h46 = net.addHost('h46', cls=Host, ip='10.0.0.46', defaultRoute=None)
    h51 = net.addHost('h51', cls=Host, ip='10.0.0.51', defaultRoute=None)
    h60 = net.addHost('h60', cls=Host, ip='10.0.0.60', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    h52 = net.addHost('h52', cls=Host, ip='10.0.0.52', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h38 = net.addHost('h38', cls=Host, ip='10.0.0.38', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h58 = net.addHost('h58', cls=Host, ip='10.0.0.58', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h44 = net.addHost('h44', cls=Host, ip='10.0.0.44', defaultRoute=None)
    h54 = net.addHost('h54', cls=Host, ip='10.0.0.54', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    h35 = net.addHost('h35', cls=Host, ip='10.0.0.35', defaultRoute=None)
    h45 = net.addHost('h45', cls=Host, ip='10.0.0.45', defaultRoute=None)
    h63 = net.addHost('h63', cls=Host, ip='10.0.0.63', defaultRoute=None)
    h39 = net.addHost('h39', cls=Host, ip='10.0.0.39', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h55 = net.addHost('h55', cls=Host, ip='10.0.0.55', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h53 = net.addHost('h53', cls=Host, ip='10.0.0.53', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h43 = net.addHost('h43', cls=Host, ip='10.0.0.43', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    h56 = net.addHost('h56', cls=Host, ip='10.0.0.56', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h64 = net.addHost('h64', cls=Host, ip='10.0.0.64', defaultRoute=None)
    h47 = net.addHost('h47', cls=Host, ip='10.0.0.47', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h40 = net.addHost('h40', cls=Host, ip='10.0.0.40', defaultRoute=None)
    h34 = net.addHost('h34', cls=Host, ip='10.0.0.34', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h48 = net.addHost('h48', cls=Host, ip='10.0.0.48', defaultRoute=None)
    h61 = net.addHost('h61', cls=Host, ip='10.0.0.61', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h41 = net.addHost('h41', cls=Host, ip='10.0.0.41', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s1, s5)
    net.addLink(s1, s6)
    net.addLink(s1, s7)
    net.addLink(s1, s8)
    net.addLink(s1, s9)
    net.addLink(s2, h1)
    net.addLink(s2, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s2, h5)
    net.addLink(s2, h6)
    net.addLink(s2, h7)
    net.addLink(s2, h8)
    net.addLink(s3, h9)
    net.addLink(s3, h10)
    net.addLink(s3, h11)
    net.addLink(s3, h12)
    net.addLink(s3, h13)
    net.addLink(s3, h14)
    net.addLink(s3, h15)
    net.addLink(s3, h16)
    net.addLink(s4, h17)
    net.addLink(s4, h18)
    net.addLink(s4, h19)
    net.addLink(s4, h20)
    net.addLink(s4, h21)
    net.addLink(s4, h22)
    net.addLink(s4, h23)
    net.addLink(s4, h24)
    net.addLink(s5, h25)
    net.addLink(s5, h26)
    net.addLink(s5, h27)
    net.addLink(s5, h28)
    net.addLink(s5, h29)
    net.addLink(s5, h30)
    net.addLink(s5, h31)
    net.addLink(s5, h32)
    net.addLink(s6, h33)
    net.addLink(s6, h34)
    net.addLink(s6, h35)
    net.addLink(s6, h36)
    net.addLink(s6, h37)
    net.addLink(s6, h38)
    net.addLink(s6, h39)
    net.addLink(s6, h40)
    net.addLink(s7, h41)
    net.addLink(s7, h42)
    net.addLink(s7, h43)
    net.addLink(s7, h44)
    net.addLink(s7, h45)
    net.addLink(s7, h46)
    net.addLink(s7, h47)
    net.addLink(s7, h48)
    net.addLink(s8, h49)
    net.addLink(s8, h50)
    net.addLink(s8, h51)
    net.addLink(s8, h52)
    net.addLink(s8, h53)
    net.addLink(s8, h54)
    net.addLink(s8, h55)
    net.addLink(s8, h56)
    net.addLink(s9, h57)
    net.addLink(s9, h61)
    net.addLink(s9, h62)
    net.addLink(s9, h63)
    net.addLink(s9, h64)
    net.addLink(s9, h58)
    net.addLink(s9, h59)
    net.addLink(s9, h60)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s6').start([c1])
    net.get('s9').start([c1])
    net.get('s1').start([c0,c1])
    net.get('s7').start([c1])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s8').start([c1])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

