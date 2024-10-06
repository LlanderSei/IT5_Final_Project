import mysql.connector
import hashlib

class CreateDatabase:
  def __init__(self):
    self.__MYSQLConnection = mysql.connector

    print('Connecting to a Database...')
    try:
      self.__MYSQLConnection = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
      print(f'Connection to a Database has been established: {self.__MYSQLConnection}')

      self.__MYSQLCursor = self.__MYSQLConnection.cursor()
    except Exception as ERR:
      print(f'Error: {ERR}')

  def CURSOR(self):
    return self.__MYSQLCursor
  
  def CONNECTOR(self):
    return self.__MYSQLConnection

  def buildDatabase(self):
    # CREATES DATABASE IF NOT EXISTS YET, THEN INSTANTLY USES THAT DATABASE
    self.CURSOR().execute('create database if not exists USER_FINANCIAL_DATABASE')
    self.CURSOR().execute('use USER_FINANCIAL_DATABASE')

    # CREATE THE TABLE WITH COLUMNS FOR USERS
    self.CURSOR().execute('''create table if not exists USERS(
                                USER_ID integer not null auto_increment primary key,
                                USERNAME varchar(255) not null unique,
                                HASHED_PASSWORD varchar(255) not null);''')
    
    # CREATE THE TABLE WITH COLUMNS FOR USER'S INFO
    self.CURSOR().execute('''create table if not exists USER_INFOS(
                                USER_ID integer,
                                foreign key (USER_ID) references USERS(USER_ID)
                                  on delete cascade on update restrict,
                                GIVEN_NAME varchar(100) not null,
                                MIDDLE_INITIAL varchar(100),
                                LAST_NAME varchar(100),
                                AGE integer,
                                ADDRESS text,
                                BALANCE float(50,2));''')
    
    # CREATE THE TABLE WITH COLUMNS FOR USER'S LIFE STATES
    self.CURSOR().execute('''create table if not exists USER_LIFE_STATES(
                                USER_ID integer,
                                foreign key (USER_ID) references USERS(USER_ID)
                                  on delete cascade on update restrict,
                                IS_STUDENT boolean,
                                HAS_KIDS boolean,
                                IS_FREAKY boolean);''')
    
    # CREATES TABLE WITH COLUMNS FOR USER'S NEEDS AND WANTS, ETC.
    self.CURSOR().execute('''create table if not exists USER_LIFE_OBJECTIVES(
                                OBJECTIVE_ID integer not null auto_increment primary key,
                                USER_ID integer,
                                foreign key (USER_ID) references USERS(USER_ID)
                                  on delete cascade on update restrict,
                                OBJECTIVE varchar(255) not null unique,
                                CATEGORY varchar(50) not null,
                                COST float(20,2) not null );''')
    
    # ONLY FOR STORING UNHASHED PASSWORD PURPOSES, SINCE HASHED PASSWORDS ARE IRREVERSIBLE
    self.CURSOR().execute('''create table if not exists USER_PASSWORDS(
                                USER_ID integer,
                                  foreign key (USER_ID) references USERS(USER_ID)
                                    on delete cascade on update restrict,
                                UNHASHED_PASSWORD varchar(255));''')

class DatabaseInteraction:
  __USER_ID = int
  __TEMP_USER_CRED = any

  def __init__(self): 
    self.__DB = CreateDatabase()
    self.__DB.buildDatabase()
    self.__USER_ID, self.__TEMP_USER_CRED
    
    self.__USER_ID
  
  def RegisterUser(self, OBJECTS):
    USERNAME, PASSWORD, GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS = OBJECTS
    try:
      if not self.__IsUserAlreadyExists(USERNAME):
        self.__DB.CURSOR().execute('insert into USERS(USERNAME, HASHED_PASSWORD) values (%s, SHA2(%s, 256))', (USERNAME, PASSWORD))
        self.__DB.CURSOR().execute(f'select USER_ID from USERS where USERNAME = \'{USERNAME}\'')
        getFetched = self.__DB.CURSOR().fetchone()

        if getFetched: tempID = getFetched[0]
        self.__DB.CURSOR().execute('insert into USER_PASSWORDS(USER_ID, UNHASHED_PASSWORD) values (%s, %s)', (tempID, PASSWORD))
        self.__DB.CURSOR().execute('insert into USER_INFOS(USER_ID, GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS) values (%s, %s, %s, %s, %s, %s)', (tempID, GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS))
        self.__InstanceUserLifeStatus(tempID)
        self.__DB.CONNECTOR().commit()
    except mysql.connector.Error as ERR:
      self.__DB.CONNECTOR().rollback()
      print(f'Error: {ERR}')
  
  def LoginUser(self, MODE, CREDENTIAL):
    match MODE:
      case 'USERNAME':
        self.__DB.CURSOR().execute(f'select * from USERS where USERNAME = \'{CREDENTIAL.lower()}\'')
        self.__TEMP_USER_CRED = self.__DB.CURSOR().fetchone()
        if self.__TEMP_USER_CRED: return 'USERFOUND'
        else: return 0

      case 'PASSWORD':
        if self.__TEMP_USER_CRED[2] == self.__hashedPassword(CREDENTIAL): return 'PASSWORDMATCHED'
        else: return 0

  def FetchUserAllInfo(self, FETCH):
    match FETCH:
      case 'USER':
        self.__DB.CURSOR().execute(f'select USER_ID, USERNAME from USERS where USER_ID = \'{self.__USER_ID}\'')
        USER_ID, USERNAME = self.__DB.CURSOR().fetchone()
        return USER_ID, USERNAME
      case 'USERINFO':
        self.__DB.CURSOR().execute(f'select GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS, BALANCE from USER_INFOS where USER_ID = \'{self.__USER_ID}\'')
        GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS, BALANCE = self.__DB.CURSOR().fetchone()
        return GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS, BALANCE
      case 'LIFESTATUS':
        self.__DB.CURSOR().execute(f'select IS_STUDENT, HAS_KIDS, IS_FREAKY from USER_LIFE_STATUSES where USER_ID = \'{self.__USER_ID}\'')
        IS_STUDENT, HAS_KIDS, IS_FREAKY = self.__DB.CURSOR().fetchone()
        return IS_STUDENT, HAS_KIDS, IS_FREAKY
      case 'OBJECTIVES':
        self.__DB.CURSOR().execute(f'select OBJECTIVE, CATEGORY, COST from USER_LIFE_OBJECTIVES where USER_ID = \'{self.__USER_ID}\'')
        OBJECTIVELIST = self.__DB.CURSOR().fetchall()
        return OBJECTIVELIST

  def ModifyLifeStatuses(self, *BOOLEANS):
    IS_STUDENT, HAS_KIDS, IS_FREAKY = BOOLEANS
    self.__DB.CURSOR().execute('''update USER_LIFE_STATES set
                                    IS_STUDENT = %s,
                                    HAS_KIDS = %s,
                                    IS_FREAKY = %s
                                    where USER_ID = %s''',
                                    IS_STUDENT, HAS_KIDS, IS_FREAKY, self.__USER_ID)

  def ModifyObjectives(self, MODE, *OBJECT):
    try:
      match MODE:
        case 'ADD': # [0] OBJECTIVE, [1] CATEGORY, [2] COTS in OBJECT
          self.__DB.CURSOR().execute('''insert into USER_LIFE_OBJECTIVES(USER_ID, OBJECTIVE, CATEGORY, COST)
                                          values (%s, %s, %s, %s)''', (self.__USER_ID, OBJECT[0], OBJECT[1], OBJECT[2]))
        case 'UPDATE': # [0] OBJECTIVE, [1] CATEGORY, [2] COTS in OBJECT
          self.__DB.CURSOR().execute('''update USER_ITEM_OBJECTIVES set
                                          OBJECTIVE = %s,
                                          CATEGORY = %s,
                                          COST = %s
                                          where USER_ID = %s''',
                                          (OBJECT[0], OBJECT[1], OBJECT[2], self.__USER_ID))
        case 'DELETE': # [0] OBJECTIVE
          self.__DB.CURSOR().execute('delete from USER_ITEM_OBJECTIVES where OBJECTIVE = %s and USER_ID = %s', (OBJECT[0], self.__USER_ID))
      self.__DB.CONNECTOR().commit()
      return 'SUCCESS'
    except mysql.connector.Error as ERR:
      print(f'An error occured: {ERR}')
      return 0

  def ModifyUser(self, MODE, *OBJECT):
    match MODE:
      case 'INFO':
        GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS = OBJECT
        self.__DB.CURSOR().execute('update USER_INFOS set GIVEN_NAME = %s, MIDDLE_INITIAL = %s, LAST_NAME = %s, AGE = %s, ADDRESS = %s where USER_ID = %s', (GIVEN_NAME, MIDDLE_INITIAL, LAST_NAME, AGE, ADDRESS, self.__USER_ID))
      case 'USERNAME':
        USERNAME = OBJECT[0]
        if not self.__IsUserAlreadyExists(USERNAME):
          self.__DB.CURSOR().execute('update USERS set USERNAME = %s where USER_ID = %s', (USERNAME, self.__USER_ID))
      case 'PASSWORD':
        PASSWORD = OBJECT[0]
        self.__DB.CURSOR().execute('update USERS set HASHED_PASSWORD = SHA2(%s, 256) where USER_ID = %s', (PASSWORD, self.__USER_ID))
        self.__DB.CURSOR().execute('update USER_PASSWORDS set UNHASHED_PASSWORD = %s where USER_ID = %s', (PASSWORD, self.__USER_ID))
      case 'BALANCE':
        BALANCE = OBJECT[0]
        self.__DB.CURSOR().execute('update USER_INFOS set BALANCE = %s where USER_ID = %s', (BALANCE, self.__USER_ID))
    self.__DB.CONNECTOR().commit()

  def __hashedPassword(self, PASSWORD):
    HASHED_PASSWORD = hashlib.sha256(PASSWORD.encode()).hexdigest()
    return HASHED_PASSWORD
  
  def __IsUserAlreadyExists(self, USERNAME):
    self.__DB.CURSOR().execute(f'select USERNAME from USERS where USERNAME = \'{USERNAME}\'')
    FetchResult = self.__DB.CURSOR().fetchone()
    if FetchResult:
      print(f'Username \'{USERNAME}\' already exists.')
      return True
    else: return False

  def __InstanceUserLifeStatus(self, USER_ID):
    self.__DB.CURSOR().execute('insert into USER_LIFE_STATES(USER_ID, IS_STUDENT, HAS_KIDS, IS_FREAKY) values (%s, %s, %s, %s)', (USER_ID, None, None, None))