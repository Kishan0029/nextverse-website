import os
import re
import urllib.request
import urllib.error

base_url = "https://wpriverthemes.com/HTML/davies/"
html_dir = "E:/davies-mainfiles/davies/"

# Find all HTML files
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

image_paths = set()
pattern = re.compile(r'src="(assets/images/[^"]+)"')
video_pattern = re.compile(r'src="(assets/images/video/[^"]+)"')
bg_pattern = re.compile(r'background-image:\s*url\((assets/images/[^)]+)\)')

for html_file in html_files:
    with open(os.path.join(html_dir, html_file), 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        for match in pattern.findall(content):
            image_paths.add(match)
        for match in bg_pattern.findall(content):
            image_paths.add(match.strip("'\""))

print(f"Found {len(image_paths)} unique media paths.")

# Download each file
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://wpriverthemes.com/HTML/davies/index.html'
}

for path in image_paths:
    local_path = os.path.join(html_dir, path)
    remote_url = base_url + path
    
    # ensure directory exists
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {path}")
    except Exception as e:
        print(f"Failed to download {remote_url}: {e}")

print("Done downloading all media.")
