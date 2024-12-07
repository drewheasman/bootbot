def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    characters = {}
    for char in text:
        char = char.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def report(book_name: str, word_count: int, character_counts: dict[str, int]) -> None:
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in character_counts:
        print(f"The '{char}' character was found {character_counts[char]} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)
    report(book_path, word_count, character_counts)

main()
