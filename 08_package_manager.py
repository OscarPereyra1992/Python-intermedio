##Python Package manager##

#Pyp
#https://pypi.org/project/pip/

import numpy
import requests 


numpy_array = numpy.array([1,2,3,4,5])
#print(type(numpy_array))

#print(numpy_array * 2)



response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())