## Data Viz Packages
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px
import pandas as pd
from sklearn import utils

def make_labels_and_names(X):

    if isinstance(X, pd.DataFrame):
        row_label = X.index.name if X.index.name else 'Rows'
        row_names = X.index.tolist()
        col_label = X.columns.name if X.columns.name else 'Columns'
        col_names = X.columns.tolist()
    else:
        row_label = 'Rows'
        row_names = list(range(X.shape[0]))
        col_label = 'Columns'
        col_names = list(range(X.shape[1]))

    return row_label, row_names, col_label, col_names

def plot(A,B, row_names, col_names, row_markers='markers+text', col_markers='markers+text'):
	fig = go.Figure()

	fig.add_trace(go.Scatter(x=A[:,0], y=A[:,1],
		name='row_profile',
		mode=row_markers,
		marker_color=("azure"),
		text=row_names,))

	fig.add_trace(go.Scatter(x=B[:,0], y=B[:,1],
		mode=col_markers,
		name='column_profile',
		marker_color=("darkorange"),
		text=col_names))


	# Set options common to all traces with fig.update_traces
	fig.update_traces(marker_line_width=2, 
		marker_size=15,textposition='top center', textfont_color='black',
					textfont_size=18)
	fig.update_layout(title='Principal Coordinates',
		yaxis_zeroline=True, xaxis_zeroline=True, 
		plot_bgcolor='ivory', width=950, height=700,
		yaxis={'visible': True, 'showticklabels':False},xaxis={'visible': True, 'showticklabels':False})
	fig.update_xaxes(zerolinecolor='navy')
	fig.update_yaxes(zerolinecolor='navy')

	return fig

def heatmap(dt):
	r = dt.corr()
	pio.templates.default = "plotly_white"

	mask = np.triu(np.ones_like(r, dtype=bool))
	rLT = r.mask(mask)

	heat  = go.Heatmap(
		z=r.mask(mask),
		x=r.columns,
		y=r.columns,
		colorscale=px.colors.diverging.RdBu,
		zmin=-1,
		zmax=1)

	title = "Heatmap"

	layout = go.Layout(title_text=title,
					        title_x=0.5,
					        width=500,
					        height=500,
					        xaxis_showgrid=False,
					        yaxis_showgrid=False,
					        yaxis_autorange='reversed')

	fig=go.Figure(data=[heat], layout=layout)

	return fig





def pie(dt):
  colors = ['navy', 'darkgreen', 'midnightblue', 'blue', 'green', 'red', 'maroon',
          'yellow', 'violet']

  fig = go.Figure(data=[go.Pie(labels=dt.columns,
                             values=dt.values.flatten().tolist())])
  fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
 # fig.update_layout(paper_bgcolor='ivory')
  return fig

