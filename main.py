
def read_in_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def main():
    words_count = read_in_content().split()
    count = 0 
    for word in words_count:
        count += 1
    print(count)

main()

