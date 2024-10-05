from DatabaseFunctions import DatabaseInteraction

SIGNUPINFOS = {'Username': None, 'Password': None, 'Given Name': None, 'Middle Initial': None, 'Last Name': None, 'Age': None, 'Address': None}
LOGININFO = {'Username': '', 'Password': ''}

# TESTESTESTETSETSTESTESTESETSTESTETSETSTETSTSETSTETSTTESTESTESESESTTSETSETS!!!!!

db = DatabaseInteraction()
while True:
  Mode = input('[s] Signup | [l] Login: ')
  match Mode.lower():
    case 'l':
      while True:
        USERINPUT = input(f'Enter username: ')
        if USERINPUT:
          RESULT = db.LoginUser('USERNAME', USERINPUT.lower())
          if RESULT == 'USERFOUND':
            while True:
              USERPASS = input('Enter password: ')
              if USERPASS:
                RESULT = db.LoginUser('PASSWORD', USERPASS)
                if RESULT == 'PASSWORDMATCHED':
                  print('Credentials confirmed!')
                  break
                else:
                  print('Credentials do not match.')
              else:
                print('Empty field.')
          else:
            print('User does not exist.')
        else:
          print('Empty field.')

    case 's':
      for Count, Keys in enumerate(SIGNUPINFOS.keys()):
        while True:
          try:
            USERINPUT = input(f'Enter {Keys}: ')
            match Count + 1:
              case 1 | 2 | 3:
                if USERINPUT: SIGNUPINFOS[Keys] = USERINPUT; break
                else: print(f'{Keys} cannot be empty.')
              case 6: 
                if USERINPUT: SIGNUPINFOS[Keys] = int(USERINPUT); break
                else: break
              case _:
                SIGNUPINFOS[Keys] = USERINPUT; break
          except Exception as ERR:
            print(f'Error: {ERR}')

      print(SIGNUPINFOS.values())

      db.RegisterUser(SIGNUPINFOS.values())

  db.FetchUserAllInfo('USER'[0])
  db.ModifyObjectives()
  print()