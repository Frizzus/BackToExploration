import json, random

class FeatureList:
    def __init__(self) -> None:
        self.RAW_GENERATION = []
        self.LAKES = []
        self.LOCAL_MODIFICATIONS = []
        self.UNDERGROUND_STRUCTURES = []
        self.SURFACE_STRUCTURES = []
        self.STRONGHOLDS = []
        self.UNDERGROUND_ORES = []
        self.UNDERGROUND_DECORATION = []
        self.FLUID_SPRINGS = []
        self.VEGETAL_DECORATION = []
        self.TOP_LAYER_MODIFICATION = []
    
    def fill_with_categorie_file(self, cat_file_path:str, allowed_downfall:float, allowed_temperature:float):
        cat_object = json.load(open(cat_file_path))

        if (cat_object["allowed_temperature_range"][1] >= allowed_temperature and allowed_temperature >= cat_object["allowed_temperature_range"][0]) and (cat_object["allowed_downfall_range"][1] >= allowed_downfall and allowed_downfall >= cat_object["allowed_downfall_range"][0]):
            nb_cat_iteration:int = 0
            random_nb = random.randint(1, 100)
            for percentage in cat_object["multiple_occurence_percentage"]:
                if random_nb <= percentage:
                    nb_cat_iteration += 1
            
            
                

    def construct_comlete_feature_list(self):
        pass

# gotta take care of the feature overall order and the priority arg in categorie files