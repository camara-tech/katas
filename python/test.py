import unittest
import main as kata

class TestKarateChop(unittest.TestCase):
	
	def test_chop(self):
		self.assertEqual(0,kata.chop(5,[5,3,6,4]))
		self.assertEqual(2,kata.chop(6,[5,3,6,4]))
		self.assertEqual(-1,kata.chop(7,[5,3,6,4]))
		


if __name__ == '__main__':
	unittest.main()
