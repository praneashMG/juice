import os, re
d = r'd:\Juicora'

old_svg_pattern = re.compile(r'<svg class="w-6 h-6" viewBox="0 0 100 100" fill="none" xmlns="http://www\.w3\.org/2000/svg">.*?<linearGradient id="logoPopGrad".*?</linearGradient>\s*</defs>\s*</svg>', re.DOTALL)

new_svg = """<svg class="w-6 h-6" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <!-- Cup Body -->
                        <path d="M 25 35 L 35 85 C 36 90 40 92 45 92 L 55 92 C 60 92 64 90 65 85 L 75 35 Z" fill="url(#juiceGrad)" stroke="var(--color-accent)" stroke-width="4" stroke-linejoin="round"/>
                        <!-- Cup Lid -->
                        <path d="M 20 35 C 20 25 80 25 80 35 Z" fill="#ffffff" stroke="var(--color-accent)" stroke-width="4" stroke-linejoin="round"/>
                        <!-- Straw -->
                        <path d="M 50 25 L 50 10 L 65 10" stroke="var(--color-accent-light)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                        <!-- Fruit Slice -->
                        <circle cx="25" cy="45" r="12" fill="#FFA726" stroke="#ffffff" stroke-width="2"/>
                        <circle cx="25" cy="45" r="9" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4 2"/>
                        <!-- Highlights -->
                        <path d="M 32 40 L 40 85" stroke="white" stroke-width="3" stroke-linecap="round" opacity="0.4"/>
                        <defs>
                            <linearGradient id="juiceGrad" x1="50" y1="90" x2="50" y2="35" gradientUnits="userSpaceOnUse">
                                <stop offset="0%" stop-color="#FF9800"/>
                                <stop offset="100%" stop-color="var(--color-accent)"/>
                            </linearGradient>
                        </defs>
                    </svg>"""

for f in os.listdir(d):
    if not f.endswith('.html'): continue
    p = os.path.join(d, f)
    with open(p, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = old_svg_pattern.sub(new_svg, content)
    
    if content != new_content:
        with open(p, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
