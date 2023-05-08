from kivy.app import App
from kivy.base import Builder
#pip3 install kivy_garden.mapview
class m(App):
    def build(self):
        return      Builder.load_string("""
#:import MapView kivy_garden.mapview.MapView
MapView:
    id: mapview
    lat: 50.6394
    lon: 3.057
    zoom: 2     
        """)
m().run()