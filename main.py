# something something

def print_report(book_path: str, no_of_words: int, total_letter_dict: dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{no_of_words} words found in the document")

    #convert dict to list of dict
    sorted_list = []

    for letter in total_letter_dict:
        sorted_list.append({"letter":letter, "num":total_letter_dict[letter]})

    sorted_list.sort(reverse=True, key=lambda dict:dict["num"])

    for entry in sorted_list:
        print(f"The '{entry["letter"]}' character was found {entry["num"]} times")



    print("--- End report ---")

def count_characters(input_string: str):
    lowered_input_string = input_string.lower()
    counter_dict = {}

    for letter in lowered_input_string:
        if letter not in counter_dict:
            counter_dict.update({letter : 1})
        else:
            counter_dict[letter] += 1

    return counter_dict



def count_words(input_string: str):
    print(len(input_string.split()))

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print_report(book_path, count_words(file_contents), count_characters(file_contents))

main()