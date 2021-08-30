#/usr/bin/env python

#
# requires your to be set the environment variable before running
#
# Ding Bot Access Token:
#
#     export DING_BOT_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#

from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

if not w3.isConnected():
  # send msg to dingding
  print("[eth] [local node] geth is not available")
