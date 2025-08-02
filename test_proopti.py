# test_proopti.py
"""
Tests for ProOpti module.
"""

import unittest
from proopti import ProOpti

class TestProOpti(unittest.TestCase):
    """Test cases for ProOpti class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProOpti()
        self.assertIsInstance(instance, ProOpti)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProOpti()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
