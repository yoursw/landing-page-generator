import unittest
import os
import json
from landing_page_generator import LandingPageGenerator, OpenCartAPI
from middle_seek import MiddleSeekProcessor

class TestLandingPageGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get API key from environment variable
        cls.openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        if not cls.openrouter_api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set")
        
        # Mock product data
        cls.mock_product = {
            "product_name": "Test Product",
            "description": "A high-quality product with amazing features.",
            "price": "99.99",
            "main_image": "https://example.com/images/main.jpg",
            "gallery_images": [
                "https://example.com/images/gallery1.jpg",
                "https://example.com/images/gallery2.jpg"
            ],
            "stock_quantity": 15
        }
        
        # Initialize components
        cls.generator = LandingPageGenerator('templates/landing_page.html', cls.openrouter_api_key)
        cls.store_name = "Test Store"

    def test_template_rendering(self):
        """Test that the template renders correctly with product data."""
        html_content = self.generator.generate(self.mock_product, self.store_name)
        
        # Check that all required elements are present
        self.assertIn(self.mock_product['product_name'], html_content)
        self.assertIn(self.mock_product['price'], html_content)
        self.assertIn(self.mock_product['main_image'], html_content)
        self.assertIn(self.store_name, html_content)
        
        # Check that gallery images are rendered
        for image in self.mock_product['gallery_images']:
            self.assertIn(image, html_content)
        
        # Check that stock alert is shown (since quantity < 20)
        self.assertIn(f"Only {self.mock_product['stock_quantity']} units remaining", html_content)

    def test_middle_seek_integration(self):
        """Test that MiddleSeek properly processes the content."""
        # Test description rewriting
        rewritten = self.generator.middle_seek.rewrite_description(self.mock_product['description'])
        self.assertIsInstance(rewritten, str)
        self.assertTrue(len(rewritten) > 0)
        self.assertNotEqual(rewritten, self.mock_product['description'])
        
        # Test alt text generation
        alt_text = self.generator.middle_seek.generate_alt_text(
            self.mock_product['product_name'],
            self.mock_product['description']
        )
        self.assertIsInstance(alt_text, str)
        self.assertTrue(len(alt_text) > 0)
        self.assertIn(self.mock_product['product_name'].lower(), alt_text.lower())

    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Test with empty product data
        with self.assertRaises(KeyError):
            self.generator.generate({}, self.store_name)
        
        # Test with missing required fields
        incomplete_product = self.mock_product.copy()
        del incomplete_product['product_name']
        with self.assertRaises(KeyError):
            self.generator.generate(incomplete_product, self.store_name)
        
        # Test with invalid price format
        invalid_product = self.mock_product.copy()
        invalid_product['price'] = "invalid"
        with self.assertRaises(ValueError):
            self.generator.generate(invalid_product, self.store_name)

    def test_output_directory(self):
        """Test that the output directory is created and file is saved."""
        output_dir = "test_output"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate and save the page
        html_content = self.generator.generate(self.mock_product, self.store_name)
        output_path = os.path.join(output_dir, "test_product.html")
        
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        # Verify file exists and contains content
        self.assertTrue(os.path.exists(output_path))
        with open(output_path, 'r') as f:
            saved_content = f.read()
            self.assertEqual(saved_content, html_content)
        
        # Cleanup
        os.remove(output_path)
        os.rmdir(output_dir)

if __name__ == '__main__':
    unittest.main() 