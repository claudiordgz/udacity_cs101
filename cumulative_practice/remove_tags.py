# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.


#inneficient
import string

def remove_tags_inefficient(text):
    to_replace = []
    for idx, ch in enumerate(text):
        if ch == '<':
            begin_pos = idx
            end_pos = text.find('>', begin_pos)
            to_replace.append(text[begin_pos:end_pos+1])
    new_text = text
    for e in to_replace:
        new_text = string.replace(new_text, e, ' ', 1)
    return new_text.split()


def remove_tags(text):
    string_array = []
    begin_pos = -1
    for idx, ch in enumerate(text):
        if ch == '<':
            if begin_pos != -1:
                if text[begin_pos:idx] != '':
                    to_append = text[begin_pos:idx].split()
                    string_array.extend(to_append)
                begin_pos = -1
            end_pos_tag = text.find('>', idx) + 1
            begin_pos = end_pos_tag
    return string_array


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']