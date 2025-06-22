import pandas as pd

def export_conll_tokens(df: pd.DataFrame, output_path: str, text_column: str = "text") -> None:
    """
    Clean a DataFrame by dropping extra columns and export tokenized text to CoNLL-ready format.

    Parameters:
    - df: pandas DataFrame with a 'text' column.
    - output_path: file path to save the tokenized output.
    - text_column: name of the column containing raw text (default = 'text').
    """
    # Drop unnecessary columns if they exist
    df = df.drop(columns=['channel_username', 'text_length'], errors='ignore')

    # Tokenize and write each token on a new line
    with open(output_path, "w", encoding="utf-8") as f:
        for message in df[text_column]:
            tokens = str(message).split()
            for token in tokens:
                f.write(f"{token}\n")
            f.write("\n")
