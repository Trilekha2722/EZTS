S= input("enter input")
dic = {'A':0,'E':0,'I':0,'O':0,'U':0}
for i in S:
    if i == 'a' or i == 'A':
        dic['A'] += 1
    elif i == 'e' or i == 'E':
        dic['E'] += 1
    elif i == 'i' or i == 'I':
        dic['I'] += 1
    elif i == 'o' or i == 'O':
        dic['O'] += 1
    elif i == 'u' or i == 'U':
        dic['U'] += 1

x=max(dic.values())
result =[]
for i,j in dic.items():
    if j == x:
        result.append(i)

print(result)