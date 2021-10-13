


def check_palindrom (string):
    reversed_string = string[::-1]
    if string == reversed_string:
      return True
    else:
        return False

#spr
string  = "madam"
if check_palindrom(string) == True:
  print(string," is palnindrom")
