'''
main, quick script
'''
from collections import defaultdict
import csv
import json
import requests
import sys

COLUMN_NAME = "cryptoname"
CSV_FILE = "cryptos.csv"
COIN_IDS_FILE = "coin-ids.json"

def main():
    '''
    main
    '''
    cryptonames_to_id = {
        'Polygon': 'matic-network',
        'Wrapped ETC': 'wrapped-ether',
        'MATIC': 'matic-network',
        'USDC': 'usd-coin',
        'Uniswap': 'uniswap',
        'Wrapped Bitcoin': 'wrapped-bitcoin',
        'Chainlink': 'chainlink',
        'Decentraland': 'decentraland',
        'The Graph': 'the-graph',
        'Ankr Network': 'ankr',
        'Tether': 'tether',
        'Aave': 'aave',
        'Avalanche': 'avalanche-2',
        'Cosmos Hub': 'cosmos',
        'Synthetic Network': 'havven',
        'The Sandbox': 'the-sandbox',
        'Render': 'render-token',
        'Compound': 'compound-governance-token',
        '1inch': '1inch',
        'Mask Network': 'mask-network',
        'Axelar': 'axelar',
        'Solana': 'solana',
    }
    # make the request for prices
    api_url = "https://api.coingecko.com/api/v3/simple/price" 
    print("coin name,USD,AUD")
    for k, v in cryptonames_to_id.items():
        response = requests.get(api_url, params={
            'ids': v,
            'vs_currencies': 'usd,aud',
            'x_cg_demo_api_key': 'CG-k4oruRoXPPc6QrdifkDF8Hkq'
        },timeout=10)

        if response.status_code == 200:
            coin_data = response.json()[cryptonames_to_id[k]]
            print(f"{k},{coin_data['usd']},{coin_data['aud']}")
            # print(f"usd: :{coin_data[k]['usd']}", end=", ")
            # print(f"aud: :{coin_data[k]['aud']}")


# curl -G \
#      --url "https://api.coingecko.com/api/v3/simple/price" \
#      --data-urlencode "ids=matic-network" \
#      --data-urlencode "vs_currencies=usd,aud" \
#      --data-urlencode "x_cg_demo_api_key=CG-k4oruRoXPPc6QrdifkDF8Hkq" \
#      --header 'accept: application/json'


if __name__ == "__main__":
    main()