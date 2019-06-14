import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go 

#We read the data into a variable

df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")


#We use the Bar function of the go library
womenoccupation = go.Bar(x= df["occupation"], y=df["women"],
               
               #We add color to the graph using the jet scale
               marker = {"color": df["women"], "colorscale" : "Jet"}
                )
                   
#We use the Layout function of the go library
titles = go.Layout(
                    #Define title of the graph
                    title = "Percentage of Women Employed by Occupation",
                    
                    #Define title for x-axis
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text="Occupation", 
                        )
                    ),
                  
                    #Define title for y-axis
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="Percentage",
                            )
                      )
                    )
                            
#We use Figure function of go library                           
fig = go.Figure(data=[womenoccupation], layout=titles)

#We call the plot function from the plotly.offline library
plot(fig)



