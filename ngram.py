def find_max_ngram(text: str, length: int) -> str:
    ngrams = {}
    for i in range(len(text) - length+1):
        ngram = text[i:i + length]
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1
    max_ngram = max(ngrams, key=ngrams.get)

    return max_ngram


if __name__ == '__main__':
    input_str = input("Input: ")
    text, length = input_str.split(",")
    length = int(length)
    print(find_max_ngram(text, length))
