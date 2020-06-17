login  = {
    1 : {
        "username": "anu",
        "password": "pass1"
    }, 
    2 : {
        "username": "ifedi",
        "password": "pass2"
    },
    3 : {
        "username": "tise",
        "password": "pass3"
    },
    4 : {
        "username": "caleb",
        "password": "pass4"
    },
    5 : {
        "username": "funmi",
        "password": "pass5"
    },
    6 : {
        "username": "anu1",
        "password": "pass6"
    }, 
    7 : {
        "username": "ifedi1",
        "password": "pass7"
    },
    8 : {
        "username": "tise1",
        "password": "pass8"
    },
    9 : {
        "username": "caleb1",
        "password": "pass9"
    },
    10 : {
        "username": "funmi1",
        "password": "pass10"
    }
}

# print(login)
print(login[10]['username'])
username = input("Username: ")
password = input("password: ")
for id in login:
  #print(id)
  if username == login[id]['username'] and password == login[id]['password']:
    print("yees")
  else:
    print("invalid username or password")
