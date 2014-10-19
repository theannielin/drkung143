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
delayFile = "delay.csv"

''' Add your global variables here ... '''



class Dijkstra (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Dijkstra Module")


        ''' lols wtf? maybe??? ... '''
        self.thelist =  []
        for row in delayFile:
            link = row["link"]
            delay = row["delay"]
            self.thelist.append(Link(link), Delay(delay))
        ''' end of random stuff '''

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        
        log.debug("Dijkstra installed on %s", dpidToStr(event.dpid))        

def launch ():
    '''
    Starting the Dijkstra module
    '''
    core.registerNew(Dijkstra)
