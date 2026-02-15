with open("br-sem-acentos.txt", "r", encoding="utf-8") as f:
    all = [line.strip() for line in f]
five = [word for word in all if len(word) == 5]
with open("pt5letters.txt", "w", encoding="utf-8") as out:
    for word in five:
        out.write(word + "\n")

print(f"Total number of 5 letter words: {len(five)}")
