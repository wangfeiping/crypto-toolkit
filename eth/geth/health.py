#/usr/bin/env python

from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

if not w3.isConnected():
  print("geth is not connect")
