name=input()
name=list(name)
distinct_name=[]
for i in name:
    if i not in distinct_name:
        distinct_name.append(i)
distinct_name=''.join(distinct_name)
if len(distinct_name)%2==1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')

