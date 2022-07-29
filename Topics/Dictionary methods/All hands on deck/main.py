dict_deck = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
total = 0
total_cards = 6
i = 1
while i <= total_cards:
    a = input()
    try:
        a = int(a)
    except Exception:
        total += dict_deck.get(a)
    else:
        total += a
    i += 1
print(total / total_cards)
