import matplotlib.pyplot as plt
import seaborn as sns

def plot_channel_message_distribution(df, column='channel_username', top_n=None, title="Messages per Channel", figsize=(10, 6), save_path=None):
    """
    Plots a horizontal bar chart of message counts per Telegram channel.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the channel column.
    - column (str): Column name for grouping (default: 'channel_username').
    - top_n (int): Number of top entries to show (e.g., top 10 channels).
    - title (str): Plot title.
    - figsize (tuple): Size of the figure (width, height).
    - save_path (str or None): If given, saves the plot to this path instead of showing it.
    """

    # Count channel messages
    value_counts = df[column].value_counts()

    if top_n:
        value_counts = value_counts.head(top_n)

    plt.figure(figsize=figsize)
    sns.set(style="whitegrid")
    ax = sns.barplot(x=value_counts.values, y=value_counts.index, palette="viridis")

    plt.title(title, fontsize=14)
    plt.xlabel("Number of Messages")
    plt.ylabel("Channel")
    plt.tight_layout()

    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from collections import Counter
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

from collections import Counter
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

import matplotlib.pyplot as plt
from matplotlib import font_manager
from collections import Counter

from matplotlib import font_manager
import matplotlib.pyplot as plt
from collections import Counter

def plot_top_words(df, text_column, top_n=20, title="", font_path=None):
    all_words = ' '.join(df[text_column].dropna().astype(str)).split()
    common = Counter(all_words).most_common(top_n)
    words, counts = zip(*common)

    # Load the Amharic font
    prop = font_manager.FontProperties(fname=font_path) if font_path else None

    plt.figure(figsize=(10, 6))
    plt.barh(range(len(words)), counts[::-1])  # Plot with numeric y-values

    # Manually set tick labels with font
    plt.yticks(ticks=range(len(words)), labels=words[::-1], fontproperties=prop)

    # Apply font to other text elements
    plt.title(title, fontsize=14, fontproperties=prop)
    plt.xlabel("መብዛት", fontproperties=prop)
    plt.ylabel("ቃላት", fontproperties=prop)

    plt.tight_layout()
    plt.show()

