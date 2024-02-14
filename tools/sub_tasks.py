from subtasks import (
    header,
    header_sub,
    free,
    comment,
    subroutine,
    collect,
    end,
    tool_call,
    tool_close,
    spindle,
    spindle_index,
    misc,
    turn_ini,
    lineal_turn,
    radial_turn,
    thread,
    cutoff,
    rough_turn_cycle,
    rough_turn_cycle_end,
    mill_ini,
    mill_end,
    lineal_mill,
    radial_mill,
    sub_matrix,
    drill_ini,
    drill_end,
    center_drill,
    drill,
    csink,
    tapping,
    flat_mill,
    face_mill,
    facing_mill,
    slotting_mill,
    platter_data,
    call_square,
    call_flatten,
    flatten_sub,
    call_lineal_x,
    lineal_rgh_x_sub,
    call_lineal_y,
    lineal_rgh_y_sub,
)

main_space = " " * 0
head_space = " " * 4
oper_space = " " * 8

tasks_list = {
    "Header": {
        "Name": header.Header,
        "Description": f"{main_space}Inicio de programa",
    },
    "Header_sub": {
        "Name": header_sub.Header_sub,
        "Description": f"{main_space}Inicio de subrutina",
    },
    "Free": {
        "Name": free.Free,
        "Description": " ",
    },
    "Comment": {
        "Name": comment.Comment,
        "Description": f"{oper_space}Comentario",
    },
    "Subroutine": {
        "Name": subroutine.Subroutine,
        "Description": f"{oper_space}-> Subrutina",
    },
    "Collect": {
        "Name": collect.Collect,
        "Description": f"{oper_space}Recolectar pieza",
    },
    "End": {
        "Name": end.End,
        "Description": f"{main_space}Fin de programa",
    },
    "Tool_call": {
        "Name": tool_call.Tool_call,
        "Description": f"{head_space}Llamar herramienta",
    },
    "Tool_close": {
        "Name": tool_close.Tool_close,
        "Description": f"{head_space}Cerrar herramienta",
    },
    "Spindle": {
        "Name": spindle.Spindle,
        "Description": f"{oper_space}Giro del husillo",
    },
    "Spindle_index": {
        "Name": spindle_index.Spindle_index,
        "Description": f"{oper_space}Orientar husillo",
    },
    "Misc": {
        "Name": misc.Misc,
        "Description": f"{oper_space}Funciones misceláneas",
    },
    "Turn_ini": {
        "Name": turn_ini.Turn_ini,
        "Description": f"{head_space}* Iniciar torneados",
    },
    "Lineal_turn": {
        "Name": lineal_turn.Lineal_turn,
        "Description": f"{oper_space}Torneado lineal",
    },
    "Radial_turn": {
        "Name": radial_turn.Radial_turn,
        "Description": f"{oper_space}Torneado radial",
    },
    "Thread": {
        "Name": thread.Thread,
        "Description": f"{oper_space}Ciclo roscado",
    },
    "Cutoff": {
        "Name": cutoff.Cutoff,
        "Description": f"{oper_space}Tronzado de pieza",
    },
    "Rough_turn_cycle": {
        "Name": rough_turn_cycle.Rough_turn_cycle,
        "Description": f"{oper_space}Ciclo de torneado desbaste",
    },
    "Rough_turn_cycle_end": {
        "Name": rough_turn_cycle_end.Rough_turn_cycle_end,
        "Description": f"{oper_space}Finalizar ciclo de torneado desbaste",
    },
    "Mill_ini": {
        "Name": mill_ini.Mill_ini,
        "Description": f"{head_space}* Iniciar fresados",
    },
    "Mill_end": {
        "Name": mill_end.Mill_end,
        "Description": f"{head_space}* Finalizar fresados",
    },
    "Lineal_mill": {
        "Name": lineal_mill.Lineal_mill,
        "Description": f"{oper_space}Fresado lineal",
    },
    "Radial_mill": {
        "Name": radial_mill.Radial_mill,
        "Description": f"{oper_space}Fresado radial",
    },
    "Sub_matrix": {
        "Name": sub_matrix.Sub_matrix,
        "Description": f"{oper_space}Línea subrutinas",
    },
    "Drill_ini": {
        "Name": drill_ini.Drill_ini,
        "Description": f"{head_space}* Iniciar perforados",
    },
    "Drill_end": {
        "Name": drill_end.Drill_end,
        "Description": f"{head_space}* Finalizar perforados",
    },
    "Center_drill": {
        "Name": center_drill.Center_drill,
        "Description": f"{oper_space}Agujero centro",
    },
    "Drill": {
        "Name": drill.Drill,
        "Description": f"{oper_space}Perforado",
    },
    "Csink": {
        "Name": csink.Csink,
        "Description": f"{oper_space}Avellanado",
    },
    "Tapping": {
        "Name": tapping.Tapping,
        "Description": f"{oper_space}Roscado rígido",
    },
    "Flat_mill": {
        "Name": flat_mill.Flat_mill,
        "Description": f"{oper_space}Fresado paleta",
    },
    "Face_mill": {
        "Name": face_mill.Face_mill,
        "Description": f"{oper_space}Fresado caras",
    },
    "Facing_mill": {
        "Name": facing_mill.Facing_mill,
        "Description": f"{oper_space}Refrentado",
    },
    "Slotting_mill": {
        "Name": slotting_mill.Slotting_mill,
        "Description": f"{oper_space}Ranurado",
    },
    "Platter_data": {
        "Name": platter_data.Platter_data,
        "Description": f"{oper_space}Datos de platina",
    },
    "Call_square": {
        "Name": call_square.Call_square,
        "Description": f"{oper_space}Llamar cuadrícula",
    },
    "Call_flatten": {
        "Name": call_flatten.Call_flatten,
        "Description": f"{oper_space}Llamar refrentado platina",
    },
    "Flatten_sub": {
        "Name": flatten_sub.Flatten_sub,
        "Description": f"{oper_space}Subrutina refrentado",
    },
    "Call_lineal_x": {
        "Name": call_lineal_x.Call_lineal_x,
        "Description": f"{oper_space}Desbaste lineal X",
    },
    "Lineal_rgh_x_sub": {
        "Name": lineal_rgh_x_sub.Lineal_rgh_x_sub,
        "Description": f"{oper_space}Subrutina desbaste lineal X",
    },
    "Call_lineal_y": {
        "Name": call_lineal_y.Call_lineal_y,
        "Description": f"{oper_space}Desbaste lineal Y",
    },
    "Lineal_rgh_y_sub": {
        "Name": lineal_rgh_y_sub.Lineal_rgh_y_sub,
        "Description": f"{oper_space}Subrutina desbaste lineal Y",
    },
}


def get_task_class(description: str) -> object:
    """Obtiene la clase de la sub tarea

    Args:
        description (str): Descripción de la sub tarea

    Returns:
        object: Clase de la sub tarea
    """

    main_values = list(tasks_list.values())

    names_list, descriptions_list = [], []
    for dictionary in main_values:
        names_list.append(dictionary["Name"])
        descriptions_list.append(dictionary["Description"])

    description_index = descriptions_list.index(description)

    return names_list[description_index]
