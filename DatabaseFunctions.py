import mysql.connector
import hashlib

class CreateDatabase:

  def __init__(self):
    self.__MYSQLConnection = None
    self.__MYSQLCursor = None

    self.__DEFAULTLOGIN()
    
  def __DEFAULTLOGIN(self):
    try:
      self.__MYSQLConnection = mysql.connector.connect(host='localhost', user='root', password='')
      self.__MYSQLCursor = self.__MYSQLConnection.cursor()
      self.buildDatabase()
      print(self.__MYSQLConnection)
    except mysql.connector.Error as ERR:
      print(f'Connection Error. Error {ERR}')
      print('You may need to change the credentials of the database by pressing that DB icon.')
      self.__MYSQLConnection = None
      self.__MYSQLCursor = None
  
  def LOGINDATABASE(self, HOST, USER, PASSWORD):
    try:
      self.__MYSQLConnection = mysql.connector.connect(host = f'{HOST}', user = f'{USER}', password =f'{PASSWORD or ''}')
      self.__MYSQLCursor = self.__MYSQLConnection.cursor()
      self.buildDatabase()
      return 'SUCCESSFUL'
    except mysql.connector.Error:
      self.__MYSQLConnection = None
      self.__MYSQLCursor = None
      return 'ERROR'

  def CURSOR(self):
    return self.__MYSQLCursor
  
  def CONNECTOR(self):
    return self.__MYSQLConnection
  
  def HAS_CONNECTION(self):
    try:
      if self.__MYSQLConnection.is_connected(): return 1
    except Exception:
      return 0
  
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
                                FIRST_NAME varchar(100) not null,
                                LAST_NAME varchar(100),
                                AGE integer,
                                ADDRESS text,
                                NOTES text,
                                MONTH_OF text);''')
    
    # CREATE THE TABLE WITH COLUMNS FOR USER'S LIFE STATES
    self.CURSOR().execute('''create table if not exists USER_BANK_INFOS(
                                USER_ID integer,
                                foreign key (USER_ID) references USERS(USER_ID)
                                  on delete cascade on update restrict,
                                ADD_SAVINGS float(50,2),
                                SAVINGS float(50,2),
                                STIPEND float(50,2),
                                BUDGET_NEEDS float(50,2),
                                BUDGET_WANTS float(50,2));''')
    
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
  __TEMP_USER_CRED = None

  def __init__(self):
    self.__USER_ID, self.__TEMP_USER_CRED
    self.__DB = CreateDatabase()

  def LoginDatabase(self, HOST, USER, PASSWORD):
    return self.__DB.LOGINDATABASE(HOST, USER, PASSWORD)

  def HasConnection(self):
    return self.__DB.HAS_CONNECTION()
  
  def GetConnector(self):
    return self.__DB.CONNECTOR()

  def GET_User_ID(self):
    return self.__USER_ID

  def BuildDatabase(self):
    self.__DB.buildDatabase()

  def RegisterUser(self, FIRSTNAME, LASTNAME, AGE, ADDRESS, USERNAME, PASSWORD):
    try:
      if not self.__IsUserAlreadyExists(USERNAME):
        self.__DB.CURSOR().execute('insert into USERS(USERNAME, HASHED_PASSWORD) values (%s, SHA2(%s, 256))', (USERNAME, PASSWORD))
        self.__DB.CURSOR().execute(f'select USER_ID from USERS where USERNAME = \'{USERNAME}\'')
        getFetched = self.__DB.CURSOR().fetchone()

        if getFetched: tempID = getFetched[0]
        self.__DB.CURSOR().execute('insert into USER_PASSWORDS(USER_ID, UNHASHED_PASSWORD) values (%s, %s)', (tempID, PASSWORD))
        self.__DB.CURSOR().execute('insert into USER_INFOS(USER_ID, FIRST_NAME, LAST_NAME, AGE, ADDRESS, NOTES, MONTH_OF) values (%s, %s, %s, %s, %s, %s, %s)', (tempID, FIRSTNAME, LASTNAME, AGE, ADDRESS, None, None))
        self.__InstantiateUserObjects(tempID)
        self.__DB.CONNECTOR().commit()
        return 'REGSUCCESS'
      else:
        return 'USERALREADYEXIST'
    except mysql.connector.Error as ERR:
      self.__DB.CONNECTOR().rollback()
      return 'REGERROR'
  
  def LoginUser(self, USERNAME, PASSWORD):
    self.__DB.CURSOR().execute(f"select * from USERS where USERNAME = '{USERNAME}' and HASHED_PASSWORD = '{self.__hashedPassword(PASSWORD)}'")
    self.__TEMP_USER_CRED = self.__DB.CURSOR().fetchone()
    if self.__TEMP_USER_CRED:
      self.__USER_ID = self.__TEMP_USER_CRED[0]
      return 'LOGINSUCCESS'
    else: return 'LOGINERROR'

  def FetchUserAllInfo(self, FETCH):
    match FETCH:
      case 'USER':
        self.__DB.CURSOR().execute(f"select USER_ID, USERNAME from USERS where USER_ID = '{self.__USER_ID}'")
        USER_ID, USERNAME = self.__DB.CURSOR().fetchone()
        return USER_ID, USERNAME
      case 'USERINFO':
        self.__DB.CURSOR().execute(f"select FIRST_NAME, LAST_NAME, AGE, ADDRESS, NOTES, MONTH_OF from USER_INFOS where USER_ID = '{self.__USER_ID}'")
        FIRST_NAME, LAST_NAME, AGE, ADDRESS, NOTES, MONTH_OF = self.__DB.CURSOR().fetchone()
        return FIRST_NAME, LAST_NAME, AGE, ADDRESS, NOTES, MONTH_OF
      case 'BANKS':
        self.__DB.CURSOR().execute(f"select ADD_SAVINGS, SAVINGS, STIPEND, BUDGET_NEEDS, BUDGET_WANTS from USER_BANK_INFOS where USER_ID = '{self.__USER_ID}'")
        ADD_SAVINGS, SAVINGS, STIPEND, BUDGET_NEEDS, BUDGETS_WANTS = self.__DB.CURSOR().fetchone()
        return ADD_SAVINGS, SAVINGS, STIPEND, BUDGET_NEEDS, BUDGETS_WANTS
      case 'OBJECTIVES':
        self.__DB.CURSOR().execute(f"select OBJECTIVE, CATEGORY, COST from USER_LIFE_OBJECTIVES where USER_ID = '{self.__USER_ID}'")
        OBJECTIVELIST = self.__DB.CURSOR().fetchall()
        return OBJECTIVELIST

  def ModifyUser(self, MODE, *OBJECTS):
    match MODE:
      case 'INFO':
        FIRST_NAME, LAST_NAME, AGE, ADDRESS = OBJECTS
        self.__DB.CURSOR().execute("update USER_INFOS set FIRST_NAME = %s, LAST_NAME = %s, AGE = %s, ADDRESS = %s where USER_ID = %s", (FIRST_NAME, LAST_NAME or None, AGE or None, ADDRESS or None, self.__USER_ID))
      case 'NOTES':
        NOTES = OBJECTS[0]
        self.__DB.CURSOR().execute(f"update USER_INFOS set NOTES = \"{NOTES}\" where USER_ID = {self.__USER_ID}")
      case 'MONTH_OF':
        MONTH_OF = OBJECTS[0]
        self.__DB.CURSOR().execute(f"update USER_INFOS set MONTH_OF = \"{MONTH_OF}\" where USER_ID = {self.__USER_ID}")
      case 'USERNAME':
        USERNAME = OBJECTS[0]
        if not self.__IsUserAlreadyExists(USERNAME):
          self.__DB.CURSOR().execute(f"update USERS set USERNAME = '{USERNAME}' where USER_ID = {self.GET_User_ID}")
      case 'PASSWORD':
        PASSWORD = OBJECTS[0]
        self.__DB.CURSOR().execute('update USERS set HASHED_PASSWORD = SHA2(%s, 256) where USER_ID = %s', (PASSWORD, self.__USER_ID))
        self.__DB.CURSOR().execute('update USER_PASSWORDS set UNHASHED_PASSWORD = %s where USER_ID = %s', (PASSWORD, self.__USER_ID))
      case 'BANK_INFOS':
        ADD_SAVINGS, SAVINGS, STIPEND, BUDGET_NEEDS, BUDGET_WANTS = OBJECTS 
        self.__DB.CURSOR().execute(f"update USER_BANK_INFOS set ADD_SAVINGS = {ADD_SAVINGS}, SAVINGS = {SAVINGS}, STIPEND = {STIPEND}, BUDGET_NEEDS = {BUDGET_NEEDS}, BUDGET_WANTS = {BUDGET_WANTS} where USER_ID = {self.__USER_ID}")
    self.__DB.CONNECTOR().commit()

  # def ModifyLifeStatuses(self, *BOOLEANS):
  #   IS_STUDENT, HAS_KIDS, IS_FREAKY = BOOLEANS
  #   self.__DB.CURSOR().execute('''update USER_LIFE_STATES set
  #                                   IS_STUDENT = %s,
  #                                   HAS_KIDS = %s,
  #                                   IS_FREAKY = %s
  #                                   where USER_ID = %s''',
  #                                   IS_STUDENT, HAS_KIDS, IS_FREAKY, self.__USER_ID)

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

  def __InstantiateUserObjects(self, USER_ID):
    self.__DB.CURSOR().execute('insert into USER_BANK_INFOS(USER_ID, ADD_SAVINGS, SAVINGS, STIPEND, BUDGET_NEEDS, BUDGET_WANTS) values (%s, %s, %s, %s, %s, %s)', (USER_ID, None, None, None, None, None))