'''
main, quick script
'''
import os
import time
import sys
import requests
from dotenv import load_dotenv

def main():
    '''
    main
    '''
    time_interval = None
    try:
        time_interval = int(input("Please specify how often in seconds you'd like to make a request for the prices (it must be more than 10): "))
        if int(time_interval) < 10:
            print("time was less than 10s", file=sys.stderr)
            return 1
    except ValueError:
        print("input time was not an integer", file=sys.stderr)
        return 1

    load_dotenv()
    api_key = os.getenv("API_KEY")
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

    # one table
    while True:
        print("\ncoin name,USD,AUD")
        for k, v in cryptonames_to_id.items():
            response = requests.get(api_url, params={
                'ids': v,
                'vs_currencies': 'usd,aud',
                'x_cg_demo_api_key': api_key
            },timeout=10)

            if response.status_code == 200:
                coin_data = response.json()[cryptonames_to_id[k]]
                print(f"{k},{coin_data['usd']},{coin_data['aud']}")
        
        time.sleep(time_interval)
       

if __name__ == "__main__":
    main()
