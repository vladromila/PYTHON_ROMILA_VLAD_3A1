import re


def extract_words(text):
    return re.split(r'(?:\s*\S*[\$\!]+\S*\s*|\s+)', text)


print(extract_words("asdjas12kdfsa faskdjf asdfjl asd fa2s134"))
