from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Add switches
        switchL1 = self.addSwitch('sL1', dpid='1')
        switchL2 = self.addSwitch('sL2', dpid='2')
        switchL3 = self.addSwitch('sL3', dpid='3')

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')

        # Connect Switches
        self.addLink(switchL1, switchL2)
        self.addLink(switchL3, switchL2)
        self.addLink(switchL1, switchL3)

        # Connect Hosts
        self.addLink(host1, switchL1)
        self.addLink(host2, switchL2)
        self.addLink(host3, switchL3)
        self.addLink(host4, switchL3)
        self.addLink(host5, switchL2)
        self.addLink(host6, switchL1)


topos = {'mytopo': (lambda: MyTopo())}
