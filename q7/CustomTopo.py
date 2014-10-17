
from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        c1 = self.addSwitch('c1')
        lastSwitch = None
        lastHost = None
        self.fanout = fanout
        ecount = 1
        hcount = 1
        for a in range(1, fanout+1):
                aggswitch = self.addSwitch('a%s' % a)
                self.addLink(aggswitch, c1,  **linkopts1)
                for e in range (1, fanout+1):
                        edgeswitch = self.addSwitch('e%s' % ecount)
                        ecount += 1
                        self.addLink(edgeswitch, aggswitch,  **linkopts2)
                        for h in range (1, fanout+1):
                                host = self.addHost('h%s' % hcount)
                                hcount += 1
                                self.addLink(host, edgeswitch, **linkopts3)

linkopts1 = dict(bw=10, delay='5ms',  max_queue_size=1000, use_htb =True)
linkopts2 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb =True)
linkopts3 = dict(bw=10, delay='5ms',  max_queue_size=1000, use_htb =True)

topos = { 'custom': ( lambda: CustomTopo(linkopts1,linkopts2,linkopts3)) }