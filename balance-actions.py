#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
import json
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="http node")
parser.add_argument("--url-list", nargs='+',
                    help="http node list (N+1 is a backup node)")
parser.add_argument("--address", help="address to watch for", required=True)
parser.add_argument(
    "--script-path", help="script location (full path)", required=True)
parser.add_argument("--limit", help="balance limit (in wei)",
                    type=int, required=True)
args = parser.parse_args()

NODE_PAYLOAD = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0x" + args.address.replace("0x", ""), "pending"],
    "id": 1
}

http_nodes = []

if (os.path.isfile(args.script_path) is False):
    sys.exit("script %s not found" % args.script_path)
else:
    if (os.access(args.script_path, os.X_OK) is False):
        sys.exit("permission error, cannot execute %s \nplease run 'chmod +x %s' " %
                 (args.script_path, args.script_path))

if (args.url_list):
    if (args.url):
        args.url_list.insert(0, args.url)
    http_nodes = list(set(args.url_list))
else:
    http_nodes.append(args.url)

if (len(http_nodes) == 0):
    sys.exit("Expecting at least 1 http node, found 0")

for i, node in enumerate(http_nodes):
    print("contacting %s" % node)
    node_response = None
    try:
        node_response = requests.post(node, data=json.dumps(NODE_PAYLOAD), headers={
                                      "Content-Type": "application/json"})
    except requests.exceptions.RequestException as e:
        pass

    if (node_response is None or (node_response.status_code is not 200 and node_response.text is not None)):
        print("%s node not available" % node)
    else:
        try:
            account_balance = int(json.loads(node_response.text)["result"], 16)
            break
        except ValueError:
            print("%s node response not valid" % node)

    if (i == len(http_nodes) - 1):
        sys.exit("request error, no nodes available")

print("account balance: %s wei" % account_balance)

if (account_balance < args.limit):
    print("account reached the limit")
    subprocess.call(args.script_path, shell=False)
