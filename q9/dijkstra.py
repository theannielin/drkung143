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
delayFile = csv.DictReader(open(delayFile))
switches = {
    'g': ('s11', 's12'),
    'h': ('s12', 's14'),
    'i': ('s14', 's16'),
    'j': ('s16', 's18'),
    'k': ('s11', 's18'),
    'l': ('s12', 's18'),
    'm': ('s12', 's16'),
    'n': ('s14', 's18'),
}


class Dijkstra (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Dijkstra Module")
        ''' self.thelist =  []
        for row in delayFile:
            link = row["link"]
            delay = row["delay"]
            self.thelist.append((link, delay))
            self.switches = (s11, s12, s14, s16, s18)
            self.hosts = (h13, h15, h17, h19)
            self.distances = {} '''

    # http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
    def _dijkstra(self, source):
        dist = {source: 0}
        prev = defaultdict(None)
        Q = set()
        for switch in switches:
            if switch != source:
                dist[switch]  = float("inf")
                prev[switch]  = None
            Q.add(switch)
        while Q != set():
            u = switch in Q with min dist[u]
            remove u from Q
            for each neighbor v of u:
                alt := dist[u] + length(u, v)
                if alt < dist[v]:
                    dist[v]  := alt
                    previous[v]  := u
        return dist, previous


    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''


        
        log.debug("Dijkstra installed on %s", dpidToStr(event.dpid))        

def launch ():
    '''
    Starting the Dijkstra module
    '''
    core.registerNew(Dijkstra)
