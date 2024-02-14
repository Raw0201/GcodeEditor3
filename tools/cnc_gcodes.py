swiss_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00XnYnZn",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01XnYnZnFn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnYnZnRnInJnKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G03XnYnZnRnInJnKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G04Un",
        "G04 = Tiempo de espera\n\nU = Tiempo en segundos",
    ],
    [
        "G17",
        "G17 = Plano de trabajo XY",
    ],
    [
        "G18",
        "G18 = Plano de trabajo XZ",
    ],
    [
        "G19",
        "G19 = Plano de trabajo YZ",
    ],
    [
        "G40XnYnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnYnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnYnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G50UnWn",
        "G50 = Coordenadas de trabajo\n\nU = Compensación en eje X\nW = Compensación en eje Y",
    ],
    [
        "G80",
        "G80 = Cancela ciclo de perforado o roscado",
    ],
    [
        "G83ZnRnQnFn",
        "G83 = Ciclo de perforado frontal en pasos\n\nZ = Profundidad del agujero\nR = Punto de retracción (salida)\nQ = Profundidad de corte por pasada\nF = Avance de corte",
    ],
    [
        "G88XnRnFnD3Sn,R1",
        "G88 = Ciclo de roscado lateral\n\nX = Posición final eje X\nR = Punto de retracción (salida)\nF = Paso de la rosca\nD3 = Husillo y sentido de giro\nS = Velocidad de rotación\n,R1 = Sincronización",
    ],
    [
        "G90",
        "G90 = Sistema de coordenadas absolutas",
    ],
    [
        "G91",
        "G91 = Sistema de coordenadas incrementales",
    ],
    [
        "G92XnZnFn",
        "G92 = Ciclo de roscado\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nF = Paso de la rosca",
    ],
    [
        "G96",
        "G96 = Velocidad de avance constante de superficie SFM",
    ],
    [
        "G97",
        "G97 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G98",
        "G98 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G99",
        "G99 = Avance de corte en pulgadas por revolución",
    ],
]

kswiss_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00XnYnZn",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01XnYnZnFn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnYnZnRnInJnKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G03XnYnZnRnInJnKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G04Un",
        "G04 = Tiempo de espera\n\nU = Tiempo en segundos",
    ],
    [
        "G17",
        "G17 = Plano de trabajo XY",
    ],
    [
        "G18",
        "G18 = Plano de trabajo XZ",
    ],
    [
        "G19",
        "G19 = Plano de trabajo YZ",
    ],
    [
        "G40XnYnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnYnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnYnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G50UnWn",
        "G50 = Coordenadas de trabajo\n\nU = Compensación en eje X\nW = Compensación en eje Y",
    ],
    [
        "G80",
        "G80 = Cancela ciclo de perforado o roscado",
    ],
    [
        "G83ZnRnQnFn",
        "G83 = Ciclo de perforado frontal en pasos\n\nZ = Profundidad del agujero\nR = Punto de retracción (salida)\nQ = Profundidad de corte por pasada\nF = Avance de corte",
    ],
    [
        "G88XnRnFnD3Sn,R1",
        "G88 = Ciclo de roscado lateral\n\nX = Posición final eje X\nR = Punto de retracción (salida)\nF = Paso de la rosca\nD3 = Husillo y sentido de giro\nS = Velocidad de rotación\n,R1 = Sincronización",
    ],
    [
        "G90",
        "G90 = Sistema de coordenadas absolutas",
    ],
    [
        "G91",
        "G91 = Sistema de coordenadas incrementales",
    ],
    [
        "G92XnZnFn",
        "G92 = Ciclo de roscado\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nF = Paso de la rosca",
    ],
    [
        "G96",
        "G96 = Velocidad de avance constante de superficie SFM",
    ],
    [
        "G97",
        "G97 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G98",
        "G98 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G99",
        "G99 = Avance de corte en pulgadas por revolución",
    ],
    [
        "G600",
        "G600 = Cancela patrones de maquinado",
    ],
    [
        "G610U0",
        "G610 = Maquinado independiente de $1 y $2\n\nU0 = Desplazamiento 0 en eje X2",
    ],
    [
        "G620U0",
        "G620 = Maquinado simultáneo de $1 y $2\n\nU0 = Desplazamiento 0 en eje X2",
    ],
    [
        "G630U0",
        "G630 = Maquinado paralelo $1 y $2\n\nU0 = Desplazamiento 0 en eje X2",
    ],
    [
        "G650U0",
        "G650 = Recolección de parte o soporte de centro\n\nU0 = Desplazamiento 0 en eje X2",
    ],
    [
        "G813",
        "G813 = Desactiva sincronización de giro de husillos",
    ],
    [
        "G814",
        "G814 = Activa sincronización de giro de husillos",
    ],
    [
        "G999",
        "G999 = Ejecuta el último programa",
    ],
]

romi_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00XnZn",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01XnZnFn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnZnRnInKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G03XnZnRnInKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G04Un",
        "G04 = Tiempo de espera\n\nU = Tiempo en segundos",
    ],
    [
        "G10",
        "G10 = Gestor de vida de la herramienta",
    ],
    [
        "G20",
        "G20 = Sistema de dimensiones inglés (pulgadas)",
    ],
    [
        "G21",
        "G21 = Sistema de dimensiones métrico (milímetros)",
    ],
    [
        "G22XnZnInKn",
        "G22 = Área de seguridad\n\nX = Punto inicio eje X\nX = Punto inicio eje Z\nI = Punto final eje X\nK = Punto final eje Z",
    ],
    [
        "G28U0W0",
        "G28 = Retorno de ejes a punto cero máquina\n\nU = Punto cero en eje X\nW = Punto cero en eje Z",
    ],
    [
        "G33XnZnRnFn",
        "G33 = Ciclo de roscado\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nR = Conicidad de la rosca\nF = Paso de la rosca",
    ],
    [
        "G40XnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G63TnAn",
        "G63 = Lector de posición de herramienta (Tool Eye)\n\nT = Número de herramienta\nA = Posición de toque del sensor",
    ],
    [
        "G70PnQn",
        "G70 = Ciclo de acabado\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno",
    ],
    [
        "G71UnRn\nG71PnQnUnWnFn",
        "G71 = Ciclo de desbaste longitudinal\n\nU = Profundidad de corte por pasada\nR = Distancia de seguridad de retracción\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno\nU = Sobrematerial X\nW = Sobrematerial Z\nF = Avance de corte",
    ],
    [
        "G72WnRn\nG72PnQnUnWnFn",
        "G72 = Ciclo de desbaste transversal\n\nW = Profundidad de corte por pasada\nR = Distancia de seguridad de retracción\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno\nU = Sobrematerial X\nW = Sobrematerial Z\nF = Avance de corte",
    ],
    [
        "G73UnWnRn\nG73PnQnUnWnFn",
        "G73 = Ciclo de desbaste paralelo\n\nU = Profundidad de corte por pasada en eje X\nW = Profundidad de corte por pasada en eje Z\nR = Cortes de desbaste\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno\nU = Sobrematerial X\nW = Sobrematerial Z\nF = Avance de corte",
    ],
    [
        "G74Rn\nG74ZnQnFn",
        "G74 = Ciclo de perforado o torneado\n\nR = Retorno incremental para quebrar viruta\n\nZ = Posición final eje Z\nQ = Profundidad de corte por pasada en eje Z\nF = Avance de corte",
    ],
    [
        "G75Rn\nG75XnZnPnQnFn",
        "G75 = Ciclo de ranurado\n\nR = Retorno incremental para quebrar viruta\n\nX = Posición final eje X\nZ = Posición final eje Z\nP = Profundidad de corte por pasada en eje X\nQ = Distancia entre las ranuras\nF = Avance de corte",
    ],
    [
        "G75XnZnPnQnRnFn",
        "G75 = Ciclo de refrentado\n\nX = Posición final eje X\nZ = Posición final eje Z\nP = Profundidad de corte por pasada en eje X\nQ = Profundidad de corte por pasada en eje Z\nR = Distancia de seguridad de retracción\nF = Avance de corte",
    ],
    [
        "G76PmraQnRn\nG76XnZnRnPnQnFn",
        "G76 = Ciclo de roscado automático\n\nP = Parámetros de corte\n   m = Repeticiones último pase\n   r = Longitud de salida angular [(radio / paso) * 10]\n   a = Ángulo de la herramienta\nQ = Profundidad mínima de corte\nR = Profundidad de último pase\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nR = Conicidad incremental eje X\nP = Altura el filo de la rosca\nQ = Profundidad de primera pasada\nF = Paso de la rosca",
    ],
    [
        "G77XnZnRnFn",
        "G77 = Ciclo de torneado paralelo o cónico\n\nX = Diámetro de la primera pasada\nZ = Posición final eje Z\nR = Conicidad incremental en eje X\nF = Avance de corte",
    ],    
    [
        "G78XnZnRnFn",
        "G78 = Ciclo de roscado semiautomático\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nR = Conicidad incremental eje X\nF = Paso de la rosca",
    ],
    [
        "G79XnZnRnFn",
        "G79 = Ciclo de refrentado paralelo o cónico\n\nX = Posición final eje X\nZ = Posición final eje Z\nR = Conicidad incremental en eje X\nF = Avance de corte",
    ],  
    [
        "G80",
        "G80 = Cancela ciclo de perforado o roscado",
    ],
    [
        "G81ZnFn",
        "G81 = Ciclo de perforado sencillo\n\nZ = Posición final eje Z\nF = Avance de corte",
    ],
    [
        "G83ZnQnPnRnFn",
        "G83 = Ciclo de perforado frontal en pasos\n\nZ = Posición final eje Z\nQ = Profundidad de corte por pasada\nP = Tiempo de espera por pasada\nR = Plano de referencia\nF = Avance de corte",
    ],
    [
        "G84ZnFn",
        "G84 = Ciclo de roscado con macho\n\nZ = Posición final eje Z\nF = Paso de la rosca",
    ],
    [
        "G85ZnFn",
        "G85 = Ciclo de rimado\n\nZ = Posición final eje Z\nF = Avance de corte",
    ],
    [
        "G90",
        "G90 = Sistema de coordenadas absolutas",
    ],
    [
        "G91",
        "G91 = Sistema de coordenadas incrementales",
    ],
    [
        "G92S2500M03",
        "G92 = Revoluciones máximas del husillo\n\nS = RPMs\nM03 = Giro del husillo en sentido antihorario",
    ],
    [
        "G94",
        "G94 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G95",
        "G95 = Avance de corte en pulgadas por revolución",
    ],
    [
        "G96Sn\nG92SnM03",
        "G96 = Velocidad de avance constante de superficie SFM\nG92 = Revoluciones máximas del husillo\n\nS = RPMs\nM03 = Giro del husillo en sentido antihorario",
    ],
    [
        "G97SnM03",
        "G97 = Velocidad en revoluciones por minuto RPM\n\nS = RPMs\nM03 = Giro del husillo en sentido antihorario",
    ],
    [
        "G224",
        "G224 = Alimentación de barra con cargador automático",
    ],
    [
        "G225",
        "G225 = Tirador de barra y descarga de pieza",
    ],
]

hardinge_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00XnZn",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01XnZnFn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnZnRnInKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G03XnZnRnInKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nR = Dimensión del radio\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G04Un",
        "G04 = Tiempo de espera\n\nU = Tiempo en segundos",
    ],
    [
        "G10P32U.0001W-.0001",
        "G10 = Contador de partes\n\nP32 = Offset #32\nU = Partes maquinadas\nW = Partes por maquinar",
    ],
    [
        "G20",
        "G20 = Sistema de dimensiones inglés (pulgadas)",
    ],
    [
        "G21",
        "G21 = Sistema de dimensiones métrico (milímetros)",
    ],
    [
        "G32XnZnRnFn",
        "G32 = Roscado en una pasada\n\nZ = Posición final eje Z\nF = Paso de la rosca",
    ],
    [
        "G40XnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G65P9135JnKnBnHnCnAnFn",
        "G65 = Llamada de macro\nP9135 = Macro de perforado profundo\n\nJ = Posición inicial en eje Z\nK = Posición final eje Z\nB = Distancia de seguridad\nH = 1/3 de la profundidad del primer corte\nC = Profundidad mínima de corte\nA = Tiempo de espera en el punto de retracción\nF = Avance de corte",
    ],
    [
        "G65P9136KnBnWnCnAnFn",
        "G65 = Llamada de macro\nP9136 = Macro de perforado profundo\n\nK = Posición final eje Z\nB = Distancia de seguridad\nW = Profundidad del primer corte\nC = Profundidad mínima de corte\nA = Tiempo de espera en el punto de retracción\nF = Avance de corte",
    ],
    [
        "G70PnQn",
        "G70 = Ciclo de acabado\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno",
    ],
    [
        "G71UnRn\nG71PnQnUnWnFn",
        "G71 = Ciclo de desbaste longitudinal\n\nU = Profundidad de corte por pasada\nR = Distancia de seguridad de retracción\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno\nU = Sobrematerial X\nW = Sobrematerial Z\nF = Avance de corte",
    ],
    [
        "G72WnRn\nG72PnQnUnWnFn",
        "G72 = Ciclo de desbaste transversal\n\nW = Profundidad de corte por pasada\nR = Distancia de seguridad de retracción\n\nP = Número de línea de inicio de contorno\nQ = Número de línea de finalización de contorno\nU = Sobrematerial X\nW = Sobrematerial Z\nF = Avance de corte",
    ],
    [
        "G73",
        "G73 = Ciclo de desbaste paralelo",
    ],
    [
        "G74Rn\nG74ZnQnFn",
        "G74 = Ciclo de perforado o torneado\n\nR = Retorno incremental para quebrar viruta\n\nZ = Posición final eje Z\nQ = Profundidad de corte por pasada en eje Z\nF = Avance de corte",
    ],
    [
        "G76PmraQnRn\nG76XnZnRnPnQnFn",
        "G76 = Ciclo de roscado automático\n\nP = Parámetros de corte\n   m = Repeticiones último pase\n   r = Longitud de salida angular [(radio / paso) * 10]\n   a = Ángulo de la herramienta\nQ = Profundidad mínima de corte\nR = Profundidad de último pase\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nR = Conicidad incremental eje X\nP = Altura el filo de la rosca\nQ = Profundidad de primera pasada\nF = Paso de la rosca",
    ],
    [
        "G90",
        "G90 = Ciclo de torneado",
    ],
    [
        "G92",
        "G92 = Ciclo de roscado",
    ],
    [
        "G94",
        "G94 = Ciclo de refrentado",
    ],
    [
        "G96",
        "G96 = Velocidad de avance constante de superficie SFM",
    ],
    [
        "G97SnM03",
        "G97 = Velocidad en revoluciones por minuto RPM\n\nS = RPMs\nM03 = Giro del husillo en sentido antihorario",
    ],
    [
        "G98",
        "G98 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G99",
        "G99 = Avance de corte en pulgadas por revolución",
    ],
]

omni_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00XnZn",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01XnZnFn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnZnInKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G03XnZnInKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nZ = Punto final en eje Z\nI = Punto centro en eje X\nK = Punto centro en eje Z",
    ],
    [
        "G04Fn",
        "G04 = Tiempo de espera\n\nF = Tiempo en segundos",
    ],
    [
        "G10UnWn",
        "G10 = Coordenadas de trabajo\n\nU = Compensación en eje X\nW = Compensación en eje Y",
    ],
    [
        "G33XnZnInKnAnPnCnO",
        "G33 = Ciclo de roscado\n\nX = Diámetro del núcleo de la rosca\nZ = Posición final eje Z\nI = Profundidad de corte\nK = Paso de la rosca\nA = Conicidad de la rosca\nP = Salida de la rosca\nC = Ángulo de entrada\nO = Repaso de acabado",
    ],
    [
        "G34ZnInKnAnPn",
        "G33 = Ciclo de roscado de una pasada\n\nZ = Posición final eje Z\nI = Profundidad de corte\nK = Paso de la rosca\nA = Conicidad de la rosca\nP = Salida de la rosca",
    ],
    [
        "G40XnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G70",
        "G70 = Sistema de dimensiones inglés (pulgadas)",
    ],
    [
        "G71",
        "G71 = Sistema de dimensiones métrico (milímetros)",
    ],
    [
        "G72",
        "G72 = Sistema de dimensiones al diámetro",
    ],
    [
        "G73",
        "G73 = Sistema de dimensiones al radio",
    ],
    [
        "G74XnZnInUnFn",
        "G74 = Ciclo de desbaste en caja\n\nX = Diámetro a tornear\nZ = Longitud a tornear\nI = Profundidad por corte\nU = Sobrematerial para acabado\nF = Avance de corte",
    ],
    [
        "G76",
        "G76 = Revoluciones mínimas con G96 activado",
    ],
    [
        "G77",
        "G77 = Revoluciones máximas con G96 activado",
    ],
    [
        "G78XnZnInUnFn",
        "G78 = Ciclo de desbaste en caja al contorno\n\nU = Sobrematerial para acabado\nP = Subrutina\nF = Avance de corte",
    ],
    [
        "G80",
        "G80 = Cancela ciclo de perforado o roscado",
    ],
    [
        "G81ZnFn",
        "G81 = Ciclo de perforado sencillo\n\nZ = Profundidad del agujero\nF = Avance de corte",
    ],
    [
        "G83ZnKnRnLnCnFn",
        "G83 = Ciclo de perforado frontal en pasos\n\nZ = Profundidad del agujero\nK = Profundidad de corte por pasada\nR = Punto de retracción (salida)\nL = Avance de retracción\nC = Distancia de seguridad\nF = Avance de corte",
    ],
    [
        "G90",
        "G90 = Sistema de coordenadas absolutas",
    ],
    [
        "G91",
        "G91 = Sistema de coordenadas incrementales",
    ],
    [
        "G92XnZn",
        "G92 = Posicionamiento inicial de herramienta\nX = Posición inicial eje X\nZ = Posición inicial eje Z",
    ],
    [
        "G94",
        "G94 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G95",
        "G95 = Avance de corte en pulgadas por revolución",
    ],
    [
        "G96",
        "G96 = Velocidad de avance constante de superficie SFM",
    ],
    [
        "G97",
        "G97 = Velocidad en revoluciones por minuto RPM",
    ],
]

mill_g_codes = [
    ["Cód", "Descripción"],
    [
        "G00X0Y0Z0",
        "G00 = Movimiento con avance rápido\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G01X0Y0Z0Fn",
        "G01 = Movimiento con avance controlado\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z\nF = Avance de corte",
    ],
    [
        "G02XnYnZnInJnKn",
        "G02 = Arco en sentido horario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G03XnYnZnInJnKn",
        "G03 = Arco en sentido antihorario\n\nX = Punto final en eje X\nY = Punto final en eje Y\nZ = Punto final en eje Z\nI = Punto centro en eje X\nJ = Punto centro en eje Y\nK = Punto centro en eje Z",
    ],
    [
        "G04Un",
        "G04 = Tiempo de espera\n\nU = Tiempo en segundos",
    ],
    [
        "G17",
        "G17 = Plano de trabajo XY",
    ],
    [
        "G18",
        "G18 = Plano de trabajo XZ",
    ],
    [
        "G19",
        "G19 = Plano de trabajo YZ",
    ],
    [
        "G20",
        "G20 = Sistema de dimensiones inglés (pulgadas)",
    ],
    [
        "G21",
        "G21 = Sistema de dimensiones métrico (milímetros)",
    ],
    [
        "G40XnYnZn",
        "G40 = Cancela compensación de radio de la herramienta\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G41XnYnZn",
        "G41 = Compensación de radio de la herramienta a la izquierda\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G42XnYnZn",
        "G42 = Compensación de radio de la herramienta a la derecha\n\nX = Desplazamiento en eje X\nY = Desplazamiento en eje Y\nZ = Desplazamiento en eje Z",
    ],
    [
        "G43",
        "G43 = Compensación de largo de la herramienta hacia arriba",
    ],
    [
        "G44",
        "G44 = Compensación de largo de la herramienta hacia abajo",
    ],
    [
        "G49",
        "G49 = Cancela compensación de largo de la herramienta",
    ],
    [
        "G52",
        "G52 = Sistema de coordenadas",
    ],
    [
        "G53",
        "G53 = Sistema de coordenadas de la máquina",
    ],
    [
        "G54",
        "G54 = Sistema de coordenadas 1 (Plato 30 piezas)",
    ],
    [
        "G55",
        "G55 = Sistema de coordenadas 2 (Prensa precisión)",
    ],
    [
        "G56",
        "G56 = Sistema de coordenadas 3 (Prensa precisión)",
    ],
    [
        "G57",
        "G57 = Sistema de coordenadas 4 (Aparato divisor)",
    ],
    [
        "G58",
        "G58 = Sistema de coordenadas 5 (Aparato divisor)",
    ],
    [
        "G59",
        "G59 = Sistema de coordenadas 6 (Base racks)",
    ],
    [
        "G73XnYnZnRnQnFn",
        "G73 = Ciclo de perforado rápido en pasos\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nQ = Profundidad de corte por pasada\nF = Avance de corte",
    ],
    [
        "G74XnYnZnRnFn",
        "G74 = Ciclo de roscado izquierdo con macho\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nF = Paso de la rosca",
    ],
    [
        "G75",
        "G75 = Ciclo de torneado desbaste",
    ],
    [
        "G76XnYnZnRnQnFn",
        "G76 = Alisado sin giro en retroceso\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nQ = Punto de retracción diametral\nF = Paso de la rosca",
    ],
    [
        "G77",
        "G77 = Ciclo de torneado reversa",
    ],
    [
        "G78",
        "G78 = Ciclo de torneado externo",
    ],
    [
        "G79",
        "G79 = Ciclo de torneado externo",
    ],
    [
        "G80",
        "G80 = Cancela ciclos de perforado",
    ],
    [
        "G81XnYnZnRnFn",
        "G81 = Ciclo de punteado\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nF = Avance de corte",
    ],
    [
        "G82XnYnZnRnEnFn",
        "G82 = Ciclo de perforado con tiempo de espera\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nE = Tiempo de espera (s * 1000)\nF = Avance de corte",
    ],
    [
        "G83XnYnZnRnQnFn",
        "G83 = Ciclo de perforado en pasos\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nQ = Profundidad de corte por pasada\nF = Avance de corte",
    ],
    [
        "G84XnYnZnRnFn",
        "G84 = Ciclo de roscado con macho\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nF = Paso de la rosca",
    ],
    [
        "G85XnYnZnRnFn",
        "G85 = Alisado con avance en retroceso\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nF = Paso de la rosca",
    ],
    [
        "G86XnYnZnRnFn",
        "G86 = Alisado sin giro en retroceso\n\nX = Posición eje X\nY = Posición eje Y\nZ = Posición final eje Z\nR = Punto de retracción\nF = Paso de la rosca",
    ],
    [
        "G87",
        "G87 = Ciclo de torneado interno en reversa",
    ],
    [
        "G88",
        "G88 = Ciclo de torneado interno con tiempo de espera",
    ],
    [
        "G89",
        "G89 = Ciclo de torneado interno con tiempo de espera",
    ],
    [
        "G90",
        "G90 = Sistema de coordenadas absolutas",
    ],
    [
        "G91",
        "G91 = Sistema de coordenadas incrementales",
    ],
    [
        "G92",
        "G92 = Sistema de coordenadas de máquina",
    ],
    [
        "G94",
        "G94 = Avance de corte en pulgadas por minuto",
    ],
    [
        "G95",
        "G95 = Avance de corte en pulgadas por revolución",
    ],
    [
        "G98",
        "G98 = Desplazamiento a Z inicial en cada paso en ciclos de perforado",
    ],
    [
        "G99",
        "G99 = Desplazamiento a punto R en cada paso en ciclos de perforado",
    ],
]
