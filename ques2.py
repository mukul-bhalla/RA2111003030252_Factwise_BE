def maxScore(cards, k):
    size = len(cards)
    if k > size:
        print("Cards required are more than available cards")
        return
    if k == size:
        return sum(cards)

    total_points = sum(cards)
    subarray_len = size - k

    curr_subarray_sum = sum(cards[:subarray_len])
    min_subarray_sum = curr_subarray_sum

    for i in range(subarray_len, size):
        curr_subarray_sum += cards[i] - cards[i - subarray_len]
        min_subarray_sum = min(min_subarray_sum, curr_subarray_sum)
    return total_points - min_subarray_sum


n = int(input("Enter total number of cards: "))
cards = []
for i in range(n):
    x = int(input("Enter Card Score: "))
    cards.append(x)
k = int(input("Enter Minimum cards to be taken: "))
ans = maxScore(cards, k)
print(ans)
