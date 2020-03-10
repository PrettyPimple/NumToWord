import GlobalLogic
import unittest

class TestCurrencyToWord(unittest.TestCase):
    def test_getNumberInWordsUa(self):
        ob = GlobalLogic.CurrencyToWords("2", "123,56")
        self.assertEqual(ob.getNumberInWords(), "сто двадцять три гривні і п'ятдесят шість копійок")
        ob2 = GlobalLogic.CurrencyToWords("2", "0,01")
        self.assertEqual(ob2.getNumberInWords(), "одна копійка")
        ob3 = GlobalLogic.CurrencyToWords("2", "1,00")
        self.assertEqual(ob3.getNumberInWords(), "одна гривня ")
        ob4 = GlobalLogic.CurrencyToWords("2", "1234567,89")
        self.assertEqual(ob4.getNumberInWords(), "один мільйон двісті тридцять чотири тисячі п'ятсот шістдесят сім гривень і вісімдесят дев'ять копійок")

    def test_getNumberInWordsEng(self):
        ob = GlobalLogic.CurrencyToWords("1", "1.00")
        self.assertEqual(ob.getNumberInWords(), "one dollar ")
        ob2 = GlobalLogic.CurrencyToWords("1", "1234567.89")
        self.assertEqual(ob2.getNumberInWords(), "one million two hundred thirty-four thousand five hundred sixty-seven dollars and eighty-nine cents")
        ob3 = GlobalLogic.CurrencyToWords("1", "0.01")
        self.assertEqual(ob3.getNumberInWords(), "one cent")
        ob4 = GlobalLogic.CurrencyToWords("1", "1234.12")
        self.assertEqual(ob4.getNumberInWords(),
                         "one thousand two hundred thirty-four dollars and twelve cents")


if __name__ == '__main__':
    unittest.main()