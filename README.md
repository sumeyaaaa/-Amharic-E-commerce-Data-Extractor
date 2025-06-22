# -Amharic-E-commerce-Data-Extractor
Amharic E-Commerce Entity Extraction is a machine learning pipeline that scrapes Amharic Telegram e-commerce posts and fine-tunes a multilingual transformer model to extract key business entities like Product, Price, and Location,  helping EthioMart become the central hub for Telegram-based digital commerce in Ethiopia.

---
## 📁 Directory Structure of AMHARIC-E-COMMERCE-DATA-EXTRACTOR/

├── .github/
├── .venv/
├── data/
│ ├── processed/
│ │ ├── conull.csv # Final labeled data in CoNLL table format
│ │ ├── telegram_scraped_data_cleaned.csv# Cleaned Telegram messages
│ │ └── top_30_messages_per_channel.csv # Selected top messages per channel for annotation
│ ├── raw/
│ │ ├── images/ # Folder for downloaded product images
│ │ └── telegram_scraped_data.csv # Raw scraped messages
│
├── models/ # Folder for storing fine-tuned NER models
│
├── notebook/
│ ├── task-1/
│ │ ├── normalization_and_tokenization.ipynb # Preprocessing pipeline notebook
│ │ ├── scrapper_session.session # Telegram session file
│ │ └── scrapping.ipynb # Data scraping script using Telethon
│ ├── task-2/
│ │ ├── coNull.ipynb # CoNLL labeling and coverage analysis
│ │ └── conll_ready_tokenized.txt # Token-per-line file for manual annotation
│
├── src/
│ ├── config.py # Channel list, output paths, phone number
│ ├── pre_processing.py # Amharic text normalization/cleaning
│ ├── scrapper.py # Telegram client & scraping logic
│
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md # Project documentation (you are here)

yaml
Copy
Edit

## 🧠 Key Tasks

### Task 1: Data Ingestion and Preprocessing
- Scrapes messages from Ethiopian Telegram e-commerce channels.
- Cleans and normalizes Amharic text.
- Outputs: `telegram_scraped_data_cleaned.csv`

### Task 2: NER Data Preparation
- Selects top 30 longest messages per channel for rich labeling.
- Tokenizes messages and exports to CoNLL-ready `.txt` format.
- Manual annotation stored in `conull.csv`.
- Outputs: 
  - `top_30_messages_per_channel.csv`  
  - `conll_ready_tokenized.txt`  
  - `conull.csv`

### Task 3–5 (Planned):
- Fine-tune multilingual NER models (XLM-Roberta, BERT, etc.)
- Evaluate model with metrics: F1-score, Precision, Recall
- Interpret predictions using SHAP or LIME
- Save final model under `models/`

---

## 📌 Labels Used for Annotation

- `O` — Outside any entity
- `B-PRODUCT`, `I-PRODUCT`
- `B-AUDIENCE`
- `B-BRAND`, `I-BRAND`
- `B-COMPONENT`, `I-COMPONENT`
- `B-TASK`, `I-TASK`
- `B-CONTACT_INFO`
- `B-PRICE`, `I-PRICE`
- `B-LOC`, `I-LOC`
- `B-DATE`, `I-DATE`
- `B-FEATURE`, `I-FEATURE`
- `B-ATTRIBUTE`, `I-ATTRIBUTE`

---

## 📊 Labeling Stats
After cleaning:
- **Total tokens** = _N_
- **Labeled tokens (not 'O')** = _M_
- **Coverage** = _(M / N) * 100%_

(To be updated after each labeling batch)

---

## 🚀 Future Plans
- Complete model training and evaluation.
- Integrate prediction pipeline into EthioMart’s backend.
- Build a scoring engine to rank vendors based on posting frequency, product diversity, and customer engagement.

---

## 🧪 Setup Instructions

### Requirements
- Python 3.8+
- pandas, regex, telethon
- Jupyter Notebook

### Run scraping:
```bash
jupyter notebook notebook/task-1/scrapping.ipynb
