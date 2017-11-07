## https://www.hackerrank.com/challenges/bon-appetit/problem


def find_charge_message(orders_qty, order_avoided_by_anna, charges, value_brian_charged):
    assert order_avoided_by_anna < orders_qty, 'Anna avoided order not in correct range'
    assert orders_qty == len(charges), 'Orders quantity must match charges quantity'
    orders_sum = sum(charges)
    anna_charge_fair_value = (orders_sum - charges[order_avoided_by_anna]) // 2
    return 'Bon Appetit' if value_brian_charged <= anna_charge_fair_value else value_brian_charged - anna_charge_fair_value


def main():
    first_line = input().strip().split(' ')
    orders_qty = int(first_line[0])
    order_avoided_by_anna = int(first_line[1])
    charges = list(map(int, input().strip().split(' ')))
    value_brian_charged = int(input().strip())
    print(find_charge_message(orders_qty, order_avoided_by_anna, charges, value_brian_charged))


main()
