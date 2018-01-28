passwords = {'default':'defualtpass'}

again = True

def randomgen():
    N = input('How long would you like your password to be? (Number only): ')
    N = int(N)
    if (type(N) == int):
        newpass = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
        print (newpass)
    else:
        pass

while True:
    if (again == True):
        again = False
        websitename = input('Website name: ')
        ### CHECK IF PASS EXISTS ###
        if websitename in passwords:
            for key, value in passwords.items():
                if key == websitename:
                    print ('Your password for', key, 'is', value)
                    again = True
        ### ADD NEW ###
        else:
            print ('You do not have a stored password for this site.')
            choice = input('Do you have a password for this site? (y/n): ')
            if (choice == 'y'):
                password = input('Password: ')
                passwords[websitename]=password
                print (passwords) 
                again = True
            if (choice == 'n'):
                randomgen()
                again = True
            else:
                print ('Answer was not y/n, please input new answer.')  
                again = True
        


