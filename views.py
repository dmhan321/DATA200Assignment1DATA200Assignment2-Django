from django.shortcuts import render
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import numpy as np

def billionaires_combined(request):

    np.random.seed(56)

    # Read the CSV file into a DataFrame
    billionaires_data = pd.read_csv(r'Billionaires_Statistics_Dataset.csv')
    billionaires_data.dropna(how='any', inplace=True)

    #Calculate the count of each category
    category_counts = billionaires_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']
    category_counts['random_x'] = np.random.randint(0, 300, len(category_counts))
    category_counts['random_y'] = np.random.randint(0, 151, len(category_counts))

    # Create the Bubble Chart using Plotly
    fig = px.scatter(category_counts, x='random_x', y='random_y', size='count', text='category', color='category',
                    title="Billionaires' Business Domains")

    fig.update_traces(marker=dict(sizemode='diameter'))
    # fig.update_traces(textposition='top center')
    fig.update_layout(width=1400, height=1000) 
    fig.update_layout(title_x=0.5)

    plot_div = fig.to_html()

    names = ' '.join(billionaires_data['firstName'].dropna())
    wordcloud = WordCloud(width=1000, height=600, background_color='white').generate(names)
    output_path  = r"C:\Users\dmhan\DATA200Django\billionaires\static\wordcloud.png"
    wordcloud.to_file(output_path)

    context = {
        'wordcloud_image': r"C:\Users\dmhan\DATA200Django\billionaires\static\wordcloud.png",
        'plot_div': plot_div,
    }
    return render(request, 'BillionaireInsights/billionaires_combined.html', context)