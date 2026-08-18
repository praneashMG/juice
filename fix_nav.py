import os, re

d = r'd:\Juicora'

new_desktop_nav = """<a href="about.html" class="nav-link">About Us</a>
                    <a href="menu.html" class="nav-link">Our Menu</a>
                    <a href="smoothies.html" class="nav-link">Smoothies</a>
                    <a href="juices.html" class="nav-link">Fresh Juices</a>
                    <a href="gallery.html" class="nav-link">Gallery</a>
                    <a href="contact.html" class="nav-link">Contact</a>"""

new_mobile_nav = """<a href="about.html" class="block text-primary-text font-semibold text-lg py-2">About Us</a>
                <a href="menu.html" class="block text-primary-text font-semibold text-lg py-2">Our Menu</a>
                <a href="smoothies.html" class="block text-primary-text font-semibold text-lg py-2">Smoothies</a>
                <a href="juices.html" class="block text-primary-text font-semibold text-lg py-2">Fresh Juices</a>
                <a href="gallery.html" class="block text-primary-text font-semibold text-lg py-2">Gallery</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>"""

for f in os.listdir(d):
    if not f.endswith('.html'): continue
    p = os.path.join(d, f)
    with open(p, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Desktop Nav Replace
    pattern_desktop = re.compile(r'<a href="about\.html"[^>]*nav-link[^>]*>About Us</a>.*?<a href="contact\.html"[^>]*nav-link[^>]*>Contact</a>', re.DOTALL)
    content = pattern_desktop.sub(new_desktop_nav, content)
    
    # Mobile Nav Replace
    pattern_mobile = re.compile(r'<a href="about\.html"[^>]*block[^>]*>About Us</a>.*?<a href="contact\.html"[^>]*block[^>]*>Contact</a>', re.DOTALL)
    content = pattern_mobile.sub(new_mobile_nav, content)
    
    with open(p, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Navbars updated robustly.")
