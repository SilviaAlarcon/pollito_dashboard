import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

chick_data = {
    'id': ['1058'],
    'date': ['01/04/2020'],
    'time': ['06:54pm'],
    'gender':['female'],
    'image_name':['opencv_frame_452.png']
}
app.layout = html.Div([
        html.Div(id='header', children=[
            html.H3(children=["PARVADA"], style={'color':'white'})],
                 style={'background-color':'purple'}
                 ),
        html.Div(id='control-buttons', children=[
            dcc.RadioItems(
                id='time_span_options',
                options=[{'label': 'Last batch','value': 'Last_batch'},
                         {'label': 'Last hour','value': 'Last_hour'}],
                value= 'Last batch',
                labelStyle={'display':'inline-block'},
                )], style= {'textAlign':'right', 'padding-right':'13%', 'padding-bottom':'3%', 'padding-top':'1%'}
        ),
        html.Div(id='content-wrapper', children=[
            html.Div(id='left-content-wrapper', children=[
                html.Div(id='counters', children=[
                    html.Div(id='female_counter', children=[
                        html.Img(src='/assets/Icons/female.png', width='90%'),
                        html.Strong(children=["5,500"], style={'left-padding':'49%'}),
                        html.P("Females")],style={'width':'30%','text-align':'center','display':'inline-block'}),
                    html.Div(id='male_counter',children=[
                        html.Img(src='/assets/Icons/male.png', width='90%'),
                        html.Strong(children=["5,502"], style={'left-padding':'49%'}),
                        html.P("Males")],style={'width':'30%','text-align':'center','display':'inline-block'}),
                    html.Div(id='counter',children=[
                        html.Img(src='/assets/Icons/chick.png', width='80%'),
                        html.Strong(children=["11,002"], style={'left-padding':'49%'}),
                        html.P("Chicks")],style={'width':'30%','text-align':'center','display':'inline-block'})
                ],style={'display':'inline-block','width':'100%','padding-bottom':'3%'}),
                html.Img(src='/assets/Best_pic/best_pic_pollito.png', width='80%')
            ], style={'width': '70%', 'display':'inline-block'}),
            html.Div(id='sexed-chick-stream', children=[
                html.H6("Recently classified"),
                html.Div(id='chick-1', children=[
                    html.P("Today 03:45pm", style={'padding-right':'40%'}),
                    html.Strong(children=["Female"], className='label-female', style={'padding-right':'70%'}),
                    html.Img(src='/assets/Streaming/opencv_frame_475.png', style={'width': '100%'})
                ],style={'width':'100%', 'padding-bottom':'8%', 'border-top':'1px solid purple'}),
                 html.Div(id='chick-2', children=[
                    html.P("Today 03:50pm", style={'padding-right':'40%'}),
                    html.Strong(children=["Male"], className='label-male', style={'padding-right':'70%'}),
                    html.Img(src='/assets/Streaming/opencv_frame_475.png', style={'width': '100%'})
                ],style={'width':'100%', 'padding-bottom':'8%', 'border-top':'1px solid purple'})
               ]
            ,style={'width': '28%', 'display':'inline-block', 'border-style':'solid', 'textAlign':'center','vertical-align':'top'})
        ],style={'display':'inline-block','width':'80%','padding-left':'10%'})
   ],style={'width':'100%'}
)



'''
@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')])
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )
'''

if __name__ == '__main__':
    app.run_server(debug=True)

