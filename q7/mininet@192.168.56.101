from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
		c1 = self.addSwitch(’c1’)
		lastSwitch = None
		lastHost = None
		self.fanout = fanout
		parameters = dict(bw=10, delay=’5ms’, loss=10, max_queue_size=1000, use_htb =True)
		ecount = 1
		hcount = 1
		for a in arange(1, fanout):
        	aggswitch = self.addSwitch(’a%s’ % a)
        	self.addLink( c1, aggswitch, **parameters)
        	for e in erange (1, fanout)
	        	edgeswitch = self.addSwitch(’ecount%s’ % ecount)
	        	ecount += 1
	        	self.addLink(aggswitch, edgeswitch, **parameters)
        		for h in hrange (1, fanout)
		        	host = self.addHost(’hcount%s’ % hcount)
		        	hcount += 1
		        	self.addLink(edgeswitch, host, **parameters)     

        
linkopts1 = dict(bw=10, delay=’5ms’, loss=10, max_queue_size=1000, use_htb =True)
linkopts2 = dict(bw=10, delay=’5ms’, loss=10, max_queue_size=1000, use_htb =True)
linkopts3 = dict(bw=10, delay=’5ms’, loss=10, max_queue_size=1000, use_htb =True)
                    
topos = { 'custom': ( lambda: CustomTopo(linkopts1,linkopts2,linkopts3)) }