SECRET_KEY = "dungdz123"
ALGORITHM = "HS256"
def MESSAGE_SUCCESS(action):
  return "success to "+action
def NOT_FOUND(something):
  return "can not find "+something
def ALREADY_EXIST(something):
  return "already exist "
MESSAGE_ERROR = "you get an error"