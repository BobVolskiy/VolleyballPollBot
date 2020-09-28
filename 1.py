
from pyowm import OWM

owm = OWM('c30a0f10eeb9a93501989842cfd6bb23')

mgr = owm.weather_manager()
observation = mgr.weather_at_place('Kyiv')
w = observation.weather

print(w.temperature('celsius')) 
