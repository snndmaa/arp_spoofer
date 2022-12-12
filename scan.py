#!/usr/bin/env python3
import nmap

# perform a network scan with nmap
def scanNetwork(network):
    returnlist = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, arguments='-sn')

    for k, v in a['scan'].items():
        if str(v['status']['state']) == 'up':
            try:
                returnlist.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
            except:
                pass

    return returnlist
