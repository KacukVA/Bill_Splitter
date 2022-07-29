# put your python code here
import string
double_alphabet = dict()
a = string.ascii_lowercase
for _ in a:
    double_alphabet.update({_: _ * 2})
