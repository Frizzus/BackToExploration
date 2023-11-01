import json, random, lib.utilities as utils

class FeatureList:
    def __init__(self) -> None:
        self.RAW_GENERATION:list[str] = []
        self.LAKES:list[str] = []
        self.LOCAL_MODIFICATIONS:list[str] = []
        self.UNDERGROUND_STRUCTURES:list[str] = []
        self.SURFACE_STRUCTURES:list[str] = []
        self.STRONGHOLDS:list[str] = []
        self.UNDERGROUND_ORES:list[str] = []
        self.UNDERGROUND_DECORATION:list[str] = []
        self.FLUID_SPRINGS:list[str] = []
        self.VEGETAL_DECORATION:list[str] = []
        self.TOP_LAYER_MODIFICATION:list[str] = []

    def density_cat_filler(self, nb_iteration:int, cat_object:dict):
        density_content:list[list] = []
        odds_1000:list[int] = []
        for feature in cat_object["features"]:
            density_content.append(feature["content"])
            odds_1000.append(feature["odds_1000"])

        choosen_contents:list[dict] = []
        for gen_turn in range(nb_iteration):
            choosen_contents.append(utils.weighted_choice(density_content, odds_1000, 1000))

        contents_indexes:list[list[int]] = []
        contents_odds:list[list[int]] = []
        for content in choosen_contents:
            current_indexes = []
            current_odds = []
            for index in range(len(content)):
                current_indexes.append(index)
                current_odds.append(content[index]["odds"])
            contents_indexes.append(current_indexes)
            contents_odds.append(current_odds)

        choosen_features_str_indexes:list = []
        for i in range(len(contents_indexes)):
            choosen_features_str_indexes.append(utils.weighted_choice(contents_indexes[i], contents_odds[i], 100))

        tuples_res:list[tuple] = []
        for index in range(len(choosen_features_str_indexes)):
            if not ("priority" in choosen_contents[index][choosen_features_str_indexes[index]]):
                choosen_contents[index][choosen_features_str_indexes[index]]["priority"] = 10_000
            tuples_res.append((choosen_contents[index][choosen_features_str_indexes[index]]["feature"], choosen_contents[index][choosen_features_str_indexes[index]]["priority"]))

        tuples_res = utils.sort_with_priority(tuples_res)

        res:list[str] = []
        for tupl in tuples_res:
            res.append(tupl[0])

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
        

    def basic_cat_filler(self, nb_iteration:int, cat_object:dict):
        """
        take a categorie json object and a number of iteration to randomly choose a feature in the categorie
        it will fill the FeatureList object with the randomly chosen feature
        """
        features_indexes:list[int] = []
        odds:list[int] = []

        for index in range(len(cat_object["features"])):
            features_indexes.append(index)
            odds.append(cat_object["features"][index]["odds_1000"])
        
        choosen:list = []
        for gen_turn in range(nb_iteration):
            choosen.append(utils.weighted_choice(features_indexes, odds, 1000))

        tuples_res:list[tuple] = []
        for index in choosen:
            if not ("priority" in cat_object["features"][index]):
                cat_object["features"][index]["priority"] = 10_000
            tuples_res.append((cat_object["features"][index]["feature"], cat_object["features"][index]["priority"]))

        tuples_res = utils.sort_with_priority(tuples_res)

        res:list[str] = []
        for tupl in tuples_res:
            res.append(tupl[0])

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
            
            
                

    def construct_complete_feature_list(self) -> list[list[str]]:
        """
        Return the features array to use in a json biome
        """
        res = []
        res.append(self.RAW_GENERATION)
        res.append(self.LAKES)
        res.append(self.LOCAL_MODIFICATIONS)
        res.append(self.UNDERGROUND_STRUCTURES)
        res.append(self.SURFACE_STRUCTURES)
        res.append(self.STRONGHOLDS)
        res.append(self.UNDERGROUND_ORES)
        res.append(self.UNDERGROUND_DECORATION)
        res.append(self.FLUID_SPRINGS)
        res.append(self.VEGETAL_DECORATION)
        res.append(self.TOP_LAYER_MODIFICATION)
        return res
