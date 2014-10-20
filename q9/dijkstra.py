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



class Dijkstra (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Dijkstra Module")
        self.thelist =  []
        for row in delayFile:
            link = row["link"]
            delay = row["delay"]
            self.thelist.append((link, delay))
            self.switches = (s11, s12, s14, s16, s18)
            self.hosts = (h13, h15, h17, h19)
            self.distances = {}


    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        visited = {initial: 0}
        path = {}
        nodes = set(self.switches)

        while nodes: 
        min_node = None
        for node in nodes:
          if node in visited:
            if min_node is None:
              min_node = node
            elif visited[node] < visited[min_node]:
              min_node = node

        nodes.remove(min_node)
        current_weight = visited[min_node]

        #from h13 to h15
        for link in self.thelist[min_node]:
          weight = current_weight + self.distance[(min_node, link)]
          if link not in visited or weight < visited[link]:
            visited[link] = weight
            path[link] = min_node

(node1, node2) = self.dict[link] 
fm = of.ofp_flow_mod()
fm.match.in_port = node1
fm.actions.append(of.ofp_action_output(node2))



        
        log.debug("Dijkstra installed on %s", dpidToStr(event.dpid))        

def launch ():
    '''
    Starting the Dijkstra module
    '''
    core.registerNew(Dijkstra)
