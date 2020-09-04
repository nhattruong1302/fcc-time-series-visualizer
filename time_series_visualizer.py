import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
bot = df['value'].quantile(0.025)
top = df['value'].quantile(0.957)
df = df.loc[df.value>bot & df.value<top]


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(14,6))
    ax.plot(df.date, df.value, "r")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_group = df.copy()
    df_group['year'] = df.index.year
    df_group['month'] = df.index.month
    df_group1 = df_group.groupby(['df_group.year', 'df_group.month'], as_index = True)['value'].mean()
    df_bar = df_group1.pivot(index='year', columns='month', values='value')

    # Draw bar plot
    pos=list(range(len(set(df_bar.year))))
    width= 0.05

    fig,ax = plt.subplots(figsize =(14,6))
    ax.bar(pos, df_bar[1], width, label = 'January')
    ax.bar(p + width for p in pos, df_bar[2], width, label = 'February')
    ax.bar(p + width*2 for p in pos, df_bar[3], width, label = 'March')
    ax.bar(p + width*3 for p in pos, df_bar[4], width, label = 'April')
    ax.bar(p + width*4 for p in pos, df_bar[5], width, label = 'May')
    ax.bar(p + width*5 for p in pos, df_bar[6], width, label = 'June')
    ax.bar(p + width*6 for p in pos, df_bar[7], width, label = 'July')
    ax.bar(p + width*7 for p in pos, df_bar[8], width, label = 'August')
    ax.bar(p + width*8 for p in pos, df_bar[9], width, label = 'September')
    ax.bar(p + width*9 for p in pos, df_bar[10], width, label = 'October')
    ax.bar(p + width*10 for p in pos, df_bar[11], width, label = 'November')
    ax.bar(p + width*11 for p in pos, df_bar[12], width, label = 'December')
    ax.set_xticks(pos + width*5)
    ax.set_xticklabels(['2016', '2017', '2018', '2019'])
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(ncols=2, nrows=1, figsize = (14,6), sharey = True)
    sns.boxplot(x=df_box.year, y=df_box.value, axes = ax[0])
    sns.boxplot(x=df_box.month, y=df_box.value, axes = ax[1])
    




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
