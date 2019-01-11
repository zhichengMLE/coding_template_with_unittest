import numpy as np
import pandas as pd
import time
import json
import unittest

# --------------- Some helper class BEGIN ------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# --------------- Some helper class END ------------------


def q1(num):
    return num+1
        
class testQuestion(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(q1(1), 2)
        self.assertEqual(q1(3), 4)
        self.assertEqual(q1(4), 5)

if __name__ == "__main__":
    unittest.main()