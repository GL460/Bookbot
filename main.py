def main():
    book_path = "/home/gl460/workspace/github.com/GL460/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    book = "frankenstein"

    #This marks the start of the book report now variables have been defined above. 
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    character_counts = get_char_count(text)
   

    for char in sorted(character_counts, key=character_counts.get, reverse=True):
        print(f"The '{char}' character was found {character_counts[char]} times")

    print("--- End Report ---") 


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lower = text.lower()
    char_count = {}

    for char in lower:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

main()
