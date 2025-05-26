import os
from dotenv import load_dotenv
from landing_page_generator import LandingPageGenerator

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Sample product data
    product_data = {
        "name": "DharmaComply: AI-Powered Compliance Suite",
        "description": """<div class="product-description">
<h1>DharmaComply: AI-Powered Compliance Suite</h1>

<div class="compliance-badges"><img alt="99.999% Accuracy" src="/badges/accuracy.svg" width="80" /> <img alt="ISO Certified" src="/badges/iso.svg" width="80" /> <img alt="Ethics Verified" src="/badges/ethics.svg" width="60" /> <img alt="Global Standards" src="/badges/global.svg" width="60" /></div>

<div class="product-meta">
<p><strong>License:</strong> Open Source with Commercial Options</p>

<p><strong>Support:</strong> Certified Compliance Experts ($150/hr)</p>
</div>

<div class="description-section">
<h2>Simplify Compliance with AI</h2>

<p>Automate your compliance across 37+ global regulations with our precision-engineered platform. Perfect for businesses that value both compliance and ethical technology.</p>

<div class="highlight-box">
<h3>Key Features</h3>

<ul>
	<li>Instant Audit Reports with Verified Evidence</li>
	<li>Self-Updating Policy Engine</li>
	<li>Ethical Impact Scoring</li>
	<li>Automated Data Privacy Requests</li>
</ul>

<p class="quote">"We make compliance simple, accurate, and ethical" — Our Team</p>
</div>
</div>

<div class="compliance-section">
<h2>Supported Regulations</h2>

<table class="compliance-table">
	<thead>
		<tr>
			<th>Standard</th>
			<th>Coverage</th>
			<th>Add-On Service</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GDPR (EU)</td>
			<td>Full Data Subject Rights</td>
			<td>DPO Support Package</td>
		</tr>
		<tr>
			<td>NIST (US)</td>
			<td>Complete AI Governance</td>
			<td>Gap Analysis</td>
		</tr>
		<tr>
			<td>ISO 27001</td>
			<td>Information Security</td>
			<td>Certification Prep</td>
		</tr>
		<tr>
			<td>PDPA (Thailand)</td>
			<td>Local Requirements</td>
			<td>Thai Language Setup</td>
		</tr>
	</tbody>
</table>
</div>

<div class="consulting-section">
<h2>Implementation Packages</h2>

<div class="service-tier">
<h3>Starter Package</h3>

<p><strong>$5,000</strong> | Includes:</p>

<ul>
	<li>Compliance Assessment</li>
	<li>Basic Configuration</li>
	<li>2 Training Sessions</li>
</ul>
</div>

<div class="service-tier">
<h3>Enterprise Package</h3>

<p><strong>$15,000</strong> | Adds:</p>

<ul>
	<li>Custom Workflows</li>
	<li>Audit Support</li>
	<li>Yearly Compliance Review</li>
</ul>
</div>
</div>

<div class="legal-section">
<h2>Important Information</h2>

<ol>
	<li>Open source version available under AGPLv3</li>
	<li>Commercial licenses include premium features</li>
	<li>Full compliance requires proper implementation</li>
</ol>

<p><a href="/compliance/dharmacomply-compliance-addenda?route=cms/blog.info">View Full Compliance Details</a></p>
</div>
</div>
<style type="text/css">.product-description {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  max-width: 900px;
  margin: 0 auto;
  color: #333;
  line-height: 1.6;
}

.compliance-badges {
  display: flex;
  gap: 15px;
  margin: 20px 0;
  justify-content: center;
}

.highlight-box {
  background-color: #f8f9fa;
  border-left: 4px solid #2c3e50;
  padding: 20px;
  margin: 25px 0;
}

.quote {
  font-style: italic;
  color: #666;
  margin-top: 15px;
}

.compliance-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
}

.compliance-table th {
  background-color: #2c3e50;
  color: white;
  padding: 12px;
  text-align: left;
}

.compliance-table td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

.service-tier {
  background-color: #f5f5f5;
  padding: 20px;
  margin: 15px 0;
  border-radius: 4px;
}

.service-tier h3 {
  margin-top: 0;
  color: #2c3e50;
}

a {
  color: #2980b9;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
""",
        "price": "Depends on Requirements",
        "main_image": "https://kusala.tech/image/cache/catalog/Screenshot%202568-05-26%20at%2017.23.53-500x500.png",
        "gallery_images": [
            "https://kusala.tech/image/cache/catalog/Screenshot%202568-05-26%20at%2017.23.44-800x800.png"
        ],
        "stock_quantity": 1
    }
    
    # Store configuration
    store_name = "Kusala Tech"
    
    # Get API key from environment
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set")
        print("Please create a .env file with your API key:")
        print("OPENROUTER_API_KEY=your-key-here")
        return
    
    try:
        # Initialize generator
        generator = LandingPageGenerator('templates/landing_page.html', openrouter_api_key)
        
        # Generate landing page
        html_content = generator.generate(product_data, store_name)
        
        # Save to output directory
        os.makedirs('output', exist_ok=True)
        output_path = os.path.join('output', 'dharmacomply.html')
        
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        print(f"Landing page generated successfully: {output_path}")
        print("\nPreview of generated content:")
        print("-" * 50)
        print(f"Product: {product_data['name']}")
        print(f"Price: ${product_data['price']}")
        print(f"Stock: {product_data['stock_quantity']} units")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error generating landing page: {str(e)}")

if __name__ == '__main__':
    main() 