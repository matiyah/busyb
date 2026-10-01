# -*- coding: utf-8 -*-
# Mexican Spanish, derived from the Spain text with vocabulary swaps.
import tr_es
SWAPS = [
 ("Compra, Niños, Casa, Trabajo", "Súper, Niños, Hogar, Trabajo"),
 ("Papeles del colegio", "Papeles de la escuela"),
 ("añade recoger la tintorería mañana a Casa", "agrega recoger la tintorería mañana a Hogar"),
 ("Añádelo con la voz", "Agrégalo con la voz"),
 ("«añade una tarea", "«agrega una tarea"),
 ("barra de añadir", "barra de agregar"),
 ("Añade en el teléfono", "Agrega en el teléfono"),
 ("añadir con un solo pulgar", "agregar con un solo pulgar"),
 ("añade tres usos", "agrega tres usos"),
 ("Busy B Pro añade", "Busy B Pro agrega"),
 ("merece la pena mirar", "vale la pena revisar"),
 ("habitaciones dentro de ellas", "cuartos dentro de ellas"),
 ("en Ajustes", "en Configuración"),
 ("Mosaicos para el día", "Tarjetas para el día"),
 ("los mosaicos Lista general", "los recuadros Lista general"),
 ("Prioritarias sobre las categorías fijadas", "Prioritarias sobre las categorías fijadas"),
 ("a quienes hacen", "a quienes hacen"),
 ("Hoy y Mañana", "Hoy y Mañana"),
 ("la semana que viene", "la próxima semana"),
 ("Una app de iPad de verdad", "Una verdadera app de iPad"),
]
T = []
for s in tr_es.T:
    for a, b in SWAPS:
        s = s.replace(a, b)
    T.append(s)
