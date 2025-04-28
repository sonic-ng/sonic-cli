#!/usr/bin/python3

import crossdb
import click
from tabulate import tabulate

conn = crossdb.connect(port=7777)
cursor = conn.cursor()

def bool2updown(data, idx):
	for ele in data:
		if ele[idx]:
			ele[idx] = 'up'
		else:
			ele[idx] = 'down'

def bool2updown(data, idx):
	for ele in data:
		if ele[idx]:
			ele[idx] = 'up'
		else:
			ele[idx] = 'down'

#
# 'ip' group ("show ip ...")
#

# This group houses IP (i.e., IPv4) commands and subgroups
@click.group()
def ip():
    """Show IP (IPv4) commands"""
    pass

#
# 'show ip interfaces' command
#
# Display all interfaces with master, an IPv4 address, admin/oper states, their BGP neighbor name and peer ip.
# Addresses from all scopes are included. Interfaces with no addresses are
# excluded.
#

@ip.group(invoke_without_command=True)
def interfaces():
	#cursor.execute("SELECT ifname,oper_status,admin_status,alias,description FROM appl.port ORDER BY ifname")
	#data = cursor.fetchall ()
	#header = ['Interface', 'Master', 'IPv4 address/mask', 'Admin/Oper', 'BGP Neighbor', 'Neighbor IP']
	header = ['Interface', 'IPv4 address/mask']
	cursor.execute("SELECT ifname,ipaddr FROM appl.intf ORDER BY ifname,ipaddr")
	data = cursor.fetchall ()
	click.echo(tabulate(data, header))

if __name__ == "__main__":
	ip()
