import requests

def signup():
    name = input("Name : ")
    email = input("Email : ")
    password = input("Password : ")
    data = {"name":name, "email":email, "password":password}
    resp = requests.post("http://127.0.0.1:4000/user/signup", json=data).content.decode()
    print(resp)

def signin():
    email = input("Email : ")
    password = input("Password : ")
    data = {"email":email, "password":password}
    resp = requests.post("http://127.0.0.1:4000/user/signin", json=data).content.decode()
    print(resp)

def signout():
    resp = requests.get("http://127.0.0.1:4000/user/signout").content.decode()
    print(resp)

print("1 : Signup")
print("2 : Signin")
print("3 : Signout")
print("0 : Exit")
ip_code = 1
while ip_code:
    ip_code = int(input("Enter code : "))
    if ip_code == 1:
        signup()
    elif ip_code == 2:
        signin()
    elif ip_code == 3:
        signout()
print("Bye")