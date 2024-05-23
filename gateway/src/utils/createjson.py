def createjson(respuesta): 
    respuesta = respuesta.items()
    temp_operaciones = {}
    for key, value in respuesta:
        key_parts = key.rsplit('-', 1)
        if len(key_parts) == 2:
            key_name, op_index = key_parts
            if op_index not in temp_operaciones:
                temp_operaciones[op_index] = {}
            temp_operaciones[op_index][key_name] = value
    operaciones = list(temp_operaciones.values())
    return operaciones