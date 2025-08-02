from bs4 import BeautifulSoup

input_html = r"C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\image.html"
output_txt = r"C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\image.txt"

with open(input_html, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

image_urls = []
for img in soup.find_all("img"):
    src = img.get("src")
    if src:
        image_urls.append(src)

with open(output_txt, "w", encoding="utf-8") as f:
    for url in image_urls:
        f.write(url + "\n")