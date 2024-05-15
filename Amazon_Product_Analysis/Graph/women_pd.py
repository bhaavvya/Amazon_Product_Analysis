import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

product_type_dataset = ["data_kurti.csv","data_saree.csv","data_womenjeans.csv"]
def convert_to_dataframe(index):
    data = pd.read_csv('./datasets/' + product_type_dataset[index],error_bad_lines=False)
    data['Rating']=pd.to_numeric(data['Rating'],errors='coerce')
    data['Price']=pd.to_numeric(data['Price'],errors='coerce')
    return data

def graph_1(data,women):
    brand_text = " ".join(data['Brand'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='tab20c').generate(brand_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Word Cloud of Brands')
    plt.tight_layout()

    chart_type = FigureCanvasTkAgg(plt.gcf(), master=women)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=2, column=0, columnspan=4)
    

def graph_2(data,women):
    
    sns.set(style="darkgrid")
    plt.figure(figsize=(12, 7))
    ax = sns.lineplot(x='Price', y='Rating', data=data)
    ax.set_title('Price vs Rating')
    ax.set_xlabel('Price')
    ax.set_ylabel('Rating')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=80)
    plt.tight_layout()

    chart_type = FigureCanvasTkAgg(plt.gcf(), master=women)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=3, column=0, columnspan=4)

def graph_3(data,women):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 7))
    ax = sns.scatterplot(x='Brand', hue='Rating',y='Price', data=data, palette='rocket_r')
    ax.set_title('Brand vs Price')
    ax.set_xlabel('Brand')
    ax.set_ylabel('Price')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.tight_layout()

    chart_type = FigureCanvasTkAgg(plt.gcf(), master=women)
    chart_type.draw()
    chart_type.get_tk_widget().grid(row=4, column=0, columnspan=4)

def show_graph(women,index):
    data = convert_to_dataframe(index)
    graph_1(data,women)
    graph_2(data,women)
    graph_3(data,women)
