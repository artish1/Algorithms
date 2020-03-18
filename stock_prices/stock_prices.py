#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = 0
    first_pass = False  # Used to set an initial max profit at the beginning, incase of negative profits at first iteration
    for i in range(0, len(prices)):
        current_bought_price = prices[i]
        for n in range(i + 1, len(prices)):
            profit = prices[n] - current_bought_price
            if not first_pass:
                max_profit = profit
                first_pass = True
            else:
                if profit > max_profit:
                    max_profit = profit
    return max_profit


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

