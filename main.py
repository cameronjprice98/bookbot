
def read_in_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_characters(book_string):
    total_characters ={}
    book_string_lower = book_string.lower()
    each_character = list(book_string_lower)
    for char in each_character:
        if char not in total_characters:
            total_characters.update({char : 1})
        else:
            count = total_characters[char]
            count += 1 
            total_characters.update({char : count})
    return total_characters


def alphabet_count(alpha):
    sorted_count = dict(sorted(alpha.items(), key=lambda item: item[1], reverse=True))
    for sort in sorted_count:
        if sort.isalpha():
            print(f"the '{sort}' character was found {alpha[sort]} times")
    
    return

def main():
    words = read_in_content()
    words_count = words.split()
    count = 0 
    character_count = count_characters(words)
    for word in words_count:
        count += 1
    print(f"{count} words found in the document")
    report = alphabet_count(character_count)
main()
