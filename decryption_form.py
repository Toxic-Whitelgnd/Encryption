def decrypt_(text,key):
    c = ''
    for txt in text:
        if txt == ' ':
            c += txt
        elif txt.isupper():
            m = int(key)
            c += chr((ord(txt) - m - 65) % 26 + 65)# from  ceaser ciper formula
        elif txt.isdigit():
            m = int(key)
            z = ord(txt)
            x = int(z)
            y = chr((x - m - 48) % 10 + 48)
            f = str(y)
            c += f
        elif txt.islower():
            m = int(key)
            c += chr((ord(txt) - m - 97) % 26 + 97)
        else:
            m = int(key)
            i = ord(txt)
            o = int(i)
            p = chr((o - m - 33) % 15+33)
            l = str(p)
            c += l

    return c