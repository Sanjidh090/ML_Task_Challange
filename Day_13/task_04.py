try:
    with open('u.txt','r',encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError as e:
    print(e)
