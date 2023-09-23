def stringSort(text):
    words = text.split(" ")

    storage = []

    for word in (words):
        storage.append((word, word.lower()))

    storage.sort(key=lambda x: x[1])

    sorted_words = []

    for word in (storage):
        sorted_words.append(word[0])

    sorted_text = " ".join(sorted_words)

    return sorted_text


sentence = input()

print(stringSort(sentence))