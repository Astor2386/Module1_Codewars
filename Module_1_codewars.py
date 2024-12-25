# Solution 1 - Even or Odd
def even_or_odd (n):
    if n % 2 == 0:
        return "Even"
    else:
        return"Odd"
    
# Solution 2 - Convert a Number to a String
def number_to_string(num):
    return str(num)

# Solution 3 - Vowel Count
def getCount(sentence):
    vowels = 'aeiou'
    return sum(1 for char in sentence if char in vowels)