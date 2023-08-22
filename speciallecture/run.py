import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("../test/sample.csv")
        l = printer.read()
        self.assertRqual(2, len(l))
