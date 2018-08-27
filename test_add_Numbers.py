import unittest
#from unittest import TestCase

import Main
from Main import Module_Test

class TestAdd_Numbers(unittest.TestCase):
    def test_Add_Numbers(self):
        var3 = Main.Module_Test.Add_Numbers(10, 12)
        self.assertEqual(22, var3)
        var3 = Module_Test.Add_Numbers(20, 32)
        self.assertEqual(52, var3)
        #self.fail()

    def test_Add_Numbers1(self):
        var3 = Main.Module_Test.Add_Numbers(32, 44)
        self.assertEqual(76, var3)
        var3 = Module_Test.Add_Numbers(78, 22)
        self.assertEqual(100, var3)

    def test_Subtract_Numbers(self):
        var3 = Main.Module_Test.Subtract_Numbers(32, 44)
        self.assertEqual(-12, var3)
        var3 = Module_Test.Subtract_Numbers(78, 22)
        self.assertEqual(56, var3)

if __name__ == '__main__':
    unittest.main()