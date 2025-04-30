#!/usr/bin/python3

import crossdb
import click
from tabulate import tabulate

conn = crossdb.connect(port=7777)
cursor = conn.cursor()

@click.group()
def interface():
	"""Show details of the network interfaces"""
	pass

@interface.group()
@click.pass_context
def ip(ctx):
	"""Set IP interface attributes"""
	pass

@ip.command('add')
@click.argument('interface_name', metavar='<interface_name>', required=True)
@click.argument("ip_addr", metavar="<ip_addr>", required=True)
@click.argument('gw', metavar='<default gateway IP address>', required=False)
@click.option('--secondary', "-s", is_flag=True, default=False)
def add_interface_ip(interface_name, ip_addr, gw, secondary):
	"""Add an IP address towards the interface"""
	print ("config add ip", interface_name, ip_addr)
	sql = f"INSERT INTO config.intf (ifname, ipaddr) VALUES ('{interface_name}', '{ip_addr}')"
	err = cursor.execute(sql)
	if cursor.affected_rows != 1:
		print ("failed to insert ", err)

if __name__ == "__main__":
	interface()
