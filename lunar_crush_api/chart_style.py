import plotly.graph_objects as go

def apply_common_layout(fig):
    common_layout = {
        'title_font': {'size': 24, 'color': 'black', 'family': "Arial"},
        'font': {'size': 16, 'color': 'black', 'family': "Arial"},
        'hovermode': 'closest',
        'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50},
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'showlegend': True,
        'legend': {'x': 0.5, 'xanchor': 'center', 'y': -0.2, 'yanchor': 'top', 'orientation': 'h'}
    }
    fig.update_layout(common_layout)
    
    # Apply hoverlabel to non-Indicator traces
    for trace in fig.data:
        if isinstance(trace, (go.Scatter, go.Bar, go.Box, go.Violin)):
            trace.update(hoverlabel=dict(
                bgcolor="white",
                font_size=16,
                font_family="Arial"
            ))
    
    # Update axis titles only if they are not already set
    if fig.layout.xaxis.title.text is None:
        fig.update_layout(xaxis_title='X Axis Title')
    if fig.layout.yaxis.title.text is None:
        fig.update_layout(yaxis_title='Y Axis Title')
    
    return fig
