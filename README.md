# -Amharic-E-commerce-Data-Extractor
Amharic E-Commerce Entity Extraction is a machine learning pipeline that scrapes Amharic Telegram e-commerce posts and fine-tunes a multilingual transformer model to extract key business entities like Product, Price, and Location,  helping EthioMart become the central hub for Telegram-based digital commerce in Ethiopia.

This project is part of a data annotation and modeling pipeline for Amharic Telegram e-commerce channels. It includes data scraping, preprocessing, manual annotation in CoNLL format, and visualizations.
--

## 📁 Directory Structure of AMHARIC-E-COMMERCE-DATA-EXTRACTOR

```
├── .github/                             # GitHub actions and workflows
├── .venv/                               # Python virtual environment
├── data/
│   ├── processed/
│   │   ├── conull.csv                   # Final labeled data in CoNLL table format
│   │   ├── telegram_scraped_data_cleaned.csv  # Cleaned Telegram messages
│   │   └── top_30_messages_per_channel.csv    # Top 30 messages per channel for annotation
│   ├── raw/
│   │   ├── images/                      # Downloaded product images
│   │   └── telegram_scraped_data.csv   # Raw scraped Telegram messages
│
├── models/                              # Folder for storing fine-tuned NER models
│
├── notebook/
│   ├── task-1/
│   │   ├── normalization_and_tokenization.ipynb # Preprocessing pipeline
│   │   ├── scrapper_session.session              # Telethon session file
│   │   └── scrapping.ipynb                       # Telegram scraping script
│   ├── task-2/
│   │   ├── coNull.ipynb                          # CoNLL labeling and analysis
│   │   └── conll_ready_tokenized.txt            # Tokenized text for manual labeling
│
├── src/
│   ├── config.py                    # Channel list, phone, and output paths
│   ├── pre_processing.py            # Amharic text cleaning and normalization
│   ├── scrapper.py                  # Telegram scraping with Telethon
│   ├── coNLL.py                     # Exporting CoNLL formatted files and label analysis
│   └── visualization.py            # Word counts, channel stats, font-safe Amharic plots
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to ignore by Git
└── README.md                        # This file
```

---

## 🔨 Setup & Installation

```bash
# Clone the repo
$ git clone https://github.com/sumeyaaaa/-Amharic-E-commerce-Data-Extractor.git
$ cd -Amharic-E-commerce-Data-Extractor

# Create virtual environment
$ python -m venv .venv
$ .venv\Scripts\activate      # On Windows

# Install dependencies
$ pip install -r requirements.txt
```

---

## 📌 Key Tasks

### ✅ Task 1: Scraping & Preprocessing
- Scrape Amharic e-commerce content using **Telethon**.
- Normalize and clean the Amharic text.
- Select top 30 messages per channel.

### ✅ Task 2: CoNLL Annotation Prep
- Export cleaned tokens in a `.txt` file ready for manual labeling.
- Load manually labeled CoNLL table and compute label coverage.

### 📊 Visualizations
- Top N most common words
- Bar chart of message counts per channel
- Custom font support for Amharic text using `Abyssinica SIL`

---
###  Task 3: Fine-Tune NER Model
Use pretrained models:

xlm-roberta-base

bert-tiny-amharic

afroxlmr

Tokenize and align labels

Train using Hugging Face’s Trainer API

###  Task 4: Model Comparison
Evaluate multiple models (XLM-R, DistilBERT, mBERT)

Compare F1-score, training speed, token alignment issues

Select the best for production

###  Task 5: Interpretability with SHAP & LIME
Use SHAP to analyze token-level contributions

Use LIME for local explanations on misclassified entities

Identify weaknesses in model handling ambiguous or nested entities

###  Task 6: FinTech Vendor Scorecard
Compute per-vendor metrics:

🕒 Posts per week (activity)

👁️ Average views per post (engagement)

💰 Average product price (business profile)

###  Combine into a custom Lending Score

python
Copy
Edit
lending_score = (avg_views * 0.5) + (posts_per_week * 0.5)
Present results in a comparative table

###  Learning Outcomes
By completing this project, you will:

Build a full-stack NLP pipeline from raw data collection to model interpretation

Adapt LLMs (like XLM-R) to low-resource languages (Amharic)

Use SHAP and LIME for trustworthy model deployment

Design analytics tools for FinTech and e-commerce decision-making

###  Dependencies
bash
Copy
Edit
transformers
datasets
pandas
numpy
telethon
scikit-learn
shap
lime
matplotlib
Install them via:

bash
Copy
Edit
pip install -r requirements.txt
📎 References
Getting Started with Hugging Face NER

SHAP Documentation

LIME GitHub Repo

Amharic NER Dataset

###  Final Deliverables
✅ GitHub repo with all scripts and models

✅ PDF Report:

###  Methodology

Model results

Vendor scorecard

Interpretation summary



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


## 📦 Module Overview

### `src/config.py`
Configuration: phone number, channel usernames, and file paths.

### `src/pre_processing.py`
- Clean Amharic text (remove punctuations, links, emojis).
- Normalize characters for consistent tokenization.

### `src/scrapper.py`
- Login and fetch messages using Telethon.
- Save raw messages with metadata.

### `src/coNLL.py`
- Tokenizes messages and exports token-per-line `.txt`.
- Loads labeled data and analyzes how many tokens are labeled.

### `src/visualization.py`
- `plot_channel_distribution()` for message counts.
- `plot_top_words()` to show frequent words in Amharic (with font).

---

## 📊 Amharic Font Setup for Visualization
To render Amharic glyphs in plots:
1. Download [Abyssinica SIL](https://software.sil.org/abyssinica/download/)
2. Place `AbyssinicaSIL-Regular.ttf` in a `fonts/` directory
3. Use the font in visualization:

```python
plot_top_words(
  df,
  text_column="text",
  top_n=20,
  title="ከፍተኛ የተደገመ ቃላት",
  font_path="fonts/AbyssinicaSIL-Regular.ttf"
)
```

---

## 🧠 Future Improvements
- Train a Named Entity Recognition (NER) model on labeled CoNLL data
- Expand to multi-platform Amharic datasets
- Improve normalization for OCR text

---

## 📩 Contact
Developed by [@sumeyaaaa](https://github.com/sumeyaaaa)

---

**Note**: This project is part of a 10 Academy Week 4 challenge.

## 🧪 Setup Instructions

### Requirements
- Python 3.8+
- pandas, regex, telethon
- Jupyter Notebook

### Run scraping:
```bash
jupyter notebook notebook/task-1/scrapping.ipynb
