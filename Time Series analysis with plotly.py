import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

forex_df=pd.read_csv("../Board Proj/Foreign_Exchange_Rates.csv")
forex_df.head()
forex_df=forex_df.drop("Unnamed: 0",axis=1)

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=forex_df['Time Serie'],
                y=forex_df['CANADA - CANADIAN DOLLAR/US$'],
                name="CAD/USD",
                line_color='red'))

fig.add_trace(go.Scatter(
                x=forex_df['Time Serie'],
                y=forex_df['CHINA - YUAN/US$'],
                name="CNY/USD",
                line_color='blue'))


fig.add_trace(go.Scatter(
                x=forex_df['Time Serie'],
                y=forex_df['EURO AREA - EURO/US$'],
                name="EUR/USD",
                line_color='orange'))

fig.add_trace(go.Scatter(
                x=forex_df['Time Serie'],
                y=forex_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                name="GBP/USD",
                line_color='green'))


fig.update_layout(title_text="Daily Exchange Rates (2000 - 2019)")
fig.show()

print("Daily Exchange Rates (2000-2009)")

fig = go.Figure()
fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['CANADA - CANADIAN DOLLAR/US$'],
                 name="CAD/USD",
                 line_color='red'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['CHINA - YUAN/US$'],
                 name="CNY/USD",
                 line_color='blue'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['EURO AREA - EURO/US$'],
                 name="EUR/USD",
                 line_color='orange'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                 name="GBP/USD",
                 line_color='green'))

fig.update_layout(xaxis_range=['2000-01-03','2009-12-31'],
                   title_text="Daily Exchange Rates (2000 - 2009)")

fig.show()

print("Daily Exchange Rates (2010-2019)")

fig = go.Figure()
fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['CANADA - CANADIAN DOLLAR/US$'],
                 name="CAD/USD",
                 line_color='red'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['CHINA - YUAN/US$'],
                 name="CNY/USD",
                 line_color='blue'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['EURO AREA - EURO/US$'],
                 name="EUR/USD",
                 line_color='orange'))

fig.add_trace(go.Scatter(
                 x=forex_df['Time Serie'],
                 y=forex_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                 name="GBP/USD",
                 line_color='green'))

fig.update_layout(xaxis_range=['2010-01-01','2019-12-31'],
                   title_text="Daily Exchange Rates (2010 - 2019)",
                   xaxis_rangeslider_visible=True)

fig.show()
