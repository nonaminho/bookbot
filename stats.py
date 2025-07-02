def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


def count_words(text):
    return len(text.split())

def sort_on(items):
    return items['num']

def count_each(text):
    count_dict={}
    dict_list=[]
    text = text.lower()
    for char in text:
        if char in count_dict:   
            count_dict[char]+=1
        else:
            count_dict[char]=1

    for entry in count_dict:
        if entry.isalpha():
            dict_list.append({'char':entry , 'num': count_dict[entry]})
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list