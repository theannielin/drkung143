from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os

''' Add your imports here ... '''
import csv



log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''
input_file = csv.DictReader(open("policyFile"))




class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")
        self.thelist =  []
        for row in input_file:
            mac_0 = row["mac_0"]
            mac_1 = row["mac_1"]
            self.thelist.append(EthAddr(mac_0), EthAddr(mac_1))

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        ''' TODO: Add more stuff '''
        
        

    
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
