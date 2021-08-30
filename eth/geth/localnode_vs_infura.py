#/usr/bin/env python

#
# requires your to be set the environment variable before running
#
# Infura Project ID:
#
#     export WEB3_INFURA_PROJECT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
# Ding Bot Access Token:
#
#     export DING_BOT_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#

from web3 import Web3

infura_project_id = os.getenv("WEB3_INFURA_PROJECT_ID")

infura_w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + infura_project_id))
localnode_w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

if not infura_w3.isConnected():
  print("[eth] [infura] geth is not available")
  os.exit(1)
  
if not localnode_w3.isConnected():
  print("[eth] [local node] geth is not available")
  os.exit(2)
  
if infura_w3.eth.block_number != localnode_w3.eth.block_number:
  print("w3.eth.block_number conflict")
  os.exit(3)
  
if infura_w3.eth.chain_id != localnode_w3.eth.chain_id:
  print("w3.eth.chain_id conflict")
  os.exit(4)
  
if infura_w3.eth.protocol_version != localnode_w3.eth.protocol_version:
  print("w3.eth.protocol_version conflict")
  os.exit(4)
  
print("Local Node: ", localnode_w3.clientVersion)
print("infura: ", infura_w3.clientVersion)

print("Everything is fine")
