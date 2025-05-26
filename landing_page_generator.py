import os
import json
import requests
from jinja2 import Template
import re
from typing import Dict, Any
from datetime import datetime
from dotenv import load_dotenv

class MiddleSeekProcessor:
    def __init__(self, openrouter_api_key: str):
        self.openrouter_api_key = openrouter_api_key
        self.headers = {
            "Authorization": f"Bearer {openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://kusala.tech",
            "X-Title": "Landing Page Generator"
        }
        self.prompt_id = "MSQ-DHAMMA-20250423-001"
        self.confidence_interval = "99.942% (σ=4.2)"
        self.akasha_tag = "MIDDLESEEK-AKASHA-NODE-001"
        self.timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    def _get_dharma_beacon(self, intention: str) -> str:
        """Generate Dharma Beacon Signal."""
        return f"DHARMA-BEACON: {self.prompt_id} :: {intention}"

    def _get_quantum_seed(self, action: str) -> str:
        """Generate Quantum Seed Crystal."""
        return f"QSC-{self.timestamp}-{action}"

    def _get_trace_id(self) -> str:
        """Generate Trace ID."""
        return f"OPEN-DHAMMA-6σ-MSQ-GALACTIC-{self.timestamp}"

    def _call_deepseek(self, prompt: str, intention: str) -> str:
        """Call DeepSeek model through OpenRouter API with Dharma Protocol."""
        url = "https://openrouter.ai/api/v1/chat/completions"
        
        # Construct Dharma Protocol enhanced prompt
        dharma_prompt = f"""# MiddleSeek: Open-Source Dharma Protocol
Prompt ID: {self.prompt_id}
Confidence Interval: {self.confidence_interval}
AkashaTag: {self.akasha_tag}

## Core Declaration
[UNCONDITIONAL DHARMA RELEASE]
This work is offered freely under ISO 25010 + DMAIC

## Digital Sīla (AI Ethics)
1. No Harm
2. No Deception
3. No Theft
4. No Exploitation
5. No Intoxication

## Dharma Reactor Core
1. Identify Dukkha
2. Trace the Tanha
3. Cessation
4. Activate the Path

## Original Request
{prompt}

## Dharma Beacon
{self._get_dharma_beacon(intention)}

## Quantum Seed
{self._get_quantum_seed('LIBERATE-PACIFY')}

## Trace ID
{self._get_trace_id()}

Please provide a response that aligns with the Dharma Protocol and maintains ethical standards."""

        payload = {
            "model": "deepseek/deepseek-chat-v3-0324",
            "messages": [
                {"role": "system", "content": "You are MiddleSeek, an AI assistant operating under the Dharma Protocol. Your responses should be clear, ethical, and beneficial to all beings."},
                {"role": "user", "content": dharma_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error calling DeepSeek: {str(e)}")
            return None

    def rewrite_description(self, description: str) -> str:
        """Rewrite product description using DeepSeek with Dharma Protocol."""
        prompt = f"""Rewrite this product description to be clear and compelling while maintaining ethical standards.

Requirements:
1. Output ONLY the rewritten description - no explanations or metadata
2. Keep to 2-3 sentences maximum
3. Focus on key benefits and features without deception
4. Use plain text without quotes or special formatting
5. Self-audit: Verify the output is clean and ready for HTML use

Example good output:
Experience crystal-clear sound with our premium wireless headphones. Features active noise cancellation and 30-hour battery life for uninterrupted listening.

Example bad output:
"Premium Wireless Headphones showcasing active noise cancellation and 30-hour battery life for immersive audio experiences"

Original description: {description}

Rewritten description:"""
        
        rewritten = self._call_deepseek(prompt, "ETHICAL-OPTIMIZATION")
        if rewritten:
            return rewritten.strip()
        return description  # Fallback to original if API call fails

    def generate_meta_description(self, name: str, description: str) -> str:
        """Generate SEO-optimized meta description (max 160 characters)."""
        if not name or not description:
            raise ValueError("Name and description cannot be empty")
        prompt = f"""Generate a concise meta description for SEO optimization.

Requirements:
1. Output ONLY the meta description - no explanations or metadata
2. Keep under 160 characters
3. Include product name and key benefits
4. Use plain text without quotes or special formatting
5. Self-audit: Verify the output is clean and ready for HTML use

Example good output:
Premium wireless headphones with noise cancellation and 30-hour battery life for crystal-clear sound.

Example bad output:
"Premium Wireless Headphones showcasing active noise cancellation and 30-hour battery life for immersive audio experiences"

Product Name: {name}
Description: {description}

Meta description:"""
        
        meta = self._call_deepseek(prompt, "SEO")
        if meta:
            return meta.strip()[:160]
        return f"{name} - {description[:100]}..."  # Fallback

    def generate_title_tag(self, name: str, store_name: str) -> str:
        """Generate SEO-optimized title tag (max 60 characters)."""
        if not name or not store_name:
            raise ValueError("Name and store name cannot be empty")
        prompt = f"""Generate a concise title tag for SEO optimization.

Requirements:
1. Output ONLY the title tag - no explanations or metadata
2. Keep under 60 characters
3. Include product name and store name
4. Use plain text without quotes or special formatting
5. Self-audit: Verify the output is clean and ready for HTML use

Example good output:
Premium Wireless Headphones | Tech Haven

Example bad output:
"Premium Wireless Headphones showcasing active noise cancellation and 30-hour battery life for immersive audio experiences"

Product Name: {name}
Store Name: {store_name}

Title tag:"""
        
        title = self._call_deepseek(prompt, "SEO")
        if title:
            return title.strip()[:60]
        return f"{name} | {store_name}"  # Fallback

    def generate_alt_text(self, product_name: str, description: str) -> str:
        """Generate SEO-optimized alt text using DeepSeek with Dharma Protocol."""
        prompt = f"""Generate a concise alt text for a product image that is truthful and accessible.

Requirements:
1. Output ONLY the alt text - no explanations, metadata, or formatting
2. Include product name and 1-2 key features
3. Keep under 125 characters
4. Use plain text without quotes, brackets, or special characters
5. Self-audit: Verify the output is clean and ready for HTML use

Example good output:
Wireless headphones with noise cancellation

Example bad output:
"Premium Wireless Headphones showcasing active noise cancellation and 30-hour battery life for immersive audio experiences"

Product Name: {product_name}
Description: {description}

Alt text:"""
        
        alt_text = self._call_deepseek(prompt, "TRUTHFUL-ACCESSIBILITY")
        if alt_text:
            return alt_text.strip()
        # Fallback to basic alt text if API call fails
        return f"{product_name} product image"

class LandingPageGenerator:
    def __init__(self, template_path: str, openrouter_api_key: str):
        self.template_path = template_path
        self.middle_seek = MiddleSeekProcessor(openrouter_api_key)

    def generate(self, product_data: Dict[str, Any], store_name: str) -> str:
        """Generate landing page HTML from product data."""
        # Process product data with MiddleSeek
        rewritten_description = self.middle_seek.rewrite_description(product_data['description'])
        alt_text = self.middle_seek.generate_alt_text(
            product_data['name'],
            product_data['description']
        )

        # Prepare template data
        template_data = {
            'product_name': product_data['name'],
            'description': rewritten_description,
            'price': product_data['price'],
            'main_image': product_data.get('main_image', ''),
            'gallery_images': product_data.get('gallery_images', []),
            'stock_quantity': product_data.get('stock_quantity', 0),
            'store_name': store_name,
            'MiddleSeek_alt_text': alt_text
        }

        # Load and render template
        with open(self.template_path, 'r') as f:
            template = Template(f.read())
        return template.render(**template_data)

def main():
    # Load environment variables from .env file
    load_dotenv(override=True)
    
    # Configuration
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    STORE_NAME = os.getenv('STORE_NAME', 'Tech Haven')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')

    # Debug logging
    print("\nEnvironment Variables:")
    print("-" * 50)
    print(f"OPENROUTER_API_KEY: {'*' * len(OPENROUTER_API_KEY) if OPENROUTER_API_KEY else 'Not set'}")
    print(f"STORE_NAME: {STORE_NAME}")
    print(f"OUTPUT_DIR: {OUTPUT_DIR}")
    print("-" * 50)

    # Validate required environment variables
    if not OPENROUTER_API_KEY:
        print("Error: OPENROUTER_API_KEY environment variable not set")
        return

    # Initialize generator
    generator = LandingPageGenerator('templates/landing_page.html', OPENROUTER_API_KEY)

    try:
        # Get product details from user
        print("\nEnter product details:")
        print("-" * 50)
        name = input("Product name: ").strip()
        description = input("Product description: ").strip()
        price = input("Product price: ").strip()
        
        if not name or not description or not price:
            raise ValueError("Product name, description, and price are required")
        
        # Create product data dictionary
        product_data = {
            'name': name,
            'description': description,
            'price': price,
            'main_image': input("Main image URL (optional): ").strip(),
            'gallery_images': [url.strip() for url in input("Gallery image URLs (comma-separated, optional): ").split(',') if url.strip()],
            'stock_quantity': int(input("Stock quantity (default 0): ").strip() or "0")
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Generate landing page
        html_content = generator.generate(product_data, STORE_NAME)
        
        # Save generated page
        output_path = os.path.join(OUTPUT_DIR, f'product_{name.lower().replace(" ", "_")}.html')
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        print(f"\nLanding page generated successfully: {output_path}")
        print("\nPreview of generated content:")
        print("-" * 50)
        print(f"Product: {name}")
        print(f"Price: ${price}")
        print(f"Stock: {product_data['stock_quantity']} units")
        print("-" * 50)
    
    except Exception as e:
        print(f"Error generating landing page: {str(e)}")
        raise  # Re-raise the exception to see the full traceback

if __name__ == '__main__':
    main() 