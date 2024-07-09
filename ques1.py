def number_to_words(n):
    if n == 1000:
        return "one thousand"
    words = ""

    if n >= 100:
        words += ones[n // 100] + " hundred"
        n %= 100
        if n > 0:
            words += " and "

    if n >= 20:
        words += tens[n // 10]
        n %= 10
        if n > 0:
            words += " " + ones[n]
    elif n >= 10:
        if n == 10:
            words += tens[1]
        else:
            words += teens[n % 10]
    else:
        words += ones[n]
    return words


def count_letters(words):
    return len(words.replace(" ", "").replace("-", ""))


ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = [
    "",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

total_letters = 0
for i in range(1, 11):
    words = number_to_words(i)
    total_letters += count_letters(words)
print(total_letters)
