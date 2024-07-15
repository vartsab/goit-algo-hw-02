from collections import deque

def is_palindrome(s):
    # Trim the string S from spaces and convert to lower case
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Create a double-ended queue
    char_deque = deque(s)

    # ompare symbols from both sides of the queue
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Приклади використання
print(is_palindrome("Три психи пили Пилипихи спирт"))   # True
print(is_palindrome("О-к о"))                           # True
print(is_palindrome("Рак літеральний єсть вірш, которого літери, і вспак читаючися, той же текст виражають"))                           # False
