


def check_palindrom (string):
    if string == string[::-1]:
      return True
    return False

#spr
string  = "madam"
if check_palindrom(string) == True:
  print(string," is palnindrom")
