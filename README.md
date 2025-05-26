# Landing Page Generator

A dynamic landing page generator that creates SEO-optimized, accessible product pages using AI-powered content generation.

## Current Status

The project is currently in development with the following features:

- ✅ AI-powered content generation using OpenRouter API
- ✅ SEO-optimized meta descriptions and title tags
- ✅ Accessible alt text generation
- ✅ Responsive landing page template
- ✅ Dharma Protocol integration for ethical AI usage

OpenCart integration is planned for future development. For now, product data is manually provided through `test_generator.py`.

## Setup

1. Create a `.env` file in the project root with your OpenRouter API key:
```env
OPENROUTER_API_KEY=your-key-here
STORE_NAME=Your Store Name
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Currently, the generator is operated through `test_generator.py`. To create a landing page:

1. Open `test_generator.py`
2. Update the `product_data` dictionary with your product information:
```python
product_data = {
    "name": "Your Product Name",
    "description": "Your product description",
    "price": "Your price",
    "main_image": "URL to main product image",
    "gallery_images": [
        "URL to gallery image 1",
        "URL to gallery image 2"
    ],
    "stock_quantity": 1
}
```

3. Run the generator:
```bash
python test_generator.py
```

The generated landing page will be saved in the `output` directory.

## Features

- **AI-Powered Content**: Uses OpenRouter API to generate optimized product descriptions
- **SEO Optimization**: Automatically generates meta descriptions and title tags
- **Accessibility**: Generates meaningful alt text for images
- **Responsive Design**: Mobile-friendly landing page template
- **Ethical AI**: Implements Dharma Protocol for responsible AI usage

## Coming Soon

- OpenCart API integration
- Batch processing for multiple products
- Custom template support
- Additional AI models and options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the AGPLv3 License - see the LICENSE file for details. 