userList = [""]

def createUsername(first, last, id):
  username = ""
  #Your code for generating username
  #Username should follow format <first initial><last name (up to 6 letters)><last 3 digits of ID number>
  
  return username

def addUsers():
  global userList
  
  userList.append(createUsername("Johnathan", "Bostwick", "13112"))
  userList.append(createUsername("Eric", "Gray", "54182"))
  userList.append(createUsername("Danielle", "Kaps", "23325"))
  userList.append(createUsername("Ethan", "Newman", "22118"))
  userList.append(createUsername("McKenna", "Revis", "92814"))
  

addUsers()
print (userList)
