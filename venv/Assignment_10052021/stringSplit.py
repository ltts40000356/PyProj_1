def split_and_join(line):
    wordlist = line.split(" ")
    return('-'.join([str(word) for word in wordlist]))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)