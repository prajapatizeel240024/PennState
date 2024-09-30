import os

def save_to_file(file_path, content):
    """Saves the crawled content to a specified file path."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)