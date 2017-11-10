String1 = r"my name is Sagar pan is AHYUH4444V date of birth is 02\11\1984. 123.10.23.45"

import re

name = re.findall(r'[A-Z][a-z]+', String1)
print(name)
pan_no = re.findall(r'[A-Z]{5}\d{4}[A-Z]{1}', String1)
print(pan_no)
date = re.findall(r'\d{1,2}\\\d{1,2}\\\d{4}\W', String1)
print(date)
IP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', String1)
print(IP)

str2 = '[1,2,3]'
list1 = re.findall(r'[[][\d,]+[]]', str2)
print(list1)
str3 = 'sabbbadddabbbb'
match = re.search('ab?', str3)
print(match.group(0))

str4 = '1,fdfdf2,fdfdsffs3'
list2 = re.findall(r'^\d.+\d$', str4)
print(list2)

str5 = '1zfdfdf2fdfdsffs3'
z_1 = re.findall(r'\w*[z]\w*', str5)
print(z_1)
z_1 = re.findall(r'\w*[z]\w*', str5)
print(z_1)

str6 = "   __  __ "
repl = re.sub('\s','_',str6)
print(repl)
z_1 = re.findall(r'(dfdf2)', str5)
print(z_1)
str5 = 'an est fgh wer aser erd ddd awe fff ewww'
z_1 = re.findall('[ae]\w+', str5)
print(z_1)

text = 'The quick brown fox jumps over the lazy dog.'
z_1 = re.findall(r'\b\w{4,}\b', text)
print(z_1)

text1 = 'Python      Exercises'
z_1 = re.sub(' +',' ',text1)
print(z_1)
text1 = 'cdscscs https://www.w3resource.com dscdscdssvsvsvdvsv'
z_1 = re.findall(r'https://[\w.]+', text1)
print(z_1)
z_1 = re.split(' ', text)
print(z_1)
li1= ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for patt in li1:
    match = re.search('\w+',patt)
    print (match.group())