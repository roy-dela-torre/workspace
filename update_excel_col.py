import openpyxl
import re

excel_path = r'C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\blog_post.xlsx'
wb = openpyxl.load_workbook(excel_path)
ws = wb.active

# Regex to match src="URL" inside <img> tags
img_src_pattern = re.compile(
    r'(<img[^>]+src=")(https?://[^\s">]+/(?:[\w-]+\.(?:jpg|jpeg|png|gif)))(")', re.IGNORECASE
)

# Regex to fix duplicated double quotes in HTML attributes
attr_quote_pattern = re.compile(r'="([^"]*)""')

def update_img_src(cell_value):
    if not isinstance(cell_value, str):
        return cell_value
    def replacer(match):
        prefix, old_url, suffix = match.groups()
        filename = old_url.split('/')[-1]
        new_url = f'https://windowworksnc.wpenginepowered.com/wp-content/uploads/2025/07/{filename}'
        return f'{prefix}{new_url}{suffix}'
    # Update image src
    updated = img_src_pattern.sub(replacer, cell_value)
    # Fix duplicated quotes in all HTML attributes
    updated = attr_quote_pattern.sub(r'="\1"', updated)
    return updated

for row in ws.iter_rows():
    for cell in row:
        cell.value = update_img_src(cell.value)

wb.save(excel_path)
