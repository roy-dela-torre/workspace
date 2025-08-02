import requests
from bs4 import BeautifulSoup, Tag
import pandas as pd
from urllib.parse import urlparse
import time

# List of blog post URLs
urls = [
    "https://www.windowworksnc.com/should-you-cap-your-windows-what-homeowners-in-apex-nc-need-to-know/",
    "https://www.windowworksnc.com/vinyl-or-vinyl-clad-what-homeowners-in-holly-springs-nc-should-know-before-upgrading/",
    "https://www.windowworksnc.com/confused-about-which-windows-to-buy-our-free-buying-guide-makes-it-simple/",
    "https://www.windowworksnc.com/why-you-should-rethink-buying-windows-on-sale-for-your-home-in-cary-nc/",
    "https://www.windowworksnc.com/full-frame-vs-pocket-window-replacement-in-holly-springs-nc-what-gets-removed/",
    "https://www.windowworksnc.com/think-you-dont-need-dunnage-doors-think-again/",
    "https://www.windowworksnc.com/pultrusion-and-extrusion-explained-what-cary-nc-homeowners-should-know-about-door-construction/",
    "https://www.windowworksnc.com/guide-to-bifold-stack-and-slide-patio-doors-for-morrisville-nc-homes/",
    "https://www.windowworksnc.com/choosing-between-a-slider-or-hinged-patio-door-which-is-best-for-your-morrisville-nc-home/",
    "https://www.windowworksnc.com/why-you-should-avoid-buying-doors-online-without-local-support-in-apex-nc/",
    "https://www.windowworksnc.com/why-long-door-handles-are-a-must-have-trend-for-2025-in-cary-nc/",
    "https://www.windowworksnc.com/a-simple-water-test-can-determine-if-the-windows-in-your-apex-nc-home-were-improperly-installed/",
    "https://www.windowworksnc.com/broken-front-door-glass-in-holly-springs-nc-home-now-what-advice-from-a-door-installer/",
    "https://www.windowworksnc.com/the-5-hidden-costs-of-wood-doors-in-holly-springs-nc/",
    "https://www.windowworksnc.com/is-your-raleigh-nc-wood-front-door-really-all-wood/",
    "https://www.windowworksnc.com/demystifying-window-sizes-a-quick-guide-for-busy-homeowners-in-raleigh-nc/",
    "https://www.windowworksnc.com/are-windows-installed-from-the-inside-or-the-outside-of-a-home-in-cary-nc/",
    "https://www.windowworksnc.com/five-steps-to-choosing-the-right-size-window-for-your-space-in-morrisville-nc/",
    "https://www.windowworksnc.com/no-you-probably-dont-need-impact-resistant-windows-in-central-nc/",
    "https://www.windowworksnc.com/how-long-should-a-front-door-last/",
    "https://www.windowworksnc.com/5-reasons-why-a-pre-hung-door-is-better-than-a-slab-every-time/",
    "https://www.windowworksnc.com/should-the-door-heights-throughout-my-home-match/",
    "https://www.windowworksnc.com/top-3-reasons-to-fall-in-love-with-provia-doors/",
    "https://www.windowworksnc.com/whats-the-best-front-door-material-for-homes-in-raleigh-nc/",
    "https://www.windowworksnc.com/still-looking-for-storm-windows-heres-why-you-cant-find-them/",
    "https://www.windowworksnc.com/oops-the-complete-guide-to-reselling-windows-online-in-apex-nc/",
    "https://www.windowworksnc.com/avoid-these-three-grille-mistakes-when-updating-a-homes-windows-in-holly-springs-nc/",
    "https://www.windowworksnc.com/5-reasons-to-love-floor-to-ceiling-slim-vertical-windows/",
    "https://www.windowworksnc.com/condensation-outside-your-windows-separating-fact-from-fiction/",
    "https://www.windowworksnc.com/does-replacing-windows-increase-your-holly-springs-nc-homes-value/",
    "https://www.windowworksnc.com/what-is-cladding-on-a-window/",
    "https://www.windowworksnc.com/five-money-saving-tips-for-buying-new-windows-in-raleigh-nc-that-will-wind-up-costing-you-money/",
    "https://www.windowworksnc.com/a-door-experts-verdict-is-it-good-or-bad-to-install-a-pet-door/",
    "https://www.windowworksnc.com/the-top-5-rooms-in-your-raleigh-nc-home-for-adding-a-dutch-door/",
    "https://www.windowworksnc.com/multipoint-lock-maintenance-4-essential-steps-to-keep-your-front-door-secure/",
    "https://www.windowworksnc.com/the-science-behind-thermal-break-doors-how-they-work-to-improve-your-homes-energy-efficiency/",
    "https://www.windowworksnc.com/whats-the-best-season-to-replace-a-front-door-in-apex-nc/",
    "https://www.windowworksnc.com/updated-energy-star-certification-requirements-for-homes-in-apex-nc/",
    "https://www.windowworksnc.com/the-unfiltered-truth-about-pass-through-windows-for-homes-in-cary-nc/",
    "https://www.windowworksnc.com/7-telltale-signs-of-a-bad-window-installation-job-in-your-wake-county-nc-home/",
    "https://www.windowworksnc.com/5-undeniable-reasons-why-double-hung-windows-for-your-apex-nc-homes-are-better-than-single-hung-windows/",
    "https://www.windowworksnc.com/can-you-buy-and-install-andersen-windows-for-your-holly-springs-nc-home-yourself/",
    "https://www.windowworksnc.com/7-gorgeous-front-door-hardware-add-ons-to-boost-your-raleigh-nc-homes-curb-appeal/",
    "https://www.windowworksnc.com/the-top-5-advantages-of-using-prefinished-doors-in-your-morrisville-nc-home/",
    "https://www.windowworksnc.com/why-do-doors-in-holly-springs-nc-cost-so-much/",
    "https://www.windowworksnc.com/are-multipoint-lock-doors-for-your-cary-nc-home-worth-the-investment/",
    "https://www.windowworksnc.com/5-reasons-to-love-dsa-master-crafted-doors-for-your-holly-springs-nc-home/",
    "https://www.windowworksnc.com/three-reasons-to-love-patio-door-built-in-blinds-for-your-cary-nc-home/",
    "https://www.windowworksnc.com/boost-your-homes-curb-appeal-with-an-arch-top-or-round-top-front-door/",
    "https://www.windowworksnc.com/3-updates-to-take-your-sidelights-and-transoms-from-frump-to-fresh/",
    "https://www.windowworksnc.com/making-this-mistake-when-buying-energy-efficient-windows-for-your-new-home-in-raleigh-nc-can-cost-you-thousands/",
    "https://www.windowworksnc.com/avoid-these-3-rookie-assumptions-when-replacing-your-windows-for-your-morrisville-nc-home/",
    "https://www.windowworksnc.com/questions-about-window-measurement-and-consultation-appointments-answered/",
    "https://www.windowworksnc.com/5-essential-features-of-japandi-style-windows/",
    "https://www.windowworksnc.com/stop-these-5-common-practices-will-void-the-warranty-on-new-windows/",
    "https://www.windowworksnc.com/the-5-steps-you-must-take-when-researching-replacement-windows/",
    "https://www.windowworksnc.com/full-frame-or-pocket-insert-replacement-windows/",
    "https://www.windowworksnc.com/2023-door-trends-our-top-three-predictions/",
    "https://www.windowworksnc.com/an-in-depth-guide-to-getting-an-ada-compliant-door-to-make-your-home-accessible/",
    "https://www.windowworksnc.com/front-door-security-5-tips-for-break-in-proof-doors-that-every-homeowner-should-know/",
    "https://www.windowworksnc.com/replacing-a-window-with-a-door-read-these-dos-and-donts-first/",
    "https://www.windowworksnc.com/window-trends-we-hope-are-gone-for-good-in-2023/",
    "https://www.windowworksnc.com/what-is-brickmould-on-a-window/",
    "https://www.windowworksnc.com/3-scary-things-that-can-happen-when-you-diy-window-installation/",
    "https://www.windowworksnc.com/can-i-just-replace-some-of-my-windows-at-a-time-and-which-ones-should-i-choose/",
    "https://www.windowworksnc.com/energy-efficient-windows/",
    "https://www.windowworksnc.com/the-top-5-features-to-look-for-in-a-vinyl-window/",
    "https://www.windowworksnc.com/why-are-windows-so-expensive/",
    "https://www.windowworksnc.com/5-rules-for-replacing-your-historic-homes-doors/",
    "https://www.windowworksnc.com/dutch-door/",
    "https://www.windowworksnc.com/5-things-to-avoid-doing-to-your-new-morrisville-nc-homes-front-door/",
    "https://www.windowworksnc.com/the-only-exterior-door-maintenance-checklist-youll-ever-need/",
    "https://www.windowworksnc.com/5-essential-sliding-glass-door-features/",
    "https://www.windowworksnc.com/door-terminology-explained-door-parts-101/",
    "https://www.windowworksnc.com/why-not-install-my-own-front-door/",
    "https://www.windowworksnc.com/top-10-questions-about-patio-doors-answered/",
    "https://www.windowworksnc.com/energy-efficient-door/",
    "https://www.windowworksnc.com/do-i-have-andersen-windows-how-to-find-out-in-under-a-minute/",
    "https://www.windowworksnc.com/get-ready-for-window-installation/",
    "https://www.windowworksnc.com/andersen-window-series-an-in-depth-product-comparison/",
    "https://www.windowworksnc.com/andersen-versus-renewal-by-andersen-windows/",
    "https://www.windowworksnc.com/fog-between-the-windows-whats-normal-and-whats-not-when-it-comes-to-moisture-between-your-window-panes/",
    "https://www.windowworksnc.com/top-10-costly-mistakes-to-avoid-when-buying-new-windows/",
    "https://www.windowworksnc.com/three-factors-that-affect-the-cost-of-new-windows/",
    "https://www.windowworksnc.com/replace-a-wood-front-door/",
    "https://www.windowworksnc.com/7-questions-to-ask-yourself-before-getting-a-new-front-door/"
]


def get_slug(url):
    return urlparse(url).path.strip('/').split('/')[-1]

def get_featured_image(soup):
    og_image = soup.find('meta', property='og:image')
    if og_image and og_image.get('content'):
        return og_image['content']
    image_module = soup.find('div', class_='et_pb_module et_pb_image et_pb_image_0_tb_body')
    if image_module:
        img = image_module.find('img')
        if img and img.get('src'):
            return img['src']
    img = soup.find('img')
    if img and img.get('src'):
        return img['src']
    return ''

def get_meta_description(soup):
    meta = soup.find('meta', attrs={'name': 'description'})
    if meta and meta.get('content'):
        return meta.get('content')
    return ''

def get_title_tag(soup):
    if soup.title:
        return soup.title.string.strip()
    return ''

def get_post_title(soup):
    h1 = soup.find('h1')
    if h1:
        return h1.get_text(strip=True)
    return get_title_tag(soup)

def remove_style_attributes(soup):
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]
    return soup

def extract_images_from_tag(tag):
    images = []
    for img in tag.find_all("img"):
        if img.get("src"):
            images.append(str(img))
    return images

def extract_clean_content(soup):
    from bs4 import BeautifulSoup, Tag, NavigableString

    container = soup.find("div", class_="et_pb_module et_pb_post_content et_pb_post_content_0_tb_body")
    if not container:
        return ""

    allowed_tags = {
        "h1", "h2", "h3", "h4", "h5", "h6",
        "p", "a", "img", "ul", "ol", "li", "blockquote",
        "b", "i", "strong", "em"
    }
    allowed_img_attrs = {"src", "alt", "width", "height"}
    allowed_a_attrs = {"href", "target", "rel"}

    # Unwrap all spans inside allowed tags
    for tag in container.find_all(allowed_tags):
        for span in tag.find_all("span"):
            span.unwrap()

    def clean_tag(tag):
        if isinstance(tag, NavigableString):
            return str(tag)
        if tag.name not in allowed_tags:
            # Social wrapper image handling
            if tag.name == "div" and "et_social_media_wrapper" in tag.get("class", []):
                img = tag.find("img")
                if img:
                    src = img.get("data-src") or img.get("src")
                    alt = img.get("alt", "")
                    width = img.get("width", "")
                    height = img.get("height", "")
                    return f'<img src="{src}" alt="{alt}" width="{width}" height="{height}">'
            return ""
        if tag.name == "img":
            src = tag.get("data-src") or tag.get("src")
            alt = tag.get("alt", "")
            width = tag.get("width", "")
            height = tag.get("height", "")
            return f'<img src="{src}" alt="{alt}" width="{width}" height="{height}">'
        elif tag.name == "a":
            attrs = {k: v for k, v in tag.attrs.items() if k in allowed_a_attrs}
            if "rel" in attrs:
                rel = attrs["rel"]
                if isinstance(rel, list):
                    rel = " ".join(rel)
                attrs["rel"] = rel
            attrs_string = " ".join(f'{k}="{v}"' for k, v in attrs.items())
            children_html = ''.join(clean_tag(child) if isinstance(child, Tag) else str(child) for child in tag.children)
            return f'<a {attrs_string}>{children_html}</a>'
        elif tag.name == "p":
            inner = ''.join(clean_tag(child) if isinstance(child, Tag) else str(child) for child in tag.children)
            return f"<p>{inner.strip()}</p>" if inner.strip() else ""
        elif tag.name in {"ul", "ol"}:
            lis = [clean_tag(child) for child in tag.children if isinstance(child, Tag) and child.name == "li"]
            lis = [li for li in lis if li.strip()]
            return f"<{tag.name}>\n{''.join(lis)}\n</{tag.name}>" if lis else ""
        elif tag.name == "li":
            inner = ''.join(clean_tag(child) if isinstance(child, Tag) else str(child) for child in tag.children)
            return f"<li>{inner.strip()}</li>" if inner.strip() else ""
        elif tag.name in {"h1","h2","h3","h4","h5","h6"}:
            heading_text = ''.join(
                str(child) if isinstance(child, NavigableString)
                else (child.get_text(strip=True) if child.name in {"b", "strong"} else clean_tag(child))
                for child in tag.children
            )
            return f"<{tag.name}>{heading_text.strip()}</{tag.name}>" if heading_text.strip() else ""
        else:
            inner = ''.join(clean_tag(child) if isinstance(child, Tag) else str(child) for child in tag.children)
            return f"<{tag.name}>{inner.strip()}</{tag.name}>" if inner.strip() else ""

    output = []
    for child in container.children:
        cleaned = clean_tag(child)
        if cleaned.strip():
            output.append(cleaned)

    return "\n\n".join(output)

data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

for url in urls:
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = get_post_title(soup)
        slug = get_slug(url)
        content = extract_clean_content(soup)
        image = get_featured_image(soup)
        title_tag = get_title_tag(soup)
        meta_description = get_meta_description(soup)
        data.append({
            'title': title,
            'slug': slug,
            'content': content,
            'image': image,
            'title_tag': title_tag,
            'meta_description': meta_description
        })
        time.sleep(1)
    except Exception as e:
        print(f"Error processing {url}: {e}")

df = pd.DataFrame(data, columns=[
    'title', 'slug', 'content', 'image', 'title_tag', 'meta_description'
])

excel_path = r'C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\blog_post.xlsx'
df.to_excel(excel_path, index=False)
print(f"Data saved to {excel_path}")