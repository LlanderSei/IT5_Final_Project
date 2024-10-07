from Database.Database import Databases

db = Databases('localhost', 'root', '', 'it5_arizobal')

while True:
    print("[1] Register\n[2] Login\n[3] Log-out\n[4] Blog\n[5] Read_Blog\n[6] Update_Blog\n[7] Delete_Blog\n[x] Exit")
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
        
    elif choice == '6':
        blogs = db.fetch_blogs()
        index = int(input("Enter what blog to update: "))
        db.update_blog(blogs[index - 1][0], input("Enter post: "))

    elif choice == '7':
        blogs = db.fetch_blogs()
        index = int(input("Enter what item to delete. "))
        db.delete_blog(blogs[index - 1][0])
