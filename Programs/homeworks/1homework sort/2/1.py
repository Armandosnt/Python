import re

text = r""" 
kopeev1999@gmail.com
kopeev99@mail.ru
sasuke96maho@mail.ru
""" 
print(re.findall(r'Торт.с', text)) 
# -> [] 
print(re.findall(r'Торт.с', text, flags=re.DOTALL)) 
# -> ['Торт\nс'] 
print(re.findall(r'kopeev99@mail.ru\w+', text, flags=re.MULTILINE)) 
# -> ['вишней1', 'вишней2'] 
print(re.findall(r'^sasuke96maho@mail.ru\w+', text, flags=re.MULTILINE)) 
# -> ['вишней2'] 