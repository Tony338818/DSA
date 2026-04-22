"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a 
total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

# DYNAMIC PROGRAMMING


def coin_change(amount, coins):
    combinations = 0
    
    for i in range(len(coins)):
        if amount == coins[i]:
            combinations += 1
        if (amount % coins[i]) in coins or (amount % coins[i]) == 0:
            combinations += 1
            
    return combinations

def coin_change_proper(amount, coins):
    combinations = []
    
    for i in range(len(coins)):
        if amount == coins[i]:
            combinations += 1
            print(f'Coin {coins[i]} = {amount}')
        
        


amount = 5
coins = [1, 2, 5]
print(coin_change_proper(amount, coins))  