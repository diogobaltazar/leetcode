#!/usr/bin/env python3
"""
Test runner for LeetCode exercises.

Usage:
    python run_tests.py                # Run all tests
    python run_tests.py arrays         # Run tests for a specific category
    python run_tests.py arrays.max_value  # Run tests for a specific exercise
"""
import unittest
import sys
import os

def run_tests(test_path=None):
    """
    Run tests based on the provided path.
    
    Args:
        test_path: Optional path to specific tests to run.
                  Format: 'category' or 'category.exercise'
    """
    if test_path is None:
        # Run all tests
        test_suite = unittest.defaultTestLoader.discover('tests')
    elif '.' in test_path:
        # Run tests for a specific exercise
        category, exercise = test_path.split('.')
        test_module = f'tests.{category}.test_{exercise}'
        test_suite = unittest.defaultTestLoader.loadTestsFromName(test_module)
    else:
        # Run tests for a specific category
        test_suite = unittest.defaultTestLoader.discover(f'tests/{test_path}')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    return result.wasSuccessful()

if __name__ == "__main__":
    # Get the test path from command line arguments
    test_path = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Run the tests
    success = run_tests(test_path)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)
