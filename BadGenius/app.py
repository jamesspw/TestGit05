substitution = {
        'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
        'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
        'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
        'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
}
def reduce_20(input_string):
    if len(input_string) != 40:
        raise ValueError("Input string must be 40 characters long")

    result = []
    for i in range(0, len(input_string), 2):
        pair = input_string[i:i + 2]
        if pair in substitution:
            result.append(substitution[pair])
        else:
            raise ValueError(f"Invalid pair: {pair}")

    return ''.join(result)
def convert_40(input_string):
    if len(input_string) != 20:
        raise ValueError("Input string must be 20 characters long")

    result = []
    for char in input_string:
        found = False
        for pair, replacement in substitution.items():
            if replacement == char:
                result.append(pair)
                found = True
                break
        if not found:
            raise ValueError(f"Invalid character: {char}")

    return ''.join(result)
print("Before =", "abbbdbacbcbbcdbacbbbbcdbbbbacbbbdaacdadb")
print("Reduce =", reduce_20("abbbdbacbcbbcdbacbbbbcdbbbbacbbbdaacdadb"))
print("After =", convert_40(reduce_20("abbbdbacbcbbcdbacbbbbcdbbbbacbbbdaacdadb")))