def view():
    with open("passwords.txt", 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", passw)
            

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", 'a') as file:
        file.write(name + "|" + pwd + "\n")
        
def main():

    master_pwd = input("What is the master password? ")

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

main()