index = []

def insert_new_keyword(index, keyword, url):
    new_key = [keyword]
    new_key.append([])
    new_key[1].append(url)
    index.append(new_key)

def add_to_index(index,keyword,url):
    for arr in index:
        if keyword == arr[0]:
            arr[1].append(url)
            return
    insert_new_keyword(index, keyword, url)

def lookup(index, keyword):
    for arr in index:
        if arr[0] == keyword:
            return arr[1]
    return []


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index

print lookup(index, 'udacity')

def add_page_to_index(index,url,content):
    str_arr = content.split()
    for string in str_arr:
        add_to_index(index, string, url)

add_page_to_index(index,'fake.text',"This is a test")
print(index)