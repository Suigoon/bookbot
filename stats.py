def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(words):
    lowercase = words.lower()
    char_count = {}
    for char in lowercase:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["Num"]


def sort_list(char_count):
    sorted = []
    for char, count in char_count.items():
        char_info = {"char": char, "Num": count}  
        sorted.append(char_info)
    sorted.sort(key=sort_on, reverse=True)
    
    return sorted