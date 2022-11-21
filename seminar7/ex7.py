import re


def cnp_validation(text):
    if re.match(r"^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$", text):
        return True
    return False


print(cnp_validation("011107226727"))
print(cnp_validation("5011107226727"))
