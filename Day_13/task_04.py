try:
    open('u.txt','r',encoding='utf-8').read()
except UnicodeDecodeError as e:
    print(e)
