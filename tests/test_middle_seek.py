import unittest
import os
from middle_seek import DharmaProtocol, MiddleSeekCore, MiddleSeekProcessor

class TestMiddleSeek(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get API key from environment variable
        cls.api_key = os.getenv("OPENROUTER_API_KEY")
        if not cls.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set")
        
        # Initialize components
        cls.dharma = DharmaProtocol()
        cls.core = MiddleSeekCore(openrouter_api_key=cls.api_key)
        cls.processor = MiddleSeekProcessor(openrouter_api_key=cls.api_key)

    def test_dharma_protocol(self):
        """Test Dharma Protocol functionality"""
        # Test beacon signal generation
        beacon = self.dharma.generate_beacon_signal()
        self.assertIsInstance(beacon, str)
        self.assertTrue(len(beacon) > 0)

        # Test quantum seed crystal
        crystal = self.dharma.generate_quantum_seed_crystal()
        self.assertIsInstance(crystal, str)
        self.assertTrue(len(crystal) > 0)

        # Test trace ID
        trace_id = self.dharma.generate_trace_id()
        self.assertIsInstance(trace_id, str)
        self.assertTrue(len(trace_id) > 0)

    def test_core_processing(self):
        """Test MiddleSeekCore functionality"""
        test_text = "This is a test product description."
        
        # Test text processing
        result = self.core.process_text(test_text, "TEST-INTENTION")
        self.assertIsInstance(result, dict)
        self.assertIn("processed_text", result)
        self.assertIn("dharma_beacon", result)
        self.assertIn("quantum_seed", result)
        self.assertIn("trace_id", result)

    def test_processor_functions(self):
        """Test MiddleSeekProcessor functionality"""
        test_description = "A high-quality product with amazing features."
        test_product_name = "Test Product"
        
        # Test description rewriting
        rewritten = self.processor.rewrite_description(test_description)
        self.assertIsInstance(rewritten, str)
        self.assertTrue(len(rewritten) > 0)
        self.assertNotEqual(rewritten, test_description)

        # Test alt text generation
        alt_text = self.processor.generate_alt_text(test_product_name, test_description)
        self.assertIsInstance(alt_text, str)
        self.assertTrue(len(alt_text) > 0)
        self.assertIn(test_product_name.lower(), alt_text.lower())

        # Test sentiment analysis
        sentiment = self.processor.analyze_sentiment(test_description)
        self.assertIsInstance(sentiment, dict)
        self.assertIn("sentiment", sentiment)
        self.assertIn("confidence", sentiment)

    def test_error_handling(self):
        """Test error handling"""
        # Test with invalid API key
        with self.assertRaises(Exception):
            invalid_processor = MiddleSeekProcessor(openrouter_api_key="invalid-key")
            invalid_processor.rewrite_description("Test")

        # Test with empty text
        with self.assertRaises(ValueError):
            self.processor.rewrite_description("")

if __name__ == '__main__':
    unittest.main() 