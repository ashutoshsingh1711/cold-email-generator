import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove special characters, including colons and semicolons (keeping only letters, numbers, and spaces)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # Trim leading and trailing whitespaces
    text = text.strip()

    return text
