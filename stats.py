def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


def count_words(text):
    return len(text.split())


def count_each(text):
    count_dict={}
    text = text.lower()
    for char in text:
        if char in count_dict:   
            count_dict[char]+=1
        else:
            count_dict[char]=1
            
    
    return count_dict