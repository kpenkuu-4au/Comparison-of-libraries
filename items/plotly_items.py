import plotly.graph_objects as g
import plotly.express as px
from files import data_read as r

# fig1 = go.Figure(
#     [go.Bar(
#         x=r.device[:13],
#         y=r.num_app[:13],
#         text=r.gender[:13],
#         textposition='auto'
#     )]
# )
# fig1.update_layout(
#     title="Number of Apps Installed by Devise Model",
#     xaxis_title="Device Model",
#     yaxis_title="Number of Apps Installed"
# )
# fig1.show()

# fig2 = go.Figure(data=go.Scatter(
#     x=r.users[:15],
#     y=r.screen[:15],
#     mode='lines+markers'
# ))
# fig2.update_layout(
#     title="Screen On Time by users",
#     xaxis_title="User ID",
#     yaxis_title="Screen On Time (hours/day)"
# )
# fig2.show()

fig3 = go.Figure(data=[go.Pi])