import sys
import os
from time import sleep
print("""           Email Filter By Domain v 0.0.1

                            
                    Telegram : https://t.me/itslucifero
                       
                            
                            
                             """) 
print(' GIVE ME A FRACTION OF SECOND MUHAHAHAH\n')
print('RESULT WILL BE SAVED IN mrhouse998 REZULT FOLDER.\n \n')                                          
mlist = input("Enter the list path : ")

dir = 'mrhouse998 REZULT'
os.mkdir(dir)

for email in open(mlist, 'r'):
    email = email.strip()
    if '@gmail' in email:
        gmail = open(f'{dir}/gmail.txt', 'a+')
        gmail.write(email + '\n')
        gmail.close()
        print('[GMAIL] -', email)
    elif '@yahoo' in email:
        yahoo = open(f'{dir}/yahoo.txt', 'a+')
        yahoo.write(email + '\n')
        yahoo.close()
        print('[YAHOO] -', email)
    elif '@hotmail' in email:
        hotmail = open(f'{dir}/hotmail.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[HOTMAIL] -', email)
    elif '@aol.com' in email:
        hotmail = open(f'{dir}/aol.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[AOL] -', email)
    elif '@yandex.ru' in email:
        hotmail = open(f'{dir}/yandex-ru.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[YANDEX] -', email)
    else:
        other = open(f'{dir}/other.txt', 'a+')
        other.write(email + '\n')
        other.close()
print("-------------------------------")
print("IM DONE GETFO!!!!! ", len(open(mlist, 'r').readlines()), ' ,i,')
sleep(2)
