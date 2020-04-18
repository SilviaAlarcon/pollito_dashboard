import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['assets/index.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash(__name__)

chick_data = {
    'id': ['1058'],
    'date': ['01/04/2020'],
    'time': ['06:54pm'],
    'gender':['female'],
    'image_name':['opencv_frame_452.png']
}     
app.layout = html.Div(className= 'hero', children = [
        html.Div(className= 'hero-container', children = [
            html.Div(id='header', children=[
                html.Div(className='header-container', children=[
                    html.Img(className= 'logo', src='/assets/Icons/logo.jpeg')]
                        )
                ]),

            html.Div(id='control-buttons', className='buttons-container', children=[
                dcc.RadioItems(
                    id='time_span_options', className='buttons',
                    options=[{'label': 'Last batch','value': 'Last_batch'},
                            {'label': 'Last hour','value': 'Last_hour'}],
                    value= 'Last batch',
                    )]
            ),
            
                
                    
                        html.Div(id='female_counter', className='box-female', children=[
                            html.Strong(children=["5,500"]),
                            html.P("Females"),
                            html.Img(className= 'iconF', src='/assets/Icons/female.svg')]),
                        html.Div(id='male_counter', className='box-male', children=[
                            html.Strong(children=["5,502"]),
                            html.P("Males"),
                            html.Img(className= 'iconM',src='/assets/Icons/male.svg')]),
                        html.Div(id='counter', className='box-chicken', children=[
                            html.Strong(children=["11,002"]),
                            html.P("Chicks"),
                            html.Img(className= 'iconC',src='/assets/Icons/CHICKEN.svg')]),
                    
                html.Div(className='video-container', children=[
                    html.Video(className= 'video', controls = True, id = 'movie_player'),
                ]),    
                
                html.Div(id='sexed-chick-stream', className='side-container', children=[
                    html.Div(className='recently', children=[
                    html.H6("Recently classified"),
                    ]),
                    html.Div(id='chick-1', className='gender', children=[
                        html.P("Today 03:45pm"),
                        html.Strong(children=["Female"], className='badge pink'),
                        html.Img(src='/assets/Streaming/opencv_frame_475.png')
                    ]),
                    html.Div(id='chick-2', className='gender', children=[
                        html.P("Today 03:50pm"),
                        html.Strong(children=["Male"], className='badge blue'),
                        html.Img(src='/assets/Streaming/opencv_frame_475.png')
                    ]),
                    html.Div(id='chick-3', className='gender', children=[
                        html.P("Today 03:50pm"),
                        html.Strong(children=["Male"], className='badge blue'),
                        html.Img(src='/assets/Streaming/opencv_frame_475.png')
                    ])                     
                ]
                )
            
        ])
   ]
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


