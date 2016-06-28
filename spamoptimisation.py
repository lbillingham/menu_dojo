#!/usr/bin/env python3
from itertools import combinations_with_replacement
import json

def total_price(combination):
    return sum([float(item["price"]) for item in combination])

def evaluate_combination(desired_price, combination):
    total = total_price(combination)
    return abs(desired_price - total)

def main():
    desired_price = 12.5
    json_file = "spammenu.json"
    with open(json_file) as menu_json:
        menu = json.load(menu_json)

    results = []
    n = 1
    for i in range(100):
        combinations = list(combinations_with_replacement(menu, n))
        for comb in combinations:
            results.append(comb)

    results.sort(key=lambda comb: evaluate_combination(desired_price, comb))

    for combination in results[:10]:
        print(total_price(combination))
        print(combination)

if __name__ == '__main__':
    main()
