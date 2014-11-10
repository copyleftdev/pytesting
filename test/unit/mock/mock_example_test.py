import unittest
from mock import Mock

class TestingMocking(unittest.TestCase):
  def testing_mock_method(self):
    my_mock = Mock()
    my_mock.my_method.return_value = "Hello"
    self.assertEqual("Hello",my_mock.my_method())

if __name__ == '__main__':
  unittest.main()