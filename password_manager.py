from cryptography.fernet import Fernet

# Call once to generate file, then delete file
# Add a check if file exists at another time
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Change master_pwd to throw error at beginning using Fernet
master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
              
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", 'a') as file:
        file.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")
        


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
        
    if mode == "view":
            view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
