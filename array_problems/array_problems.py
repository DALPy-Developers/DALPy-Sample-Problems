from dalpy.arrays import Array


# ************************** DO NOT MODIFY ABOVE THIS LINE ******************************

def count_prizes(prizes, items):
    table = Array(52)
    for i in range(52):
        table[i] = False
    ascii_a = ord('a')
    ascii_z = ord('z')
    ascii_capital_a = ord('A')
    for i in range(prizes.length()):
        ascii_prize = ord(prizes[i])
        if ascii_a <= ascii_prize <= ascii_z:
            table[ascii_prize - ascii_a] = True
        else:
            table[26 + (ascii_prize - ascii_capital_a)] = True
    prize_count = 0
    for i in range(items.length()):
        ascii_item = ord(items[i])
        if ascii_a <= ascii_item <= ascii_z:
            lookup = ascii_item - ascii_a
        else:
            lookup = 26 + ascii_item - ascii_capital_a
        if table[lookup]:
            prize_count += 1
    return prize_count
    
            
        
