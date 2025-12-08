def encode_rle(s):
    if not s: return ''
    result, count = '', 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1
    return result + str(count) + s[-1]

def decode_rle(encoded):
    result, i, count = '', 0, ''
    while i < len(encoded):
        if encoded[i].isdigit():
            count += encoded[i]
        else:
            result += encoded[i] * int(count or 1)
            count = ''
        i += 1
    return result


levels = [
    ("AAAABBBCCD", "4A3B2C1D"),
    ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB", "12W1B12W3B24W1B")
]
score = 0
for lvl, target in levels:
    print(f"\nLevel: {lvl}")
    user_enc = input("Encode (or press Enter for auto): ").strip()
    if not user_enc: user_enc = encode_rle(lvl)
    decoded = decode_rle(user_enc)
    compression = (1 - len(user_enc)/len(lvl)) * 100
    if decoded == lvl:
        pts = min(100, 100 - (len(user_enc) - len(target)) * 10)
        score += pts
        print(f"Correct! Compression: {compression:.1f}% | Points: {pts}")
    else:
        print(f"Wrong. Original: {lvl}, Yours decoded to: {decoded}")
print(f"\nFinal Score: {score}/200. Great job!")

