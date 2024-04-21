text = 'CRAFTCODECLUB'

chars = [0]*26


for c in text:
    index = ord(c) - ord('A')
    chars[index] += 1

index = None
max_freq = 0
for i in range(26):
    if chars[i] > max_freq:
        max_freq = chars[i]
        index = i

print(f'The most frequent character is {chr(index + ord("A"))} with frequency {max_freq}')