#Teksta analize


def main():
    my_text = input("Ievadiet tekstu: \n")
    print(f"\nSimbolu skaits (bez atstarpēm): {count_characters_without_spaces(my_text)}")
    print(f"Vārdu skaits: {count_words(my_text)}")
    print(f"Teikumu skaits: {count_sentences(my_text)}")
def count_characters_without_spaces(text: str) -> int:
    return len(text.replace(" ", ""))
def count_words(text: str) -> int:
    words = text.split()
    return len(words)
def count_sentences(text: str) -> int:
    sentence_endings = ['.', '!', '?']
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    return count
if __name__ == "__main__":
    main()
