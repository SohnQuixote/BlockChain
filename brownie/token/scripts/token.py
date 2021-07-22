#!/usr/bin/python3

from brownie import Token, accounts


def main():
    return Token.deploy("Test Token", "TST", 18, 4e21, {'from': accounts[0]})

def distribute_tokens(sender=accounts[0], receiver_list=accounts[1:]):
    token = main()
    for receiver in receiver_list:
        token.transfer(receiver, 1e18, {'from': sender})

