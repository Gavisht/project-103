import plotly.express as pl
import pandas as pd
data = pd.read_csv("project.csv")
fig = pl.scatter(data, x = "date", y = "cases", color="country")
fig.show()