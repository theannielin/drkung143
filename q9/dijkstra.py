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
        self.thelist =  {}
        for row in delayFile:
            link = row["link"]
            delay = row["delay"]
            self.thelist['link'] = delay

    # from http://geekly-yours.blogspot.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
    def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
        """ calculates a shortest path tree routed in src
        """    
        # a few sanity checks
        if src not in graph:
            raise TypeError('the root of the shortest path tree cannot be found in the graph')
        if dest not in graph:
            raise TypeError('the target of the shortest path cannot be found in the graph')    
        # ending condition
        if src == dest:
            # We build the shortest path and display it
            path=[]
            pred=dest
            while pred != None:
                path.append(pred)
                pred=predecessors.get(pred,None)
            return path
        else :     
            # if it is the initial  run, initializes the cost
            if not visited: 
                distances[src]=0
            # visit the neighbors
            for neighbor in graph[src] :
                if neighbor not in visited:
                    new_distance = distances[src] + graph[src][neighbor]
                    if new_distance < distances.get(neighbor,float('inf')):
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = src
            # mark as visited
            visited.append(src)
            # now that all neighbors have been visited: recurse                         
            # select the non visited node with lowest distance 'x'
            # run Dijskstra with src='x'
            unvisited={}
            for k in graph:
                if k not in visited:
                    unvisited[k] = distances.get(k,float('inf'))        
            x=min(unvisited, key=unvisited.get)
            dijkstra(graph,x,dest,visited,distances,predecessors)


    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        # make a graph with all of the switches and their delay values
        graph = {'s11': {'s12': self.thelist["g"] , 's18': self.thelist["k"]},
            's12': {'h13': 1, 's14': self.thelist["h"] , 's16': self.thelist["m"] , 's18': self.thelist["l"]},
            's14': {'h15': 1, 's12': self.thelist["h"] , 's18': self.thelist["n"] , 's16': self.thelist["i"]},
            's16': {'h17': 1, 's12': self.thelist["m"] , 's14': self.thelist["i"] , 's18': self.thelist["j"]},
            's18': {'h19': 1, 's12': self.thelist["l"] , 's16': self.thelist["j"] , 's14': self.thelist["n"]},
            'h13': {'s12': 0},
            'h15': {'s14': 0},
            'h17': {'s16': 0},
            'h19': {'s18': 0},
            }

        # for every node, make a flow table
        for node1 in graph.keys():
            for node in graph.keys():
                path = dijkstra(graph, node1, node2)
                # for every node in our path, create the flow to the next node in the path
                for link1 in path:
                    link2 = link1+1
                    for link2 in path:
                        fm = of.ofp_flow_mod()
                        fm.match.in_port = link1
                        fm.actions.append(of.ofp_action_output(port = link2))
        
        log.debug("Dijkstra installed on %s", dpidToStr(event.dpid))        

def launch ():
    '''
    Starting the Dijkstra module
    '''
    core.registerNew(Dijkstra)
