import csv
import plotly.graph_objects as go
import numpy as np

filename = 'DataProject/county_pop_data.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get name, population growth (domestic and international)
    names, pop_growth, counties_net_change = [], [], []
    
    for row in reader:
        sumlev = int(row[0])
        name = (row[6])
        # if name is for grand traverse county fill gt array
        if sumlev==50:
            net_change = 0
            for x in range(86, 97):
                pop_growth_for_year = int(row[x])
                pop_growth.append(pop_growth_for_year)
                net_change += pop_growth_for_year
            if net_change > 1000 and net_change < 6500:
                counties_net_change.append(net_change)
                names.append(name)

colors=['lightgreen','lightblue','lavender','lemonchiffon']
fig = go.Figure(data=[go.Pie(labels=names, values=counties_net_change)])
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=20, 
    marker=dict(colors=colors,line=dict(color='black',width=2))
    )
fig.update_layout(
    title_text="Mid Range Growth of 1000-6500",
    title_font_color="darkgreen", 
    title_font_size=30, 
    title_font_family="Raleway", 
    title_xref="paper", 
    title_yref="paper",
    margin_l=200,
    margin_r=200
    )
fig.show()
