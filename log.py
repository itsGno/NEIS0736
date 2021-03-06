import datetime
import hashlib

def writeLog():
    f.write('Username: '+username+'\n')
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    f.write('password: '+sha256.hexdigest()+'\n')
    f.write('login date: '+str(datetime.datetime.now())+'\n')

print('welcome to member system')
while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == 'Test' and password == '1234':
        print('login Successfully')
        f = open('login.txt','a')
        writeLog()
        f.write('#'*30+'\n')
        f.close()
        break
    else:
        print('wrong username or password')