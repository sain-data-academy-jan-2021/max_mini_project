

def read_file(filename):
    file = open(filename, 'r')
    for line in file.readlines():
        temp = line.strip()
    return temp


def login():
    while True:     
        user = input("Username: ")
        passw = input("Password: ")
        
        
        un = read_file('username.txt')
        pw = read_file('password.txt')
        

        if user == un and passw == pw:
            print ("Login successful!")
            return
        print ("Wrong username/password")

login()
