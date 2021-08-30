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

from web3.auto.infura import w3

if not w3.isConnected():
  # send msg to dingding
  print("[eth] [local node] geth is not available")
