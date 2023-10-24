import json, logging

current_template:dict = {}
template_name:str
logging.basicConfig(filename="logs.txt", level=logging.FATAL)

def set_current_template(path:str):
    template_file = open("path")
    template_name = template_file.name
    current_template = json.load(template_file)

    # checking if the object is from an env_template

    try:
        if not current_template["has_precipitation"].isinstance(bool): is_an_env_template = False
        if not current_template["temperature"].isinstance(float): is_an_env_template = False
        if not current_template["downfall"].isinstance(float): is_an_env_template = False
        if not current_template["effects"]["fog_color"].isinstance(int): is_an_env_template = False
        if not current_template["effects"]["sky_color"].isinstance(int): is_an_env_template = False
        if not current_template["effects"]["water_color"].isinstance(int): is_an_env_template = False
        if not current_template["effects"]["water_fog_color"].isinstance(int): is_an_env_template = False
    except KeyError:
        is_an_env_template = False

def template_key_checking(key:object, intance_of:type):
    try:
        if not isinstance(key, intance_of): raise TypeError
    except Exception as e:
        if isinstance(e, TypeError):
            logging.fatal("MissTyped |" + str(key) + "| is not of type " + str(intance_of) + " in \"" + template_name + ".json\"")
            raise e
        if isinstance(e, KeyError):
            logging.fatal("The json variable |" + str(key) + "| does not exist and should")
            raise e
