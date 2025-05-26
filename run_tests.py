import os
import sys
import unittest

def main():
    # Ensure the parent directory is in the Python path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    # Check for API key
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable not set")
        print("Please set it using:")
        print("export OPENROUTER_API_KEY='your-key-here'")
        sys.exit(1)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate status code
    sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    main() 