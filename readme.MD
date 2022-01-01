# Simple affiliate smart contract with Solidity
You must set up an .env file in the base directory (affiliate_brownie) for this to work.
example .env file:
```
PRIVATE_KEY=your_private_key
WEB3_INFURA_PROJECT_ID=infura_project_id
ETHERSCAN_TOKEN=etherscan_api_token
```
Make sure that the Infura project id is set to the used network as seen below.
![Infura example](https://i.hizliresim.com/5c5sb8z.PNG)

Suggested to deploy this on a test network (preferably Kovan as seen in the following command)
Make sure you have enough Kovan ETH in your wallet.
Command to deploy: ```brownie run scripts/deploy_affiliate.py --network kovan```


