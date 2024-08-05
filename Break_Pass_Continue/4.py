sample_words = ["hello", "world", "python", "is", "awesome"]
n = 4
long_words = []

for word in sample_words:
    if len(word) > n:
        long_words.append(word)

print("Words longer than", n, "characters:", long_words)
