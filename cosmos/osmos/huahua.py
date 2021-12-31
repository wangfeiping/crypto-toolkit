#!/usr/bin/env python3
#
# view osmos wallet and huahua price
#

import json
import requests


wallet = "XXXXX"

r = requests.get("https://lcd-osmosis.keplr.app/bank/balances/" + wallet)
print("# Osmos Wallet #")
obj = r.json()["result"]
pretty = json.dumps(obj, indent=2)
# print(pretty)
atom_balance = 0
huahua_balance = 0
for i in obj:
    if i["denom"] == "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2":
        atom_balance = float(i["amount"]) / 10**6
    if i["denom"] == "ibc/B9E0A1A524E98BB407D3CED8720EFEFD186002F90C1B1B7964811DD0CCC12228":
        huahua_balance = float(i["amount"]) / 10**6
print("atom_balance:", atom_balance)
print("huahua_balance:", huahua_balance)


r = requests.get("https://lcd-osmosis.keplr.app/osmosis/gamm/v1beta1/pools/606")
print("# Huahua/Atom #")
obj = r.json()["pool"]["poolAssets"]
pretty = json.dumps(obj, indent=2)
# print(pretty)

atom_total = 0
huahua_total = 0
for i in obj:
    if i["token"]["denom"] == "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2":
        atom_total = i["token"]["amount"]
    if i["token"]["denom"] == "ibc/B9E0A1A524E98BB407D3CED8720EFEFD186002F90C1B1B7964811DD0CCC12228":
        huahua_total = i["token"]["amount"]

# print("atom_total:", atom_total)
# print("huahua_total:", huahua_total)
print("huahua/atom:", float(huahua_total)/float(atom_total))
