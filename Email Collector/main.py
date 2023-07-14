import re

str = '''ved
ayk,mm
vedshiv@gmail.com
jbblk;4
ved
abc@gmail.com
sjdjdm
123@gmail.com
'''

email = re.compile(r"[0-9A-Za-z._+%]+@[0-9A-Za-z._+%]+[.][0-9A-Za-z.]+")

matches = email.findall(str)
for match in matches:
    print(match)
    
# with open(r"C:\Coding\python\projects\Email Collector\emails.txt" , "w") as f:
#     f.write(match)
