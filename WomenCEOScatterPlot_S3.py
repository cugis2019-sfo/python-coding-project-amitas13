import pandas as pd
import plotly
from plotly.offline import download_plotlyjs, plot
import plotly.graph_objs as go

df = pd.read_excel('wo.xlsx', sheet_name = 'women_CEOs')


trace = go.Scatter(x= df['Year'], y=df['Percentages'],
                   
                   #We add the mode parameter to create markers
                   mode='markers',
                   
                   #We add colors to the markers to make them distinct
                   #Note we use the marker parameter!
                   marker = dict(size=12, 
                                 color = df['Percentages'],
                                 colorscale= 'Jet',
                                 showscale= True),
                   name = 'Percentage Scale')


'''We use the Layout function of the go library'''                   
layout = go.Layout(
                  #Define title of the graph  
                  title = 'Share of CEOs who are women',
                  
                  #We add the plot_bgcolor and showlegend parameters
                  plot_bgcolor= 'rgb(247, 244, 244)',
                  showlegend= True,
                  
                  #Define title for x-axis
                  xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text='Year'
                        )
                    ),
                   
                    #Define title for y-axis
                   yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text='Percentages',
                        )
                    )
                   
                  )

''' We use Figure function of go library'''                            
fig = go.Figure(data=[trace], layout=layout)


'''We call the plot function from the plotly.offline library'''
plot(fig)



