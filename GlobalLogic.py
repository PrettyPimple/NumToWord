from NumericalWords import *

class CurrencyToWords:
    def __init__(self, lang, num):
        self.intLang = int(lang)
        try:
            if "," in num:
                tryNum = num.replace(",", ".")
                fNum = float(tryNum)
            else:
                fNum = float(num)
        except Exception as e:
            print(e+"\nUncorrect inputed chars!")
        self.num = num
        self.word = str(num)
        self.lenWord = len(self.word)


    def getEngHundreds(self,partWord, poryadok):
        hundreds = ""
        decimals = ""
        if partWord[0] != "0":
            hundreds = toTen[0][int(partWord[0])] + "hundred "
        if partWord[1] == "1":
            decimals = underTwenty[0][int(partWord[2])]
        elif partWord[1] != "0" or (partWord[1] == "1" and partWord[2] == "0"):
            if partWord[2] == "0":
                change = underHundred[0][int(partWord[1])].replace("-", " ")
                decimals = change + toTen[0][int(partWord[2])]
            else:
                decimals = underHundred[0][int(partWord[1])] + toTen[0][int(partWord[2])]

        elif partWord[1] == "0":
            decimals = toTen[0][int(partWord[2])]
        return hundreds + decimals

    def getSlavicHundreds(self, partWord, poryadok):
        hundreds = ""
        decimals = ""
        if partWord[0] != "0":
            hundreds = overHundred[self.intLang - 1][int(partWord[0])]
        if partWord[1] == "1":
            decimals = underTwenty[self.intLang - 1][int(partWord[2])]
        elif partWord[1] != "0":
            if partWord[2] == "0":
                decimals = underHundred[self.intLang - 1][int(partWord[1])] + toTen[self.intLang - 1][poryadok][
                    int(partWord[2])]
            else:
                decimals = underHundred[self.intLang - 1][int(partWord[1])] + toTen[self.intLang - 1][poryadok][
                    int(partWord[2])]
        elif partWord[1] == "0":
            decimals = toTen[self.intLang - 1][poryadok][int(partWord[2])]

        if (hundreds + decimals) == "тисяч " or (hundreds + decimals) == "мільйонів " or (
                hundreds + decimals) == "мільярдів ":
            return ""
        else:
            return hundreds + decimals

    def getHundreds(self, partWord, poryadok):
        if self.intLang == 1:
             return self.getEngHundreds(partWord, poryadok)
        else:
             return self.getSlavikHundreds(partWord, poryadok)


    def getPennies(self, partWord):
        if self.intLang == 1:
            return self.getEngPennies(partWord)
        else:
            return self.getSlavicPennies(partWord)

    def getEngPennies(self, partWord):
        result = self.getHundreds("0" + partWord[0:2], 0)
        if result == "":
            return ""
        elif result == "one ":
            return result + "cent"
        else:
            return result + "cents"

    def getSlavicPennies(self, partWord):
        result = self.getSlavicHundreds("0" + partWord[0:2], 0)
        if result == "":
            return ""
        elif partWord[1] == "1":
            return result + "копійка"
        elif partWord[1] >= "2" and partWord[1] <= "4":
            return result + "копійки"
        else:
            return result + "копійок"


    def getResult(self):
        if self.intLang == 1:
            return self.getEngResult()
        else:
            return self.getSlavicResult()

    def getEngResult(self):
        result = ""
        remain = self.lenWord % 3
        poryadok = 0
        for i in range(self.lenWord - 3, 0, -3):
            try:
                result = self.getHundreds(self.word[i - 3:i], 0) + overHundred[0][poryadok] + result
            except IndexError:
                if remain == 1:
                    result = self.getHundreds("00" + self.word[0], 0) + overHundred[0][poryadok] + result
                else:
                    result = self.getHundreds("0" + self.word[0:2], 0) + overHundred[0][poryadok] + result
            poryadok += 1
        if result == "":
            return ""
        elif result == "one ":
            return result + "dollar "
        else:
            return result + "dollars "

    def getSlavicResult(self):
        result = ""
        remain = self.lenWord % 3
        poryadok = 0
        for i in range(self.lenWord - 3, 0, -3):
            try:
                result = self.getSlavicHundreds(self.word[i - 3:i], poryadok) + result
            except IndexError:
                if remain == 1:
                    result = self.getSlavicHundreds("00" + self.word[0], poryadok) + result
                else:
                    result = self.getSlavicHundreds("0" + self.word[0:2], poryadok) + result
            poryadok += 1
        if result == "":
            return ""
        elif self.word[-4] == "1":
            return result + "гривня "
        elif self.word[-4] >= "2" and self.word[-4] <= "4":
            return result + "гривні "
        else:
            return result + "гривень "


    def getNumberInWords(self):
        if self.intLang == 1:
            return self.getNumberInEngWords()
        else:
            return self.getNumberInSlavicWords()

    def getNumberInEngWords(self):
        if (self.getResult() != "") and (self.getPennies(self.word[-2:self.lenWord]) != ""):
            return self.getResult() + "and " + self.getPennies(self.word[-2:self.lenWord])
        elif self.getResult() == "" and self.getPennies(self.word[-2:self.lenWord]) == "":
            return "zero"
        else:
            return self.getResult() + self.getPennies(self.word[-2:self.lenWord])


    def getNumberInSlavicWords(self):
        if (self.getSlavicResult() != "") and (self.getSlavicPennies(self.word[-2:self.lenWord]) != ""):
            return self.getSlavicResult() + "і " + self.getSlavicPennies(self.word[-2:self.lenWord])
        elif self.getSlavicResult() == "" and self.getSlavicPennies(self.word[-2:self.lenWord]) == "":
            return "нуль"
        else:
            return self.getSlavicResult() + self.getSlavicPennies(self.word[-2:self.lenWord])

if __name__ == "__main__":
    ob = CurrencyToWords(input("Select language:\n1)English;\n2)Ukrainian;\n"), input("Input number:\n"))
    print(ob.getNumberInWords())