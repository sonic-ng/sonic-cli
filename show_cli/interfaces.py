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

@click.group()
def interfaces():
	"""Show details of the network interfaces"""
	pass

@interfaces.command()
@click.argument('interfacename', required=False)
@click.option('--verbose', is_flag=True, help="Enable verbose output")
def description(interfacename, verbose):
	"""Show interface status, protocol and description"""

	cursor.execute("SELECT ifname,oper_status,admin_status,alias,description FROM appl.port ORDER BY ifname")
	data = cursor.fetchall ()
	bool2updown(data, 1)
	bool2updown(data, 2)
	header = ['Interface', 'Oper', 'Admin', 'Alias', 'Description']
	click.echo(tabulate(data, header))

if __name__ == "__main__":
	interfaces()
