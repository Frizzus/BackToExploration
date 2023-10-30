import json, random, lib.utilities as utils

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


    def basic_cat_filler(self, nb_iteration:int, cat_object:dict):
        features_indexes:list[int] = []
        odds:list[int] = []

        for index in range(len(cat_object["features"])):
            features_indexes.append(index)
            odds.append(cat_object["features"][index]["odds_1000"])
        
        choosen:list = []
        for gen_turn in range(nb_iteration):
            choosen.append(utils.weighted_choice(features_indexes, odds, 1000))

        res:list[tuple] = []
        for index in choosen:
            if not ("priority" in cat_object["features"][index]):
                cat_object["features"][index]["priority"] = 10_000
            res.append((cat_object["features"][index]["feature"], cat_object["features"][index]["priority"]))

        res = utils.sort_with_priority(res)

        match cat_object["generation_step"]:
                case "RAW_GENERATION":
                    self.RAW_GENERATION.extend(res)
                case "FLUID_SPRINGS":
                    self.FLUID_SPRINGS.extend(res)
                case "LOCAL_MODIFICATIONS":
                    self.LOCAL_MODIFICATIONS.extend(res)
                case "LAKES":
                    self.LAKES.extend(res)
                case "STRONGHOLDS":
                    self.STRONGHOLDS.extend(res)
                case "SURFACE_STRUCTURES":
                    self.SURFACE_STRUCTURES.extend(res)
                case "TOP_LAYER_MODIFICATION":
                    self.TOP_LAYER_MODIFICATION.extend(res)
                case "UNDERGROUND_DECORATION":
                    self.UNDERGROUND_DECORATION.extend(res)
                case "UNDERGROUND_ORES":
                    self.UNDERGROUND_ORES.extend(res)
                case "VEGETAL_DECORATION":
                    self.VEGETAL_DECORATION.extend(res)
    

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