t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():

    if "а" <= s <= "я":
        slug += t[ord(s) - ord('а')]
    # elif s == "ё":
        # slug = 'yo'
    # elif s in " !?;:.,":
        # slug = "-"
    else:
        slug += s

# while slug.count('--'):
# slug = slug.replace('--', '-')

print(slug)