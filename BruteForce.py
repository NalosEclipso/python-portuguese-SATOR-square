from verification import SATOR

with open("Dic/h.txt", "r", encoding="utf-8") as f:
    h_words = [line.strip() for line in f]

with open("Dic/p.txt", "r", encoding="utf-8") as f:
    p_words = [line.strip() for line in f]

solution = []
for h1 in h_words:
    for h2 in h_words:
      for p in p_words:
        if SATOR(h1, h2, p):
          solution.append([h1,h2,p])
            
print("Total solutions:", len(solution))
print(solution)
