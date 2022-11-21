import re


def extract_words(reg, text, x):
    results = re.findall(reg, text)
    toReturnResults = []
    for result in results:
        if len(result) < x:
            toReturnResults.append(result)
    return results


print(extract_words(r'(\d+[a-z]+)', '12124adbad13434AGDFDF434348888AAA', 10))
