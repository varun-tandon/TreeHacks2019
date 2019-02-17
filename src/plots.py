import plotly as py
import plotly.graph_objs as go

print(py.__version__)

def sentimentChart(dates, votes):
    #dates is a list, votes is a 2d list

    top_labels = ['Support', 'Neutral', 'Oppose']

    colors = ['rgba(56, 142, 60, 1)', 'rgba(69, 90, 100, 1)',
              'rgba(211, 47, 47, 1)']

    x_data = [votes[0],
              votes[1],
              votes[2],
              votes[3]]

    y_data = [dates[0],
              dates[1], dates[2],
              dates[3]]


    traces = []

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            traces.append(go.Bar(
                name=top_labels[i],
                x=[xd[i]],
                y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(
                            color='rgb(248, 248, 249)',
                            width=1)
                )
            ))

    layout = go.Layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(
            l=120,
            r=10,
            t=140,
            b=80
        ),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=14,
                                              color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
                # labeling the rest of percentages for each bar (x_axis)
                annotations.append(dict(xref='x', yref='y',
                                        x=space + (xd[i]/2), y=yd,
                                        text=str(xd[i]) + '%',
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(248, 248, 255)'),
                                        showarrow=False))
                # labeling the Likert scale
                if yd == y_data[-1]:
                    annotations.append(dict(xref='x', yref='paper',
                                            x=space + (xd[i]/2), y=1.1,
                                            text=top_labels[i],
                                            font=dict(family='Arial', size=14,
                                                      color='rgb(67, 67, 67)'),
                                            showarrow=False))
                space += xd[i]

    layout['annotations'] = annotations

    fig = go.Figure(data=traces, layout=layout)
    py.offline.plot(fig, filename='bar-colorscale')
