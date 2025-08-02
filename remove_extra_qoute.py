import pandas as pd
import re

# Load your Excel file
df = pd.read_excel(r'C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\blog_post.xlsx')

# Fix double double-quotes and remove leading/trailing quotes
df['content'] = df['content'].str.replace(r'""', '"', regex=True)
df['content'] = df['content'].str.strip('"')

# Replace domain in content
df['content'] = df['content'].str.replace(
    r'https://www\.windowworksnc\.com',
    'https://windowworksnc.wpenginepowered.com',
    regex=True
)

# Replace image URLs in content
def replace_image_url(text):
    text = str(text) if not pd.isna(text) else ""
    return re.sub(
        r'https://windowworksnc\.wpenginepowered\.com/wp-content/uploads/[^/]+/([^"\s]+)',
        r'https://windowworksnc.wpenginepowered.com/wp-content/uploads/2025/07/\1',
        text
    )

df['content'] = df['content'].apply(replace_image_url)

# Save the cleaned data to a new Excel file
df.to_excel('yourfile_fixed.xlsx', index=False)