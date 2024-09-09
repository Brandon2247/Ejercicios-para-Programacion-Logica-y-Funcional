inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
             {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
             {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
             {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
             {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'},]

def añadirprecio(inmueble):
    precio = (inmueble['metros']*1000 + inmueble['habitaciones']* 500 + int(inmueble['garaje']) * 15000) * (1 - (2020 - inmueble['año'])/100)
    if inmueble['zona'] == 'B':
        precio *= 1.5
    inmueble['precio'] = precio
    return inmueble

def buscarInmuebles(inmuebles, presupuesto):
    def filtro(inmueble):
        return inmueble['precio'] <= presupuesto
    return list(filter(filtro, map(añadirprecio, inmuebles)))

print(buscarInmuebles(inmuebles, 15000))