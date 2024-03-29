import time
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

class BadWordException(Exception):
    def __init__(self, badword):
        Exception.__init__(self)
        self.badword = badword

class LongInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.atleast = atleast
        self.length = length

badwords = ('fuck', 'bitch', 'cyka', 'naxui','naked')

try :
    text = input("Enter a string : ").strip(' ')
    if len(text) > 10 & len(text) < 5:
        raise ShortInputException(len(text), 3)
    if len(text) > 10:
        raise LongInputException(len(text),10)
    for badword in badwords:
        if text.lower().find(badword) != -1:
            raise BadWordException(badword)
except BadWordException as ex:
    print("BadWordException: You have used a badword : {} ".format(ex.badword))
except ShortInputException as ex:
    print("ShortInputException: Your entered string was too small. Should be atleast {}".format(ex.atleast))

except LongInputException as ex:
    print("LongInputException: Your entered string was too long.Should be atleast {}".format(ex.atleast))


time.sleep(5)
input("Press any key to exit...")