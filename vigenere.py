from caesar import encrypt
from caesar import alphabet_position
from caesar import rotate_character

def encrypt(text,key):
    newMessage=""
    k=[]
    z=0
    count=0
    for i in range(len(text)):
        for j in key:
            k.append(j)
    for jj in text:
        zz=k[z]
        y=alphabet_position(zz)
        if jj.isalpha()==True:
            x=rotate_character(jj,y)
            newMessage+=str(x)
            z+=1
        else:
            x=rotate_character(jj,y)
            newMessage+=str(x)
            
    return newMessage


def main():
    x=raw_input("Hello, please enter a message to encrypt: ")
    y=raw_input("And what is the encryption key: ")
    en=encrypt(x,y)
    print (en)

if __name__=="__main__":
    main()

