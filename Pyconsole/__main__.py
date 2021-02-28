#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import Civ4Shell

import argparse

try:
    from ports_local import PORT_MAPS
except:
    PORT_MAPS = {
        "PB1": 3333,
    }


parser = argparse.ArgumentParser(description='Commandline interface to Civ4 games with pyconsole support.')
parser.add_argument('-q', '--quiet', action='store_true', 
                    help='Print retured text from game only.')
#parser.add_argument('-p', '--port', type=int, default=Civ4Shell.PYCONSOLE_PORT,
#                    help="Port of Civ4's Pyconsole backend.")
parser.add_argument('-x', '--host', type=str, default=Civ4Shell.PYCONSOLE_HOSTNAME,
                    help='Hostname')
parser.add_argument('game', help="PORT or GAME NAME. Default port of backend is {port}.".format(port=Civ4Shell.PYCONSOLE_PORT))


args = parser.parse_args()

if args.quiet:
    Civ4Shell.QUIET = True

# Translate game name into port
if args.game in PORT_MAPS:
    port = PORT_MAPS[args.game]
else:
    port = args.game

port = int(port)
Civ4Shell.start(port=port, host=args.host)

