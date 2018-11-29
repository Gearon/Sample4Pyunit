import unittest
class suiteTest(unittest.TestCase):
   def setUp(self):
      self.a = 10
      self.b = 20 
      
   def testadd(self):
      """Add"""
      result = self.a+self.b
      self.assertTrue(result == 100)
   def testsub(self):
      """sub"""
      result = self.a-self.b
      self.assertTrue(result == -10)
      
if __name__ == '__main__':
   runner = unittest.TextTestRunner()
   loader = unittest.TestLoader()
   test_suite = unittest.TestSuite()
   test_suite.addTests(loader.loadTestsFromTestCase(suiteTest))
   runner.run (test_suite)