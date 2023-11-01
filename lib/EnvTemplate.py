import json, logging, copy
from lib.FeatureList import FeatureList

logging.basicConfig(filename="logs.txt", level=logging.FATAL)

class EnvTemplate:
    def __init__(self) -> None:
        self.current_template:dict = {}
        self.biome_counter:int = 0

    def set_current_template(self, path_to_template):
        """
        set the current_template of the module to the file "path" point to

        does a basic checking to see if a biome JSON file would work in a datapack if the current_template is used
        """

        template_file = open(path_to_template, "r")
        template_name = template_file.name
        self.current_template = json.load(template_file)
        template_file.close()

        # checking if the object is from a valid env_template

        template_key_checking(self.current_template["has_precipitation"], bool, template_name)
        template_key_checking(self.current_template["temperature"], float, template_name)
        template_key_checking(self.current_template["downfall"], float, template_name)
        template_key_checking(self.current_template["effects"]["sky_color"], int, template_name)
        template_key_checking(self.current_template["effects"]["water_color"], int, template_name)
        template_key_checking(self.current_template["effects"]["water_fog_color"], int, template_name)
        template_key_checking(self.current_template["carvers"], dict, template_name)
        template_key_checking(self.current_template["features"], list, template_name)
        template_key_checking(self.current_template["spawners"], dict, template_name)
        template_key_checking(self.current_template["spawn_costs"], dict, template_name)

    def create_biome(self, biome_folder = "bte/data/worldgen/biome/") -> str:
        """
        create the biome json file in the datapack

        Return the mcjson path to the biome created
        """
        self.biome_counter += 1
        print(self.biome_counter)

        cat_order_file = open("assets/feature_categories/order.json", "r")
        order_obj = json.load(cat_order_file)
        cat_order_file.close()

        biome_feature_list = FeatureList()

        for cat_file in order_obj["file_paths"]:
            biome_feature_list.fill_with_categorie_file(cat_file, self.current_template["downfall"], self.current_template["temperature"])
        features_list = biome_feature_list.construct_complete_feature_list()
        self.current_template["features"] = features_list
        biome_file = open(biome_folder+"biome_"+str(self.biome_counter)+".json", "x")
        print(biome_file.name)
        json.dump(self.current_template,biome_file)
        biome_file.close()

        return "bte:biome_"+str(self.biome_counter)
    
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
