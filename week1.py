#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]

import re
from collections import Counter

def editor(filepath):
    with open(filepath, 'r') as file:
        text = file.read().strip()
        
        if text.isdigit():
            return text[:10]
        else:
            modified_text = text.lower()
            modified_text = re.sub(r'\n', ' ', modified_text)
            words = re.findall(r'\w+', modified_text)
            word_counts = Counter(words)
            top_five = [word for word, count in word_counts.most_common(5)]
            
            return modified_text, top_five

















