
def read_in_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def main():
    print(read_in_content())


main()

