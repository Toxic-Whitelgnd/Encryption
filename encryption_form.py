def encrypt_(text,key):
    c='' #empty string

    for txt in text:
        if txt==' ':#space
            c += txt
        elif txt.isupper():
            m = int(key)
            c += chr((ord(txt)+ m - 65) % 26 + 65) # from ceaser ciper formula
        #start someting
        elif txt.isdigit():
            m=int(key)
            z = ord(txt)           #coverting the number into ASCII
            x = int(z)           #convertin the string to integer
            y = chr((x + m - 48) % 10 + 48)    #formula derived by me
            f = str(y)          #convertin to string for appending
            c += f              #adding back to the string to print the result

        elif txt.islower():
            e=int(key)
            c += chr((ord(txt)+ e - 97) % 26 + 97)
        else:
            m = int(key)
            i = ord(txt)
            o = int(i)
            p = chr((o + m - 33) % 15 + 33)
            l = str(p)
            c += l
    return c