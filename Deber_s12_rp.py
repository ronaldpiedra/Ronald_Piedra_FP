#deber semana núnero 12

temperaturas = [
    [   # Ciudad 1
         [  # Semana 1
         {"day": "lunes", "temp": 45},
         {"day": "martes", "temp": 78},
         {"day": "miércoles", "temp": 34},
         {"day": "jueves", "temp": 53},
         {"day": "viernes", "temp": 34},
         {"day": "sábado", "temp": 76},
         {"day": "domingo", "temp": 55}
         ],
         [  # Semana 2
            {"day": "lunes", "temp": 76},
            {"day": "martes", "temp": 67},
            {"day": "miércoles", "temp": 89},
            {"day": "jueves", "temp": 45},
            {"day": "viernes", "temp": 78},
            {"day": "sábado", "temp": 65},
            {"day": "domingo", "temp": 90}
        ],
         [  # Semana 3
            {"day": "lunes", "temp": 74},
            {"day": "martes", "temp": 65},
            {"day": "miércoles", "temp": 69},
            {"day": "jueves", "temp": 65},
            {"day": "viernes", "temp": 38},
            {"day": "sábado", "temp": 75},
            {"day": "domingo", "temp": 30}
        ],
         [  # Semana 4
            {"day": "lunes", "temp": 47},
            {"day": "martes", "temp": 56},
            {"day": "miércoles", "temp": 39},
            {"day": "jueves", "temp": 55},
            {"day": "viernes", "temp": 28},
            {"day": "sábado", "temp": 55},
            {"day": "domingo", "temp": 60}
        ]
    ],
    [  # Ciudad 2
       [  # Semana 1
           {"day": "lunes", "temp": 37},
           {"day": "martes", "temp": 26},
           {"day": "miércoles", "temp": 19},
           {"day": "jueves", "temp": 65},
           {"day": "viernes", "temp": 78},
           {"day": "sábado", "temp": 85},
           {"day": "domingo", "temp": 90}
    ],
        [  #Semana 2
        {"day": "lunes", "temp": 34},
        {"day": "martes", "temp": 56},
        {"day": "miércoles", "temp": 78},
        {"day": "jueves", "temp": 98},
        {"day": "viernes", "temp": 65},
        {"day": "sábado", "temp": 58},
        {"day": "domingo", "temp": 29}
    ],
        [  #Semana 3
        {"day": "lunes", "temp": 76},
        {"day": "martes", "temp": 36},
        {"day": "miércoles", "temp": 18},
        {"day": "jueves", "temp": 92},
        {"day": "viernes", "temp": 35},
        {"day": "sábado", "temp": 78},
        {"day": "domingo", "temp": 19}
    ],
        [   #Semana 4
        {"day":  "lunes", "temp": 76},
        {"day": "martes", "temp": 36},
        {"day": "miércoles", "temp": 18},
        {"day": "jueves", "temp": 92},
        {"day": "viernes", "temp": 35},
        {"day": "sábado", "temp": 78},
        {"day": "domingo", "temp": 19}
    ]
],

    [ # Ciudad 3
        [   #Semana 1
        {"day": "lunes", "temp": 98},
        {"day": "martes", "temp": 65},
        {"day": "miércoles", "temp": 43},
        {"day": "jueves", "temp": 23},
        {"day": "viernes", "temp": 98},
        {"day": "sábado", "temp": 29},
        {"day": "domingo", "temp": 64}
    ],
        [ #semana 2
        {"day": "lunes", "temp": 33},
        {"day": "martes", "temp": 32},
        {"day": "miércoles", "temp":32},
        {"day": "jueves", "temp": 55},
        {"day": "viernes", "temp": 66},
        {"day": "sábado", "temp":77},
        {"day": "domingo", "temp": 28}

    ],
        [ #Semana 3
        {"day": "lunes", "temp": 44},
        {"day": "martes", "temp": 99},
        {"day": "miércoles", "temp":45},
        {"day": "jueves", "temp": 46},
        {"day": "viernes", "temp": 76},
        {"day": "sábado", "temp":73},
        {"day": "domingo", "temp": 22}
    ],
        [ #Semana 4
        {"day": "lunes", "temp": 88},
        {"day": "martes", "temp": 54},
        {"day": "miércoles", "temp":78},
        {"day": "jueves", "temp": 20},
        {"day": "viernes", "temp": 28},
        {"day": "sábado", "temp":29},
        {"day": "domingo", "temp": 30}


        ]
      ]
     ]

     #Calcular el promedio de la temperatura para cada ciudad y cada semana

     ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
     for ciudad_idx, ciudad  in enumerate (temperaturas):
         for semana_idx, semana in enumerate (ciudad):
             suma_temperaturas = sum ([dia["temp"] for dia in semana])
             promedio = suma_temperaturas / len(semana)
             print (f"Promedio de temperaturas en {ciudades [ciudad_idx]}, Semana {semana_idx + 1}:{promedio:.2f} grados")
