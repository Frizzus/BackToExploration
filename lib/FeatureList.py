
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
        pass

    def construct_comlete_feature_list(self):
        pass

# gotta take care of the feature overall order and the priority arg in categorie files