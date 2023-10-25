import json, logging

current_template:dict = {}
logging.basicConfig(filename="logs.txt", level=logging.FATAL)


def template_key_checking(key:object, intance_of:type, template_name:str):
    """
    Help checking the validity of necessary json variable of a biome_env_template json file.

    Return useful error message and log when the user will misstype something in env_template
    """

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
    """
    set the current_template of the module to the file "path" point to

    does a basic checking to see if a biome JSON file would work in a datapack if the current_template is used
    """

    template_file = open("path")
    template_name = template_file.name
    current_template = json.load(template_file)

    # checking if the object is from a valid env_template

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


def create_biome(biome_path_list:list[str]):
    # copy current template
    # get order.json (make sure it exists)
    # create a features object to store all the features
    # for loop for every line in order list
    # give the cat path and the allowed_downfall/temperature of the template and the to a featurelist method that fill the featurelist object
    # get back the feature object and use the method to get the formated list
    # push the list to the current template 
    # create a json with a name to the bte/data/worldgen/biome/ dir and add the biome file path to biome_path_list
    pass
