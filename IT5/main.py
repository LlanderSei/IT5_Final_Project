from Database.Database import Databases

db = Databases('localhost', 'root', '', 'it5_arizobal')

while True:
    print("[1] Register\n[2] Login\n[3] Log-out\n[4] Blog\n[5] Fetch_Blog\n[x] Exit")
    choice = input()
    if choice == "x":
        break

    if choice == "1":
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")

        db.register(name, username, password)
    
    elif choice == '2':
        username = input("Please Enter Your Username: ")
        password = input("Please Enter Your Password: ")
        user = db.login(username, password)
        print(user)
    
    elif choice == '3':
        db.logout()

    elif choice == '4':
        post = input()
        db.create_blog(post)
    
    elif choice == '5':
        blogs = db.fetch_blogs()
        for blog in blogs:
            print(blog[1])
