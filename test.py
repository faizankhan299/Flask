from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

app = Flask(__name__)

df = pd.read_csv("traffic accidents.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

#Graph functions

def accidents_vs_time_of_day():
    fig = px.bar(df, x= 'accidents', y = 'time_of_day',  
              title = 'Accidents vs Time of day')
    graph1_html = pio.to_html(fig, full_html=False)
    return graph1_html

def accidents_vs_traffic_density():
    fig = px.scatter(df, x = 'accidents', y  = 'traffic_density', 
                 title = 'Accidents vs. Traffic Density')
    graph2_html = pio.to_html(fig, full_html=False)
    return graph2_html

def Accidents_vs_rain_intensity():
    fig = px.bar(df, x = 'accidents', y = 'rain_intensity', 
             title = 'Accidents vs. Rain Intensity')
    graph3_html = pio.to_html(fig, full_html=False)
    return graph3_html

def Accidents_by_urban_area():
    fig = px.pie(df, names= 'accidents', values='urban_area',
             hole=0.2,title = 'Accidents by Urban Area ')
    graph4_html = pio.to_html(fig, full_html=False)
    return graph4_html 
  


  # environment impact analysis graph 




def Rain_intensity_vs_traffic_density():
    fig = px.line(df, x = 'rain_intensity' ,y = 'traffic_density',
              title = 'Rain intensity vs. Traffic Density')
    graph5_html = pio.to_html(fig, full_html=False)
    return graph5_html

def Rain_intensity_vs_average_speed():
    fig = px.scatter(df, x = 'rain_intensity' ,y = 'average_speed',
              title = 'Rain intensity vs. Average speed')
    graph6_html = pio.to_html(fig, full_html=False)
    return graph6_html

def Pavement_quality_vs_accidents():
    fig = px.bar(df, x = 'pavement_quality' , y = 'accidents',
             title= 'Pavement Quality vs. Accidents')
    graph7_html = pio.to_html(fig, full_html=False)
    return graph7_html

def Rain_intensity_vs_accidents():
    fig = px.bar(df, x = 'rain_intensity' , y = 'accidents',
             title= 'Rain Intensity vs. Accidents')
    graph8_html = pio.to_html(fig, full_html=False)
    return graph8_html






# traffiv fine analysis 


def Traffic_fine_amount_distribution():
    fig = px.histogram(df, x= 'traffic_fine_amount',
             title = 'Traffic fine Amount Distribution')
    graph9_html = pio.to_html(fig, full_html=False)
    return graph9_html

def Traffic_fine_Amount_vs_traffic_density():
    fig = px.scatter(df.head(102), x = 'traffic_fine_amount', y = 'traffic_density',
                 title = 'Traffic Fine Amount VS. Traffic Density')
    graph10_html = pio.to_html(fig, full_html=False)
    return graph10_html

def Traffic_fine_Amount_vs_pavement_quality():
    fig = px.box(df, x = 'traffic_fine_amount' , y = 'pavement_quality',
             title= 'Traffic Fine Amount VS. Pavement Quality')
    graph11_html = pio.to_html(fig, full_html=False)
    return graph11_html

def Traffic_fine_Amount_by_time_of_day():
    fig = px.bar(df, x = 'traffic_fine_amount' , y = 'time_of_day',
             title= 'Traffic Fine Amount by Time of Day')
    graph12_html = pio.to_html(fig, full_html=False)
    return graph12_html




# traffic flow analysis

def Traffic_density_vs_time_of_day():
    fig = px.line( df, x = 'traffic_density' , y = 'time_of_day',
              title = 'Traffic density vs Time of day')
    graph13_html = pio.to_html(fig, full_html=False)
    return graph13_html


def Vehicle_count_vs_average_speed():
    fig = px.scatter( df, x = 'vehicle_count', y = 'average_speed',
                 title = 'Vechile Count vs. Average speed')
    graph14_html = pio.to_html(fig, full_html=False)
    return graph14_html

def Traffic_lights_vs_traffic_density():
    fig = px.bar(df, x = 'traffic_lights', y = 'traffic_density',
             title = 'Traffic Light vs. Traffic Density')
    graph15_html = pio.to_html(fig, full_html=False)
    return graph15_html

def Traffic_density_vs_urban_area():
    fig = px.density_heatmap(df, x = 'traffic_density', y = 'urban_area',
                         title='Traffic Density  vs. Urban area')
    graph16_html = pio.to_html(fig, full_html=False)
    return graph16_html








# correlation and predective analysis 

def Accidents_vs_traffic_density():
    fig = px.scatter(df, x="traffic_density", y="accidents",
                 title="Accidents vs. Traffic Density",
                 labels={"traffic_density": "Traffic Density", "accidents": "Number of Accidents"},
                 color="traffic_density",  
                 size="accidents",         
                 template="plotly")
    graph17_html = pio.to_html(fig, full_html=False)
    return graph17_html


def Correlation_matrix_heatmap():
    correlation_matrix = df[[
    "accidents", "traffic_fine_amount", "traffic_density", "traffic_lights",
    "pavement_quality", "urban_area", "average_speed", "rain_intensity",
    "vehicle_count", "time_of_day"
]].corr()


    fig = px.imshow(correlation_matrix,
                labels=dict(x="Features", y="Features", color="Correlation Coefficient"),
                x=correlation_matrix.columns,
                y=correlation_matrix.columns,
                color_continuous_scale="Viridis",
                title="Correlation Matrix Heatmap")

    fig.update_layout(width=800, height=600)
    graph18_html = pio.to_html(fig, full_html=False)
    return graph18_html




def Regression_plot_vehicle_count_vs_average_speed():
    fig = px.scatter(df, x="vehicle_count", y="average_speed",
        title="Regression Plot: Vehicle Count vs. Average Speed",
        labels={"vehicle_count": "Vehicle Count", "average_speed": "Average Speed"},
        trendline="ols", 
        template="plotly")
    graph19_html = pio.to_html(fig, full_html=False)                  
    return graph19_html




def threed_scatter_rain_intensity_traffic_density_accidents():
    fig = px.scatter_3d(df, x="rain_intensity", y="traffic_density", z="accidents",
                    title="3D Scatter Plot: Rain Intensity, Traffic Density, and Accidents",
                    labels={
                        "rain_intensity": "Rain Intensity",
                        "traffic_density": "Traffic Density",
                        "accidents": "Number of Accidents"},
                    color="rain_intensity", 
                    size="accidents",
                    template="plotly")
    graph20_html = pio.to_html(fig, full_html=False)
    return graph20_html







#time based analysis 

def Accidents_vs_time_of_day():
    fig = px.line(df,x="time_of_day", y="accidents",
                  title="Accidents vs. Time of Day",
                  labels={"time_of_day": "Time of Day", "accidents": "Number of Accidents"},
                  markers=True)
    graph21_html = pio.to_html(fig, full_html=False)
    return graph21_html



def Traffic_fine_by_time_of_day():
    fig = px.bar(df,x="time_of_day",y="traffic_fine_amount",   
                title="Traffic Fine Amount by Time of Day",
                labels={"time_of_day": "Time of Day", "traffic_fine_amount": "Traffic Fine Amount"},
                color="traffic_fine_amount",  
                hover_data=["traffic_fine_amount"])
    graph22_html = pio.to_html(fig, full_html=False)
    return graph22_html


def Traffic_density_vs_time_of_day():
    fig = px.scatter(df, x="time_of_day", y="traffic_density",   
                    title="Traffic Density vs. Time of Day",
                    labels={"time_of_day": "Time of Day", "traffic_density": "Traffic Density"},
                    color="traffic_density",  
                    size="traffic_density",  
                    hover_data=["traffic_density"])
    graph23_html = pio.to_html(fig, full_html=False)
    return graph23_html







#ANALYSIS PAGES


@app.route('/analysis')
def analysis():
    graph1 =  accidents_vs_time_of_day()
    graph2 = accidents_vs_traffic_density()
    graph3 = Accidents_vs_rain_intensity()
    graph4 = Accidents_by_urban_area()
    return render_template('analysis.html', graph1=graph1, graph2=graph2, graph3=graph3, graph4=graph4)

@app.route('/environmentimpact')
def environmentimpact():
    graph5 = Rain_intensity_vs_traffic_density
    graph6 = Rain_intensity_vs_average_speed()
    graph7 = Pavement_quality_vs_accidents()
    graph8 = Rain_intensity_vs_accidents()
    return render_template('environmentimpact.html', graph5=graph5, graph6=graph6,graph7=graph7, graph8=graph8)

@app.route('/trafficfine')
def trafficfine():
    graph9 =  Traffic_fine_amount_distribution()
    graph10 = Traffic_fine_Amount_vs_traffic_density()
    graph11 = Traffic_fine_Amount_vs_pavement_quality()
    graph12 = Traffic_fine_by_time_of_day()
    return render_template('trafficfine.html', graph9=graph9, graph10=graph10, graph11=graph11, graph12=graph12)

@app.route('/trafficflow')
def trafficflow(): 
    graph13 = Traffic_density_vs_time_of_day()
    graph14 = Vehicle_count_vs_average_speed()
    graph15 = Traffic_lights_vs_traffic_density()
    graph16 = Traffic_density_vs_urban_area()
    return render_template('traficflow.html' , graph13=graph13,graph14=graph14, graph15=graph15, graph16=graph16)

@app.route('/correlation')   
def correlation():
    graph17 = accidents_vs_traffic_density()
    graph18 = Correlation_matrix_heatmap()
    graph19 = Regression_plot_vehicle_count_vs_average_speed()
    graph20 = threed_scatter_rain_intensity_traffic_density_accidents()
    return render_template('correlation.html', graph17=graph17, graph18=graph18, graph19=graph19, graph20=graph20)

@app.route('/timebased')
def timebased():
    graph21 = accidents_vs_time_of_day()
    graph22 = Traffic_fine_by_time_of_day()
    graph23 = Traffic_density_vs_time_of_day()


    return render_template('timebased.html', graph21=graph21, graph22=graph22, graph23=graph23)




if __name__ == '__main__':
    app.run(debug=True) 
