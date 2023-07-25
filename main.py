import os

def run(x, y):
    with open(x, 'w') as f:
        f.writelines(y)

def display(x):
    with open(x, 'r') as f:
        s = f.read()
        print(s)

def update(x, y):
    with open(x, 'a') as f:
        f.write(y)

def Q1():
    with open('abc.txt', 'r') as f:
        u = 0
        s= f.read()
        for i in s:
            if i.isupper():
                print('uppercase char:', i)
                u+=1
        print('no of uppercase:', u)

def Q2(y):
    with open('abc.txt', 'r') as f:
        c = 0
        s = f.read()
        for i in s:
            if i.lower() == y.lower():
                print('char found:', i)
                c+=1
        print('no of occurences:', c)

def Q3(x, y):
    with open(x, 'r') as f:
        l = f.read()
    with open(y, 'a') as g:
        g.write('\n')
        g.write(l)
    print('displaying second file')
    display(y)

def Q4():
    l = []
    u = []
    o = []
    while True:
        user = input('enter char:')
        if user.islower():
            l.append(user)
        elif user.isupper():
            u.append(user)
        else:
            o.append(user)
        ch = input('Do you wanna continue? (y/s):')
        if ch in 'Nn':
            break
    run('lower.txt', l)
    run('upper.txt', u)
    run('other.txt', o)
    display('lower.txt')
    display('upper.txt')
    display('other.txt')
    
def Q5():
    with open('abc.txt', 'r') as f:
        c = 0
        s= f.read()
        for i in s:
            if i.isdigit():
                print('digit found')
                c+=1
        print('no of digits:', c)

def Q6():
    with open('abc.txt', 'r') as f:
        c = 0
        s= f.read()
        for i in s:
            if i.isspace():
                c+=1
        print('no of spaces:', c)

def Q6_b():
    with open('abc.txt', 'r') as f:
        c = 0
        s= f.read()
        for i in s:
            if i.isspace() or i == '\n':
                c+=1
        print('no of spaces and newline characters:', c)


def Q7():
    with open('abc.txt', 'r') as f:
        f.seek(0, 2)
        size = f.tell()
        print('Total bytes:', size)



def Q8():
    with open('abc.txt', 'r') as f:
        s = f.read()
        s = s.replace(' ', '').replace('\n', '').replace('\t', '')
        print('Total bytes without spaces:', len(s))

def Q9_loop_over():
    with open("abc.txt","r") as f:
        for line in f:
            print(line,end="")

def Q10():
    with open("multi.txt",'w',encoding="utf-8") as f:
        while True:
            line = input("enter a sentence in any language: ")
            f.write (line+'\n')
            ch = input("More (y/n)?")
            if ch in 'nN': 
                break
    with open("multi.txt",'r',encoding="utf-8") as f:
        l = f.readlines()
        for x in l:
            print(x)
                
def Q11():
    with open('abc.txt') as f:
        s = f.read()
        s = s.split()
        print('no of words:', len(s))

#part B

def Q1_B():
    with open('abc.txt', 'r') as f:
        a, b, c = 0, 0, 0
        z=f.read()
        l=z.split()
        for x in l:
            if x=='The':
                a+=1
            elif x=='the':
                b+=1
            elif x=='THE':
                c+=1
            else:
                pass
        print('no of the',a)
        print('no of THE', b)
        print('no of The',c)

def Q2_B(user):
    with open('abc.txt', 'r') as f:
        c = 0
        s=f.read()
        l=s.split()
        for x in l:
            if x.lower() == user.lower():
                c+=1
        print('no of occurences', c)

def Q3_B():
    with open('abc.txt', 'r') as f:
        c = 0
        s=f.read()
        l=s.split()
        for x in l:
            if 'to' in x.lower():
                c+=1
        print('no of occurences of to', c)

def Q4_B():
    with open('abc.txt', 'r') as f:
        c = 0
        s=f.read()
        l=s.split()
        for x in l:
            if x.lower()[0] == 'w':
                c+=1
        print('no of words beg with w', c)
        
def Q5_B():
    with open('abc.txt', 'r') as f:
        u = []
        s=f.read()
        l=s.split()
        for x in l:
            if x[0].isupper():
                u.append(x)
    with open('upper_b.txt', 'w') as f:
        f.writelines(u)
    display('upper_b.txt')

def Q6_B():
    with open('abc.txt') as f:
        s = f.read()
        s = s.split()
        print('no of words:', len(s))

def Q7_B():
    with open('abc.txt') as f:
        s = f.read()
        s = s.lower().replace(' is ', ' was ')
        print(s)

def Q8_B():
    with open('abc.txt') as f:
        s = f.read()
        print(s.title())

def Q9_B():
    with open('abc.txt') as f:
        s = f.read()
        l = s.split()
        rev = []
        for x in l:
            rev.append(x[::-1])
        print(' '.join(rev))
        
def Q10_B():
    with open('abc.txt', 'r') as f:
        s = f.read()
        l = s.lower().split()
        ft = {}
        for x in l:
            if x not in ft:
                ft[x] = s.lower().count(x)
        for x in ft:
            print(x, ':', ft[x])

def Q11_B():
    with open('abc.txt', 'r') as f:
        s = f.read()
        l = s.split()
        v = []
        for x in l:
            for i in x:
                if i in 'AEIOUaeiou':
                    v.append(x)
                    print(x)
                    break
    with open('vowels.txt', 'w') as f:
        f.writelines(v)
    display('vowels.txt')

def Q12_B(y):
    with open('abc.txt', 'r') as f:
        s = f.read()
        l = s.split()
        v = []
        for x in l:
            if len(x) == y:
                print(x)

def Q13_B():
    with open('abc.txt', 'r') as f:
        s = f.read()
        l = s.split()
        max = 0
        for x in l:
            if len(x) > max:
                max = len(x)
                word = x
        print('longest word:', word)

def Q14_B():
    with open('abc.txt', 'r') as f:
        s = f.read()
        l = s.split()
        s = ' '.join(l)
    with open('new.txt', 'w') as f:
        f.write(s)
    os.remove('abc.txt')
    os.rename('new.txt', 'abc.txt')
    display('abc.txt')       
    
def Q15_B(x, y):
    with open(x, 'r') as f:
        l = f.read()
    with open(y, 'a') as g:
        g.write('\n', l)
        
#Part c

def Q1_C():
    with open('abc.txt', 'r') as f:
        l = f.readlines()
        for x in l:
            if x[0] == 'I':
                print(x)

def Q2_C():
    with open('abc.txt', 'r') as f:
        l = f.readlines()
        for x in l:
            if x.lower().startswith('it ') :
                print(x)

def Q3_C():
    with open('abc.txt', 'r') as f:
        l = f.readlines()
        c = 0
        for x in l:
            if x[0] in 'AEIOUaeiou':
                print(x)
                c+=1
        print(c)
        
def Q4_C(x, y):
    with open(x, 'r') as f:
        l = f.read() 
    with open(y, 'w') as f:
        f.write(l)

def Q5_C():
    with open('abc.txt', 'r') as file:
        lines = file.readlines()   
    del lines[1]
    with open('abc.txt', 'w') as file:
        file.writelines(lines)
    print("Second line deleted successfully.")
    display('abc.txt')

def Q6_C(user):
    with open('abc.txt', 'r') as f:
        l = f.readlines()
        for x in l:
            if user.lower() in x.lower():
                print(x)
                
def Q7_C(y):
    with open('abc.txt', 'r') as file:
        lines = file.readlines()
    with open('abc.txt', 'w') as file:
        for x in lines:
            if y not in x:
                file.write(x)
    display('abc.txt')

def Q8_C(y):
    with open("abc.txt","a") as f:
        f.write(y)
    display('abc.txt')

def Q9_C():
    with open('abc.txt', 'r') as f:
        l = f.readlines()
        max = 0
        for x in l:
            if len(x) > max:
                max = len(x)
                line = x
    print('longest line:', line, 'length:', max)
    
def Q10_C(x, y):
    with open(x, 'r') as f:
        l = f.readlines()
    with open(y, 'a') as g:
        g.write('\n')
        for x in l:
            g.write('\n')
            g.write(x)
    display(y)

def Q11_C():
    with open('abc.txt', 'r') as f:
        lines = f.readlines()
        n_elines = 0
        for x in lines:
            if x.strip() == '':
                n_elines+=1
        f.seek(0)
        ch = f.read()
        f.seek(0)
        n_lines = len(lines)
        n_ch = len(ch)
        avg = n_ch/n_lines
        e_avg = n_ch/n_elines
        print('num of lines:', n_lines)
        print('num of empty lines:', n_elines)
        print('avf characters per line:', avg)
        print('avg characters per empty line:', e_avg)



Q11_C()
