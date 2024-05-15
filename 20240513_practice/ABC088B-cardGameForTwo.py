def calcurate_card_game(N, cards):
    cards.sort(reverse=True)

    alice_score = 0
    bob_score = 0

    for i in range(N):
        if i % 2 ==0:
            alice_score += cards[i]
        else:
            bob_score += cards[i]

    return alice_score - bob_score

N = int(input())
cards = list(map(int, input().split()))

print(calcurate_card_game(N, cards))