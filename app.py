import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import seaborn as sns

# Download NLTK stopwords if not already present
try:
    stopwords.words('english')
except:
    nltk.download('stopwords')

# --- Part 1 & 2: Data Loading, Cleaning, and Preparation ---
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    
    # Drop rows with missing titles
    clean_df = df.dropna(subset=['title']).copy()
    
    # Fill missing values
    clean_df['abstract'].fillna('Not Available', inplace=True)
    clean_df['journal'].fillna('Not Available', inplace=True)
    
    # Convert and extract date information
    clean_df['publish_time'] = pd.to_datetime(clean_df['publish_time'], errors='coerce')
    clean_df.dropna(subset=['publish_time'], inplace=True)
    clean_df['publication_year'] = clean_df['publish_time'].dt.year
    
    # Create word count column
    clean_df['abstract_word_count'] = clean_df['abstract'].str.split().str.len()
    
    return clean_df

# Load the data
df = load_data()

# --- Part 4: Streamlit Application ---
st.title("CORD-19 Data Explorer")
st.write("A simple exploration of COVID-19 research papers using the metadata dataset.")

# Add interactive elements
min_year = int(df['publication_year'].min())
max_year = int(df['publication_year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, max_year))

# Filter data based on the slider selection
filtered_df = df[(df['publication_year'] >= year_range[0]) & (df['publication_year'] <= year_range[1])]

# --- Display Visualizations ---
st.header("Visualizations")

# Plot 1: Publications over time
st.subheader("Publications Over Time")
papers_by_year = filtered_df['publication_year'].value_counts().sort_index()
fig1, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=papers_by_year.index, y=papers_by_year.values, marker='o', ax=ax)
ax.set_title(f'Publications from {year_range[0]} to {year_range[1]}')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
ax.grid(True)
st.pyplot(fig1)

# Plot 2: Top publishing journals
st.subheader("Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax)
ax.set_title('Top 10 Publishing Journals')
ax.set_xlabel('Number of Papers')
ax.set_ylabel('Journal')
st.pyplot(fig2)

# Plot 3: Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
all_titles = ' '.join(filtered_df['title'].str.lower().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig3, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Word Cloud of Paper Titles')
st.pyplot(fig3)

# Plot 4: Distribution of papers by source
st.subheader("Distribution of Papers by Source")
source_counts = filtered_df['source_x'].value_counts()
fig4, ax = plt.subplots(figsize=(8, 8))
ax.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
ax.set_title('Distribution of Papers by Source')
st.pyplot(fig4)

# --- Display a sample of the data ---
st.header("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'abstract', 'publication_year']].sample(n=10))

# --- Conclusion ---
st.markdown("---")
st.info("This application provides a basic framework for exploring a large dataset. You can extend it by adding more complex visualizations, advanced text analysis (e.g., topic modeling), or search functionality.")