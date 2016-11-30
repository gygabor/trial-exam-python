import exercise4
import unittest

class Test_exercise4(unittest.TestCase):

    def test_working_with_string(self):
        self.assertTrue(exercise4.greeter('Joe'))

    def test_working_with_empty_string(self):
        self.assertTrue(exercise4.greeter(''))

    def test_working_with_number(self):
        self.assertTrue(exercise4.greeter(0))

    def test_return_with_good_value(self):
        self.assertEqual(exercise4.greeter('Joe'), 'Hello, Joe!')

    def test_return_with_good_value_emptystring(self):
        self.assertEqual(exercise4.greeter(''), 'Hello, Mr Nobody!')

    def test_exception_handling(self):
        self.assertRaises(TypeError, exercise4.greeter, 123)

if __name__ == '__main__':
    unittest.main()
