from datetime import date


def ftext(text_string: str) -> str:
    """Formatea un texto a mayúsculas

    Args:
        text_string (str): Texto a formatear

    Returns:
        str: Texto formateado
    """

    return text_string.upper()


def ftape(machine: str, tape_number: int) -> str:
    """Formatea el número de tape según la máquina

    Args:
        machine (str): Máquina utilizada
        tape_number (int): Número de tape_number

    Returns:
        str: Número de tape formateado
    """

    if machine != "OMNITURN":
        tape_number = str(tape_number)
        if len(tape_number) < 4:
            if machine == "MAZAK":
                while len(tape_number) != 8:
                    tape_number = f"0{tape_number}"
            else:
                while len(tape_number) != 4:
                    tape_number = f"0{tape_number}"

    return tape_number


def foper(operation: str) -> float:
    """Formatea la operación matemática a decimal

    Args:
        operation (str): Operación matemática

    Returns:
        float: Resultado de la operación en decimales
    """

    result = ""
    if operation != "":
        try:
            result = eval(operation)
            result = float(fnum4(result))
        except NameError:
            result = 0
    return result


def fdia(diameter: str) -> str:
    """Formatea un diámetro a 3 decimales

    Args:
        diameter (str): Diámetro a formatear

    Returns:
        str: Diámetro formateado
    """

    diameter = "{0:.3f}".format(float(diameter))

    while True:
        if diameter[0] == "-":
            if diameter[1] != "0":
                break
            diameter = f"-{diameter[2:]}"
        elif diameter[0] != "0":
            break
        else:
            diameter = diameter[1:]
    diameter = "0" if diameter == ".0" else diameter

    return diameter


def fnum3(number_string: str) -> str:
    """Formatea un número a máximo 3 decimales

    Args:
        number_string (str): Número en formato texto

    Returns:
        str: Cadena de texto con formato de 3 decimales
    """

    number_string = "{0:.3f}".format(float(number_string))

    while number_string[-1] == "0" and number_string[-2] != ".":
        number_string = number_string[:-1]

    while True:
        if number_string[0] == "-":
            if number_string[1] != "0":
                break
            number_string = f"-{number_string[2:]}"
        elif number_string[0] != "0":
            break
        else:
            number_string = number_string[1:]
    number_string = "0" if number_string in {".0", "-.0"} else number_string

    return number_string


def fnum4(number_string: str) -> str:
    """Formatea un número a máximo 4 decimales

    Args:
        number_string (str): Número en formato texto

    Returns:
        str: Cadena de texto con formato de 4 decimales
    """

    number_string = "{0:.4f}".format(float(number_string))

    while number_string[-1] == "0" and number_string[-2] != ".":
        number_string = number_string[:-1]

    while True:
        if number_string[0] == "-":
            if number_string[1] != "0":
                break
            number_string = f"-{number_string[2:]}"
        elif number_string[0] != "0":
            break
        else:
            number_string = number_string[1:]
    number_string = "0" if number_string == ".0" else number_string

    return number_string


def fversion() -> str:
    """Formatea la versión del tape

    Returns:
        str: Cadena de texto de versión
    """

    return date.today().strftime("V%m.%d.%y")


def fspace() -> str:
    """Formatea un espacio en blanco

    Returns:
        str: Espacio en blanco
    """

    return " "


def fcom(tool: int, compensations: list) -> float:
    """Formatea la compensación de la herramienta

    Args:
        tool (int): Número de herramienta
        compensations (list): Lista de compensaciones

    Returns:
        float: Valor de la compensación
    """
    return compensations[tool] if tool in compensations else False


def fparam(parameter_value: float) -> str:
    """Formatea un número a parámetro de torno suizo

    Args:
        parameter_value (float): Valor del parámetros

    Returns:
        str: Cadena de texto del parámetro formateado
    """

    parameter_value = str(int(float(fnum3(parameter_value)) * 10000))
    while len(parameter_value) < 10:
        parameter_value = f"0{parameter_value}"
    return parameter_value


def ffed(feed_string: str) -> str:
    """Formatea el valor de avance de corte

    Args:
        feed_string (str): Avance en formato texto del

    Returns:
        str: Avance formateado a máximo 4 decimales
    """

    try:
        feed_string = "{0:.4f}".format(float(feed_string))

        while feed_string[-1] == "0":
            feed_string = feed_string[:-1]

        while feed_string[0] == "0":
            feed_string = feed_string[1:]
    except IndexError:
        feed_string = ".0005"

    feed_string = "0" if feed_string == "." else feed_string

    return feed_string
