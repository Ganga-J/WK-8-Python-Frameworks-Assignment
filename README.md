CORD-19 Data Analysis: Project Report and Reflection
Overview
This project involved a basic data analysis of the CORD-19 research dataset's metadata file. The primary goals were to practice fundamental data science skills, including data loading, cleaning, analysis, and visualization, and to present the findings in a simple Streamlit web application.

Key Findings
Data Size and Structure: The metadata.csv file is a large, complex dataset with a mix of data types and a significant number of missing values. The initial exploration showed the need for a robust data cleaning process before any analysis could be performed.

Publication Trends: The analysis revealed a massive surge in COVID-19-related publications starting in 2020, with the majority of the research being published in that year and 2021. This trend directly reflects the global response to the pandemic.

Top Contributors: The analysis identified the top journals and repositories publishing this research. This insight highlights the key platforms where pandemic-related scientific information was being shared and disseminated.

Content Focus: A word cloud of paper titles showed a clear focus on keywords like "COVID," "Sars-Cov-2," "patients," and "infection," confirming the thematic concentration of the dataset.

Challenges and Learning
One of the main challenges encountered was data cleaning. The raw dataset contained inconsistent date formats and numerous missing values, which required careful handling to avoid errors in the analysis. A key learning from this was the importance of thoroughly inspecting the data and deciding on a consistent cleaning strategy (e.g., dropping rows with missing titles, filling missing abstract fields).

Another challenge was converting the analysis from a static Jupyter Notebook to an interactive Streamlit application. This required structuring the code differently to work within the app's framework, particularly using st.cache_data to ensure efficient data loading. This part of the assignment taught me how to transform a linear data analysis workflow into a dynamic, user-friendly presentation.

Overall, this project provided valuable, hands-on experience with a real-world dataset. I gained a deeper understanding of the entire data science workflow, from raw data to a presentable application.
