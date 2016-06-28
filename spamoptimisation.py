#!/usr/bin/env python3
from itertools import combinations_with_replacement
import json
import argparse

def total_price(combination):
    return sum([float(item["price"]) for item in combination])

def evaluate_combination(desired_price, combination):
    total = total_price(combination)
    return abs(desired_price - total)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--price", type=float, default=30.0)
    parser.add_argument("--menu", type=str, default="spammenu.json")
    parser.add_argument("--item-limit", type=int, default=8)
    args = parser.parse_args()

    desired_price = args.price
    json_file = args.menu
    item_limit = args.item_limit
    with open(json_file) as menu_json:
        menu = json.load(menu_json)

    results = []
    for i in range(1, item_limit + 1):
        for comb in combinations_with_replacement(menu, i):
            results.append(comb)

    results.sort(key=lambda comb: evaluate_combination(desired_price, comb))

    for combination in results[:4]:
        print(total_price(combination))
        items = ",\n".join(["Name: {}, Price: {}".format(item["name"], item["price"]) for item in combination])
        print(items)
        print("\n")

if __name__ == '__main__':
    main()
