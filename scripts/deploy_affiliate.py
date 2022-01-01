from brownie import network, accounts, config, Affiliate

def main():
    acct = accounts.add(config["wallets"]["from_key"])
    Affiliate.deploy({'from': acct}, publish_source=True)
