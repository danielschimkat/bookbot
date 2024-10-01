
def text_out(data):
    print(data)

def word_count(data):
    number_of_words = 0
    #split data to get number of words
    lines = data.split()
    #add word to word count
    number_of_words += len(lines)
    print(number_of_words)
    return number_of_words

def count_characters(data):
    count = {}
    lowered_text = data.lower()
    getVals = list([val for val in lowered_text if val.isalpha()])
    lowered_text ="".join(getVals)
    for c in lowered_text:
        count[c] = count.setdefault(c,0)+1
    return count

def report_builder(count, number_of_words):
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    print(f'{number_of_words} words found in the document \n \n')
    for i,j in count.items():
        print(f"The '{i}' character was found {j} times")


def main():
    with open(r'./books/frankenstein.txt', 'r') as file:
        data = file.read()
        text_out(data)
        number_of_words = word_count(data)
        count = count_characters(data)
        report_builder(count, number_of_words)


if __name__ == "__main__":
    main()