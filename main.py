
def read_in_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_characters(book_string):
    book_string_lower = book_string.lower()
    print(book_string_lower)
    
    return 

def main():
    words = read_in_content()
    words_count = read_in_content().split()
    count = 0 
    count_characters(words)
    for word in words_count:
        count += 1
    print(count)

main()

