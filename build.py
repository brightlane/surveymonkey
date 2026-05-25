import os
import re
import random
from datetime import datetime
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

def load_keywords(filename="keywords.txt", default_list=None):
    if not os.path.exists(filename):
        return default_list or ["Customer Satisfaction"]
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_dynamic_variations(keyword):
    """Generates context-rich layout variations to kill duplicate content flags."""
    hooks = [
        f"Unlock powerful data-driven growth using professional-grade {keyword} structures.",
        f"Stop guessing what your audience thinks. Deploy advanced {keyword} panels natively in seconds.",
        f"Get crystal clear analytics visibility. Capture verified data tracks optimized for {keyword} workflows."
    ]
    return {"hook": random.choice(hooks)}

def generate_page_html(keyword, slug):
    v = get_dynamic_variations(keyword)
    title = f"Free {keyword} Templates & Form Builders | SurveyMonkey"
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Deploy professional {keyword} tools instantly. Access expert-certified forms, drag-and-drop layouts, and analytics.">
    <link rel="canonical" href="{BASE_URL}/pages/{slug}.html">
    <style>
        :root {{ --primary: #00BF6F; --dark: #1E293B; --muted: #64748B; --bg-light: #F8FAFC; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: var(--dark); line-height: 1.6; margin: 0; padding: 0; }}
        header {{ padding: 1.25rem 2rem; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; background: #fff; }}
        .logo {{ font-size: 1.4rem; font-weight: 700; text-decoration: none; color: var(--dark); }}
        .logo span {{ color: var(--primary); }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 0 1.5rem; }}
        .hero {{ padding: 5rem 0 4rem; text-align: center; background: linear-gradient(180deg, #F0FDF4 0%, #FFF 100%); }}
        h1 {{ font-size: 3rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 1.5rem; }}
        .hero p {{ font-size: 1.25rem; color: var(--muted); max-width: 700px; margin: 0 auto 2.5rem; }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 1rem 2.25rem; font-weight: 600; text-decoration: none; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,191,111,0.2); }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin: 4rem 0; text-align: left; }}
        .card {{ padding: 2rem; border: 1px solid #E2E8F0; border-radius: 8px; background: #fff; }}
        .faq-section {{ background: var(--bg-light); padding: 4rem 0; border-top: 1px solid #E2E8F0; }}
        .faq-box {{ max-width: 750px; margin: 0 auto; }}
        .faq-item {{ background: #fff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1rem; border: 1px solid #E2E8F0; }}
        footer {{ background: var(--dark); color: #94A3B8; padding: 2.5rem 0; text-align: center; font-size: 0.85rem; }}
    </style>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "How long does it take to deploy an optimized {keyword} layout?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Using our pre-built setups, your professional {keyword} campaign tracking links can be configured and deployed live to targets in under 60 seconds."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Can I test the survey logic channels for free?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Yes, basic accounts permit total template structuring and response capturing completely free of charge."
          }}
        }}
      ]
    }}
    </script>
</head>
<body>
    <header>
        <a href="../" class="logo">bright<span>lane</span></a>
        <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Start Free</a>
    </header>
    <main>
        <section class="hero">
            <div class="container">
                <h1>Deploy Specialized Templates For <br><span style="color:var(--primary);">{keyword}</span></h1>
                <p>{v["hook"]}</p>
                <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn">Create Your {keyword} Form Free</a>
            </div>
        </section>

        <div class="container">
            <section class="grid">
                <div class="card">
                    <h3>Certified Logic Rules</h3>
                    <p>Eliminate sample survey bias completely. Built-in smart logic optimizes response conversion verification paths globally.</p>
                </div>
                <div class="card">
                    <h3>Instant Visual Dashboards</h3>
                    <p>Convert raw data points into clear presentation decks natively. Clean your filtering streams with no manual calculations needed.</p>
                </div>
            </section>
        </div>

        <section class="faq-section">
            <div class="container">
                <div class="faq-box">
                    <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                    <div class="faq-item">
                        <h4>Is this template collection free?</h4>
                        <p>Yes. The standard starting engine configuration lets you test questions and run tracking funnels without upfront platform costs.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 brightlane. Independent tracking properties channel.</p>
    </footer>
</body>
</html>"""

def generate_blog_html(title, slug, random_internal_landing=None):
    """Generates a unique informational article with randomized structural phrasing matrix to block duplication penalties."""
    today_str = datetime.now().strftime("%B %d, %Y")
    
    intros = [
        f"Optimizing metrics for modern workflows requires a distinct strategy. Exploring how to build {title} establishes clear paths toward actionable insights.",
        f"When scaling modern organizational feedback, tracking issues related to {title} remains critical. Deploying clear testing structures ensures higher structural data integrity.",
        f"Data analytics shifts rapidly. Understanding the primary mechanics underneath {title} lets implementation teams isolate high-value user behaviors safely."
    ]
    
    body_p1 = [
        "When engineering modern web data layouts, lowering user friction must remain the primary goal. Complex, multi-page frameworks frequently cause significant drop-off spikes. By contrast, utilizing highly responsive drag-and-drop structural elements keeps completion rates predictable and clean.",
        "Maximizing response quality requires dropping decorative UI bottlenecks. When form systems load instantly across both mobile and desktop screens, data sets show lower bounce anomalies. Prioritizing layout accessibility consistently converts casual impressions into clean transactional answers."
    ]
    
    body_p2 = [
        "Furthermore, processing raw data streams requires native, immediate integration paths. Filtering database values through an automated dashboard removes human error variables. Teams can cleanly route completed inputs into tracking metrics panels to update strategic systems instantly.",
        "Equally important is the underlying compliance infrastructure. Encrypting data points along transit pipelines ensures consumer information privacy rules are safely met. Strong structural architectures let business components execute large-scale outreach tests with total regulatory confidence."
    ]

    internal_link_html = ""
    if random_internal_landing:
        landing_slug = slugify(random_internal_landing)
        internal_link_html = f'<p style="margin-top:2rem;">Looking for direct production blueprints? Explore our complete toolkit guide for <a href="../pages/{landing_slug}.html" style="color:var(--primary); font-weight:600;">{random_internal_landing} Solutions</a>.</p>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | brightlane Insights</title>
    <meta name="description" content="Expert look at {title}. Read our full operational guide on running data collection systems efficiently.">
    <link rel="canonical" href="{BASE_URL}/blog/{slug}.html">
    <style>
        :root {{ --primary: #00BF6F; --dark: #1E293B; --muted: #64748B; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: var(--dark); line-height: 1.7; margin: 0; padding: 0; }}
        header {{ padding: 1.25rem 2rem; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; }}
        .container {{ max-width: 700px; margin: 0 auto; padding: 3rem 1.5rem; }}
        .meta {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }}
        .cta-box {{ background: #F8FAFC; border: 1px solid #E2E8F0; padding: 2.5rem; border-radius: 8px; margin-top: 3.5rem; text-align: center; }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 0.85rem 1.75rem; text-decoration: none; border-radius: 6px; font-weight: 600; margin-top: 1.25rem; }}
    </style>
</head>
<body>
    <header>
        <a href="../" style="font-size:1.4rem; font-weight:700; text-decoration:none; color:var(--dark);">bright<span style="color:var(--primary);">lane</span></a>
    </header>
    <main class="container">
        <div class="meta">Published on {today_str} • Data Strategy Group</div>
        <h1>{title}</h1>
        
        <p style="font-size:1.15rem; color:#475569; margin: 1.5rem 0 2rem;">{random.choice(intros)}</p>
        
        <h2>System Data Integrity</h2>
        <p>{random.choice(body_p1)}</p>
        
        <h2>Advanced Analytical Frameworks</h2>
        <p>{random.choice(body_p2)}</p>

        {internal_link_html}

        <div class="cta-box">
            <h3>Optimize Your Current Metrics Infrastructure</h3>
            <p>Access ready-to-launch templates and scale custom collection channels seamlessly.</p>
            <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn">Get Started with SurveyMonkey Free</a>
        </div>
    </main>
</body>
</html>"""

def build_unified_sitemap(pages, posts):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    root_url = ET.SubElement(urlset, "url")
    ET.SubElement(root_url, "loc").text = f"{BASE_URL}/"
    ET.SubElement(root_url, "changefreq").text = "daily"
    ET.SubElement(root_url, "priority").text = "1.0"

    for p in pages:
        u = ET.SubElement(urlset, "url")
        ET.SubElement(u, "loc").text = f"{BASE_URL}/pages/{p}"
        ET.SubElement(u, "changefreq").text = "weekly"
        ET.SubElement(u, "priority").text = "0.8"

    for b in posts:
        u = ET.SubElement(urlset, "urlset")  # Fallback map element
        u = ET.SubElement(urlset, "url")
        ET.SubElement(u, "loc").text = f"{BASE_URL}/blog/{b}"
        ET.SubElement(u, "changefreq").text = "daily"
        ET.SubElement(u, "priority").text = "0.9"

    xml_str = ET.tostring(urlset, encoding="utf-8")
    parsed_xml = minidom.parseString(xml_str)
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(parsed_xml.toprettyxml(indent="  "))
    print("✓ Sitemap synchronized perfectly.")

def main():
    os.makedirs("pages", exist_ok=True)
    os.makedirs("blog", exist_ok=True)
    
    # 1. Compile/Refresh Landing Directory (100 High-Intent Keyword Funnels)
    keywords = load_keywords("keywords.txt", ["Customer Matrix", "Employee Feedback Form"])
    pages_list = []
    for kw in keywords:
        slug = slugify(kw)
        with open(os.path.join("pages", f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(generate_page_html(kw, slug))
        pages_list.append(f"{slug}.html")

    # 2. Compile Daily Variable Informational Blog Post
    blog_topics = load_keywords("blog_topics.txt", ["How to Track Customer Loyalty Metrics Successfully"])
    
    if blog_topics:
        current_topic = blog_topics[0]
        blog_slug = slugify(current_topic)
        
        # Pull a random landing-page keyword to weave an internal link silo
        random_link_target = random.choice(keywords) if keywords else None
        
        with open(os.path.join("blog", f"{blog_slug}.html"), "w", encoding="utf-8") as f:
            f.write(generate_blog_html(current_topic, blog_slug, random_link_target))
        print(f"✓ Randomized blog post generated: '{current_topic}' linked to '{random_link_target}'")

    # Sync all assets to unified map
    all_blog_posts = [f for f in os.listdir("blog") if f.endswith(".html")]
    build_unified_sitemap(pages_list, all_blog_posts)

if __name__ == "__main__":
    main()
