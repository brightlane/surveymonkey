import os
import re
import random
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Configuration
AFFILIATE_URL = "https://get.surveymonkey.com/mla48zxbil0q-yspnvs"
BASE_URL = "https://brightlane.github.io/surveymonkey"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def load_keywords():
    if not os.path.exists("keywords.txt"):
        return ["Customer Satisfaction", "Employee Engagement", "Market Research Form"]
    with open("keywords.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_dynamic_variations(keyword):
    """Generates context-rich variations to destroy duplicate content flags."""
    hooks = [
        f"Unlock powerful data-driven growth using professional-grade {keyword} structures.",
        f"Stop guessing what your audience thinks. Deploy advanced {keyword} panels natively in seconds.",
        f"Get crystal clear analytics visibility. Capture verified data tracks optimized for {keyword} workflows."
    ]
    
    benefit_titles_1 = ["Certified AI Logic", "Enterprise-Grade Scale", "Advanced Branching Architecture"]
    benefit_desc_1 = [
        f"Eliminate questionnaire bias. Built-in smart logic optimizes response validation paths for {keyword}.",
        f"Distribute templates effortlessly across email, secure URLs, web embeds, or SMS infrastructure tracks.",
        f"Keep form flow natural. Use predictive question skipping matrices tailored for high completion rates."
    ]
    
    benefit_titles_2 = ["Real-Time Metrics", "Instant Visual Dashboards", "Automated Compliance Auditing"]
    benefit_desc_2 = [
        f"Convert raw text into visual feedback summaries instantly. Cross-tabulate {keyword} data points natively.",
        f"Export ready-to-share graphics directly to stakeholders or management teams with zero manual scrubbing.",
        f"Secure, data-compliant infrastructure ensures information routing stays encrypted from end to end."
    ]

    return {
        "hook": random.choice(hooks),
        "t1": random.choice(benefit_titles_1),
        "d1": random.choice(benefit_desc_1),
        "t2": random.choice(benefit_titles_2),
        "d2": random.choice(benefit_desc_2),
    }

def generate_page_html(keyword, slug):
    v = get_dynamic_variations(keyword)
    title = f"Free {keyword} Templates & Form Builders | SurveyMonkey"
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Deploy professional {keyword} tools instantly. Access expert-certified forms, drag-and-drop mechanics, and custom analytic insights.">
    <link rel="canonical" href="{BASE_URL}/pages/{slug}.html">
    <style>
        :root {{ --primary: #00BF6F; --dark: #1E293B; --muted: #64748B; --bg-light: #F8FAFC; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: var(--dark); line-height: 1.6; margin: 0; padding: 0; }}
        header {{ padding: 1.25rem 2rem; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; background: #fff; }}
        .logo {{ font-size: 1.4rem; font-weight: 700; text-decoration: none; color: var(--dark); }}
        .logo span {{ color: var(--primary); }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 0 1.5rem; }}
        .hero {{ padding: 5rem 0 4rem; text-align: center; background: linear-gradient(180deg, #F0FDF4 0%, #FFF 100%); }}
        h1 {{ font-size: 3rem; font-weight: 800; letter-spacing: -0.02em; line-height: 1.2; margin-bottom: 1.5rem; }}
        h1 span {{ color: var(--primary); }}
        .hero p {{ font-size: 1.25rem; color: var(--muted); max-width: 750px; margin: 0 auto 2.5rem; }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 1rem 2.25rem; font-weight: 600; text-decoration: none; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,191,111,0.25); transition: background 0.2s; }}
        .btn:hover {{ background: #009e5b; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem; margin: 4rem 0; }}
        .card {{ padding: 2rem; border: 1px solid #E2E8F0; border-radius: 8px; background: #fff; }}
        .card h3 {{ font-size: 1.3rem; margin-bottom: 1rem; color: var(--dark); }}
        .card p {{ color: var(--muted); font-size: 0.95rem; }}
        .faq-section {{ background: var(--bg-light); padding: 4rem 0; text-align: left; border-top: 1px solid #E2E8F0; }}
        .faq-box {{ max-width: 800px; margin: 0 auto; }}
        .faq-item {{ background: #fff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1rem; border: 1px solid #E2E8F0; }}
        .faq-item h4 {{ font-size: 1.1rem; margin-bottom: 0.5rem; }}
        footer {{ background: var(--dark); color: #94A3B8; padding: 3rem 0; text-align: center; font-size: 0.85rem; }}
    </style>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "How long does it take to deploy an optimized {keyword} template?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Using our pre-built setups, your professional {keyword} campaign tracking links can be configured, structured, and deployed live to your audience targets in under 60 seconds."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Can I test the survey logic channels for free?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Yes, basic accounts permit total template structuring, questions management, and live responses capturing completely free of charge."
          }}
        }}
      ]
    }}
    </script>
</head>
<body>
    <header>
        <a href="../" class="logo">bright<span>lane</span></a>
        <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn" style="padding: 0.6rem 1.2rem; font-size: 0.95rem;">Build Free</a>
    </header>
    
    <section class="hero">
        <div class="container">
            <h1>Deploy Specialized Templates For <br><span>{keyword}</span></h1>
            <p>{v["hook"]}</p>
            <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn">Create Your {keyword} Form Free</a>
        </div>
    </section>

    <div class="container">
        <section class="grid">
            <div class="card">
                <h3>{v["t1"]}</h3>
                <p>{v["d1"]}</p>
            </div>
            <div class="card">
                <h3>{v["t2"]}</h3>
                <p>{v["d2"]}</p>
            </div>
            <div class="card">
                <h3>High Conversion Yields</h3>
                <p>Maximize layout responses using responsive, user-friendly CSS elements styled specifically to reduce desktop and mobile question bounce metrics.</p>
            </div>
        </section>
    </div>

    <section class="faq-section">
        <div class="container">
            <div class="faq-box">
                <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                <div class="faq-item">
                    <h4>Is this specific tool framework certified for {keyword}?</h4>
                    <p>Yes. Every single asset component passes structural analytical verification models, ensuring your data tracking endpoints match premium research standards.</p>
                </div>
                <div class="faq-item">
                    <h4>Can I export the response files into external data layers?</h4>
                    <p>Absolutely. Information sets collected through these pathways stream neatly into CSV layouts, spreadsheets, databases, or native custom report grids.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2026 brightlane. Independent properties tracking operational digital deployment metrics channels.</p>
        </div>
    </footer>
</body>
</html>"""

def build_sitemap(pages):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    root_url = ET.SubElement(urlset, "url")
    ET.SubElement(root_url, "loc").text = f"{BASE_URL}/"
    ET.SubElement(root_url, "changefreq").text = "daily"
    ET.SubElement(root_url, "priority").text = "1.0"

    for page in pages:
        url_node = ET.SubElement(urlset, "url")
        ET.SubElement(url_node, "loc").text = f"{BASE_URL}/pages/{page}"
        ET.SubElement(url_node, "changefreq").text = "weekly"
        ET.SubElement(url_node, "priority").text = "0.8"

    xml_str = ET.tostring(urlset, encoding="utf-8")
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print("✓ sitemap.xml updated perfectly.")

def main():
    os.makedirs("pages", exist_ok=True)
    keywords = load_keywords()
    generated_files = []

    print(f"Compiling {len(keywords)} dynamic search target funnels...")
    for kw in keywords:
        slug = slugify(kw)
        filename = f"{slug}.html"
        html_content = generate_page_html(kw, slug)
        
        with open(os.path.join("pages", filename), "w", encoding="utf-8") as f:
            f.write(html_content)
        generated_files.append(filename)

    build_sitemap(generated_files)
    print("✓ Architecture deployment complete without repository bloating.")

if __name__ == "__main__":
    main()
