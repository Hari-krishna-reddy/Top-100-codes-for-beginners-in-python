def number_to_words(n):
    # Basic words for numbers
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    if n == 0:
        return "Zero"

    def wordify(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        elif num < 1000:
            return ones[num // 100] + " Hundred" + (" " + wordify(num % 100) if num % 100 != 0 else "")

    result = ""
    i = 0

    while n > 0:
        if n % 1000 != 0:
            result = wordify(n % 1000) + " " + thousands[i] + (", " if result else "") + result
        n //= 1000
        i += 1

    return result.strip(", ")

# Example usage:
number = 1234567890
print(number_to_words(number))
