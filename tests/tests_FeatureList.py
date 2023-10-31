import unittest
from lib.FeatureList import FeatureList

class TestFeatureList(unittest.TestCase):
    def test_basic_filler_no_priority(self):
        obj:FeatureList = FeatureList()
        cat_obj = {
            "cat_type": "basic",
            "generation_step": "VEGETAL_DECORATION",
            "multiple_occurence_percentage": [95, 30, 10],
            "allowed_temperature_range":[-1.0, 2.0],
            "allowed_downfall_range":[-1.0, 2.0],
            "features": [
                {"feature":"minecraft:patch_grass_forest", "odds_1000":100},
                {"feature":"minecraft:patch_grass_jungle", "odds_1000":100},
                {"feature":"minecraft:patch_grass_plain", "odds_1000":100},
                {"feature":"minecraft:patch_grass_normal", "odds_1000":100},
                {"feature":"minecraft:patch_tall_grass", "odds_1000":100},
                {"feature":"minecraft:patch_grass_taiga", "odds_1000":100},
                {"feature":"minecraft:patch_large_fern", "odds_1000":100},
                {"feature":"minecraft:patch_berry_common", "odds_1000":100},
                {"feature":"minecraft:patch_berry_rare", "odds_1000":100},
                {"feature":"minecraft:patch_melon", "odds_1000":50},
                {"feature":"minecraft:patch_pumpkin", "odds_1000":50}
            ]
        }

        obj.basic_cat_filler(2,cat_obj)
        self.assertTrue(len(obj.VEGETAL_DECORATION) == 2)

    def test_basic_filler_priority(self):
        obj:FeatureList = FeatureList()
        cat_obj = {
            "cat_type": "basic",
            "generation_step": "VEGETAL_DECORATION",
            "multiple_occurence_percentage": [95, 30, 10],
            "allowed_temperature_range":[-1.0, 2.0],
            "allowed_downfall_range":[-1.0, 2.0],
            "features": [
                {"feature":"minecraft:patch_grass_forest", "odds_1000":100, "priority":1},
                {"feature":"minecraft:patch_grass_jungle", "odds_1000":100, "priority":3},
                {"feature":"minecraft:patch_grass_plain", "odds_1000":100, "priority":5},
                {"feature":"minecraft:patch_grass_normal", "odds_1000":100, "priority":6},
                {"feature":"minecraft:patch_tall_grass", "odds_1000":100, "priority":2},
                {"feature":"minecraft:patch_grass_taiga", "odds_1000":100, "priority":10},
                {"feature":"minecraft:patch_large_fern", "odds_1000":100, "priority":8},
                {"feature":"minecraft:patch_berry_common", "odds_1000":100, "priority":4},
                {"feature":"minecraft:patch_berry_rare", "odds_1000":100, "priority":9},
                {"feature":"minecraft:patch_melon", "odds_1000":50, "priority":7},
                {"feature":"minecraft:patch_pumpkin", "odds_1000":50, "priority":11}
            ]
        }

        obj.basic_cat_filler(4,cat_obj)
        self.assertTrue(len(obj.VEGETAL_DECORATION) == 4)

    def test_construct_complete_feature_list(self):
        feature_obj = FeatureList()
        feature_obj.RAW_GENERATION.extend(["raw_gen_feature_1","raw_gen_feature_2", "raw_gen_feature_3"])
        feature_obj.VEGETAL_DECORATION.extend(["tree_1", "tree_2", "tree_3", "tree_4"])

        model_list = [
            ["raw_gen_feature_1","raw_gen_feature_2", "raw_gen_feature_3"],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            ["tree_1", "tree_2", "tree_3", "tree_4"],
            []
        ]

        self.assertListEqual(model_list, feature_obj.construct_complete_feature_list())