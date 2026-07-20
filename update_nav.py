import os, re

files = [f for f in os.listdir(".") if f.endswith(".html")]

def insert_products(content):
    # Desktop menu
    desktop_pattern = r"(<li class=""menu-item"">\s*<a\s*href=""services\.html""[\s\S]*?><span>02 /</span>SERVICES</a\s*>\s*</li>)"
    desktop_replacement = r"\1\n                    <li class=""menu-item"">\n                      <a\n                        href=""products.html""\n                        class=""item-link link text-caption""\n                        ><span>03 /</span>PRODUCTS</a\n                      >\n                    </li>"
    content = re.sub(desktop_pattern, desktop_replacement, content)
    
    # Change 03 to 04 and 04 to 05
    content = re.sub(r"<span>03 /</span>ABOUT", "<span>04 /</span>ABOUT", content)
    content = re.sub(r"<span>04 /</span>CONTACT", "<span>05 /</span>CONTACT", content)

    # Version-2 menu
    v2_pattern = r"(<li> <a href=""services\.html"" class=""link text-caption"">SERVICES</a></li>)"
    v2_replacement = r"\1\n                                <li> <a href=""products.html"" class=""link text-caption"">PRODUCTS</a></li>"
    content = re.sub(v2_pattern, v2_replacement, content)
    
    v2_footer = r"(<a href=""services\.html"" class=""link"">SERVICES</a>)"
    v2_footer_repl = r"\1\n                    <a href=""products.html"" class=""link"">PRODUCTS</a>"
    content = re.sub(v2_footer, v2_footer_repl, content)

    # Live index desktop
    live_desktop = r"(<li class=""menu-item""><a href=""services\.html"" class=""item-link link text-caption""><span>03 /</span>SERVICES</a></li>)"
    live_desktop_repl = r"\1\n                                    <li class=""menu-item""><a href=""products.html"" class=""item-link link text-caption""><span>04 /</span>PRODUCTS</a></li>"
    content = re.sub(live_desktop, live_desktop_repl, content)
    # Fix live index numbers
    content = re.sub(r"<span>04 /</span>ABOUT", "<span>05 /</span>ABOUT", content)
    content = re.sub(r"<span>05 /</span>CONTACT", "<span>06 /</span>CONTACT", content)

    # Live index footer
    live_footer = r"(<li><a href=""services\.html"" class=""link letter-space--2 h5"">Services</a></li>)"
    live_footer_repl = r"\1\n                                <li><a href=""products.html"" class=""link letter-space--2 h5"">Products</a></li>"
    content = re.sub(live_footer, live_footer_repl, content)

    # Main footer
    main_footer = r"(<a href=""services\.html"" class=""link letter-space--2 h5""\s*>Services</a\s*>)"
    main_footer_repl = r"\1\n                    <a href=""products.html"" class=""link letter-space--2 h5"">Products</a>"
    content = re.sub(main_footer, main_footer_repl, content)

    return content

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = insert_products(content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)

