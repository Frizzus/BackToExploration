import json, logging

current_template:dict = {}
template_name:str
logging.basicConfig(filename="logs.txt", level=logging.FATAL)


def template_key_checking(key:object, intance_of:type, template_name:str):
    type_message = "MissTyped |" + str(key) + "| is not of type " + str(intance_of) + " in \"" + template_name + ".json\""
    key_message = "The json variable |" + str(key) + "| does not exist and should"

    try:
        acces_test = key
        del acces_test
    except KeyError:
        logging.fatal(key_message)
        raise KeyError(key_message)

    if not isinstance(key, intance_of):
        logging.fatal(type_message)
        raise TypeError(type_message)


def set_current_template(path:str):
    template_file = open("path")
    template_name = template_file.name
    current_template = json.load(template_file)

    # checking if the object is from an env_template

    template_key_checking(current_template["has_precipitation"], bool, template_name)
    template_key_checking(current_template["temperature"], float, template_name)
    template_key_checking(current_template["downfall"], float, template_name)
    template_key_checking(current_template["effects"]["sky_color"], int, template_name)
    template_key_checking(current_template["effects"]["water_color"], int, template_name)
    template_key_checking(current_template["effects"]["water_fog_color"], int, template_name)
    template_key_checking(current_template["carvers"], dict, template_name)
    template_key_checking(current_template["features"], list, template_name)
    template_key_checking(current_template["spawners"], dict, template_name)
    template_key_checking(current_template["spawn_costs"], dict, template_name)
