import time
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

class LongInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.atleast = atleast
        self.length = length

class BadWordException(Exception):
    def __init__(self, badword):
        Exception.__init__(self)
        self.badword = badword

class SymbolException(Exception):
    def __init__(self,symbol):
        Exception.__init__(self)
        self.symbol = symbol

badwords = ('fuck', 'bitch', 'cyka', 'naxui','naked')
symbols = ('!', '@', '#', '$', '?')

try :
    text = input("Enter a string : ").strip(' ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    if len(text) > 10:
        raise LongInputException(len(text),10)
    for badword in badwords:
        if text.lower().find(badword) != -1:
            raise BadWordException(badword)
    for symbol in symbols:
        if text.lower().find(symbol) != -1:
            raise SymbolException(symbol)
except BadWordException as ex:
    print("BadWordException: You have used a badword : {} ".format(ex.badword))
except ShortInputException as ex:
    print("ShortInputException: Your entered string was too small. Should be atleast {}".format(ex.atleast))

except LongInputException as ex:
    print("LongInputException: Your entered string was too long.Should be atleast {}".format(ex.atleast))

except SymbolException as ex:
    print("SymbolException: Your entered string has include symbol.Should be atleast {}".format(ex.symbol))



time.sleep(5)
input("Press any key to exit...")