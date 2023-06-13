import argparse
import configparser
import json
import os
import requests
from colorama import init, Fore, Style

# Initialize colorama
init()

CONFIG_FILE = os.path.expanduser('~/.spicyscopes')

# ASCII art for SpicyScopes
SPICY_SCOPES_ART = f"""
{Fore.GREEN} SSSSS          iii                 SSSSS                                     
SS      pp pp         cccc yy   yy SS        cccc  oooo  pp pp     eee   sss  
 SSSSS  ppp  pp iii cc     yy   yy  SSSSS  cc     oo  oo ppp  pp ee   e s     
     SS pppppp  iii cc      yyyyyy      SS cc     oo  oo pppppp  eeeee   sss  
 SSSSS  pp      iii  ccccc      yy  SSSSS   ccccc  oooo  pp       eeeee     s 
        pp                  yyyyy                        pp              sss  
{Style.RESET_ALL}
"""

def main():
    print(SPICY_SCOPES_ART)
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Retrieve in-scope domains from HackerOne API.')
    parser.add_argument('--program', dest='program_id', type=str, required=True,
                        help='HackerOne program ID')
    parser.add_argument('--api-key', dest='api_key', type=str,
                        help='HackerOne API key')
    args = parser.parse_args()

    # Load API key from cache if available
    if args.api_key is None:
        cached_api_key = load_api_key()
        if cached_api_key is None:
            print('No API key found. Please provide the --api-key option.')
            return
        args.api_key = cached_api_key
    else:
        # Save the provided API key to cache
        save_api_key(args.api_key)

    # Make a request to HackerOne API
    url = f'https://api.hackerone.com/v1/programs/{args.program_id}/structured_scopes'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {args.api_key}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the in-scope domains
        data = response.json().get('data', [])
        domains = []
        assets = []

        for scope in data:
            attributes = scope['attributes']
            domain = attributes['asset_identifier']
            asset_type = attributes['asset_type']
            confidentiality = attributes['confidentiality_requirement']
            integrity = attributes['integrity_requirement']
            availability = attributes['availability_requirement']
            max_severity = attributes['max_severity']
            eligible_for_bounty = attributes['eligible_for_bounty']
            eligible_for_submission = attributes['eligible_for_submission']

            # Save asset details to JSON
            asset_data = {
                'asset_identifier': domain,
                'asset_type': asset_type,
                'confidentiality_requirement': confidentiality,
                'integrity_requirement': integrity,
                'availability_requirement': availability,
                'max_severity': max_severity,
                'eligible_for_bounty': eligible_for_bounty,
                'eligible_for_submission': eligible_for_submission
            }
            assets.append(asset_data)

            # Save URL domains to TXT
            if asset_type.lower() == 'url':
                domains.append(domain)

        # Save domains to TXT
        if domains:
            txt_file = f'{args.program_id}_{max_severity.lower()}.txt'
            with open(txt_file, 'w') as f:
                f.write('\n'.join(domains))

        # Save asset details to JSON
        json_file = f'{args.program_id}_assets.json'
        with open(json_file, 'w') as f:
            json.dump(assets, f, indent=4)

        print('In-scope domains and asset details saved successfully.')
    else:
        print(f'Failed to retrieve in-scope domains. Status Code: {response.status_code}')


if __name__ == '__main__':
    main()
