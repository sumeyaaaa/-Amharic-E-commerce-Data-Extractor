import re
import pandas as pd

def preprocess_amharic_text(text):
    if pd.isna(text):
        return ""
    
    # Normalize punctuation spacing
    text = re.sub(r'\s+', ' ', text)
    
    # Remove emojis and symbols
    text = re.sub(r'[^\w\s፡።፣፤፥፦፧፨መሀ-ቈቋ-ቝበ-ኅነ-ኰኸ-ዕዐ-ፗፘ-፼a-zA-Z0-9]+', '', text)

    # Optional: lowercasing English
    text = text.lower()

    return text.strip()
