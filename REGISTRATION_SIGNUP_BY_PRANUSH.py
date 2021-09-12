filename_1='usernames.txt'
password=''
password_1=' '
password_2=' '
filename_3=''
LOGIN=input('ARE YOU A REGISTERED USER'+' '+'Y'+'/'+'N')
user_reply=LOGIN.title()
if user_reply=='Y':
    class UserAUTH():
        while True:
            input_username=input('enter your user name'+'\n')
            filename=open('usernames.txt', 'r')
            file_name_1=filename.read()
            username_1=file_name_1.split()
            if input_username in username_1:
                try:
                    with open(input_username+'.txt') as filename_3:
                        password=filename_3.read()
                        password_1=str(set(password))
                except FileNotFoundError:
                    print('Your password Files has been removed')
     
            
                break
            else:
                print('Please Enter Correct UserName')
        while True:
            password_user=str(input('please input password'+' '+'\n'))
            password_2=str(set(password_user))
        
            if password_2==password_1:
                print('Password Matching')
                break
            else:
                print('Please Enter Correct PassWord')
    pass
else:
    new_user=input('Enter Username')
    new_password=input('Enter Password')
    with open(filename_1,'a') as file_name_1:
        file_name_1.write('\n'+new_user+'\n')
    pass_file=(new_user+'.txt')
    with open(pass_file,'w') as pass_file_1:
        pass_file_1.write(new_password)
    
                 

    
