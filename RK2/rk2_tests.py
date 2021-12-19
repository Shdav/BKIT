import unittest
import rk2

class tests(unittest.TestCase):
    def test1(self):
        ans = [
            ("Condition", 273, 'Python'),
            ("Semicolon", 3, 'R')
        ]
        self.assertEqual(rk2.test_1(rk2.SynConstrs, rk2.Langs), ans)

    def test2(self):
        ans = [
            ('Java', 381.0),
            ('C#', 253.0), 
            ('Python', 173.0), 
            ('JavaScript', 145.0), 
            ('C++', 11.0), 
            ('R', 3.0)
        ]
        self.assertEqual(rk2.test_2(rk2.SynConstrs, rk2.Langs), ans)

    def test3(self):
        ans = {
            'C++': ['Condition', 'Loop', 'Shift', 'Add', 'Mul', 'Semicolon', 'Array'],
            'C#': ['Condition', 'Loop', 'Shift', 'Add', 'Mul', 'Semicolon', 'Array']
            }
        self.assertEqual(rk2.test_3(rk2.SynConstrs, rk2.Langs, rk2.SCPLs), ans)

if __name__ == "__main__":
    unittest.main()