import unittest, lib.utilities as utils
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
        self.assertTrue(utils.str_only_checking(obj.VEGETAL_DECORATION))

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
        self.assertTrue(utils.str_only_checking(obj.VEGETAL_DECORATION))

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

    def test_density_filler_priority(self):
        obj:FeatureList = FeatureList()
        cat_obj = {
            "cat_type": "density",
            "generation_step": "VEGETAL_DECORATION",
            "multiple_occurence_percentage": [60, 20, 10, 5],
            "allowed_temperature_range":[-1.0, 2.0],
            "allowed_downfall_range":[-1.0, 2.0],
            "features":[
                {
                    "odds_1000": 100,
                    "content":[
                        {"feature":"bte/tree_density/oak_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_oak_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_oak_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_oak_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_oak_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/sea_buckthorn_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_sea_buckthorn_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_sea_buckthorn_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_sea_buckthorn_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_sea_buckthorn_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000": 100,
                    "content":[
                        {"feature":"bte/tree_density/spruce_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_spruce_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_spruce_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_spruce_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_spruce_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/mangrove_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_mangrove_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_mangrove_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_mangrove_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_mangrove_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/jungle_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_jungle_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_jungle_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_jungle_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_jungle_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/grove_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_grove_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_grove_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_grove_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_grove_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/dark_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_dark_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_dark_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_dark_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_dark_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/cherry_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_cherry_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_cherry_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_cherry_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_cherry_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/birch_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_birch_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_birch_forest", "odds":10, "priority":1},
                        {"feature":"bte/tree_density/thick_birch_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_birch_forest", "odds":10, "priority":5}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/acacia_forest", "odds":50, "priority":3},
                        {"feature":"bte/tree_density/sparse_acacia_forest", "odds":15, "priority":2},
                        {"feature":"bte/tree_density/scarce_acacia_forest", "odds":10, "priority":1},
                        {"feature":"bte/tr0e_density/thick_acacia_forest", "odds":15, "priority":4},
                        {"feature":"bte/tree_density/opaque_acacia_forest", "odds":10, "priority":5}
                    ]
                }
                
            ]
        }

        obj.density_cat_filler(2,cat_obj)
        self.assertTrue(len(obj.VEGETAL_DECORATION) == 2)
        self.assertTrue(utils.str_only_checking(obj.VEGETAL_DECORATION))

    def test_density_filler_no_priority(self):
        obj:FeatureList = FeatureList()
        cat_obj = {
            "cat_type": "density",
            "generation_step": "VEGETAL_DECORATION",
            "multiple_occurence_percentage": [60, 20, 10, 5],
            "allowed_temperature_range":[-1.0, 2.0],
            "allowed_downfall_range":[-1.0, 2.0],
            "features":[
                {
                    "odds_1000": 100,
                    "content":[
                        {"feature":"bte/tree_density/oak_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_oak_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_oak_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_oak_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_oak_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/sea_buckthorn_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_sea_buckthorn_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_sea_buckthorn_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_sea_buckthorn_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_sea_buckthorn_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000": 100,
                    "content":[
                        {"feature":"bte/tree_density/spruce_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_spruce_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_spruce_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_spruce_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_spruce_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/mangrove_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_mangrove_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_mangrove_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_mangrove_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_mangrove_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/jungle_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_jungle_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_jungle_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_jungle_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_jungle_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/grove_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_grove_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_grove_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_grove_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_grove_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/dark_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_dark_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_dark_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_dark_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_dark_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/cherry_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_cherry_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_cherry_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_cherry_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_cherry_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/birch_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_birch_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_birch_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_birch_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_birch_forest", "odds":10}
                    ]
                },
                {
                    "odds_1000":100,
                    "content":[
                        {"feature":"bte/tree_density/acacia_forest", "odds":50},
                        {"feature":"bte/tree_density/sparse_acacia_forest", "odds":15},
                        {"feature":"bte/tree_density/scarce_acacia_forest", "odds":10},
                        {"feature":"bte/tree_density/thick_acacia_forest", "odds":15},
                        {"feature":"bte/tree_density/opaque_acacia_forest", "odds":10}
                    ]
                }
                
            ]
        }

        obj.density_cat_filler(4,cat_obj)
        self.assertTrue(len(obj.VEGETAL_DECORATION) == 4)
        self.assertTrue(utils.str_only_checking(obj.VEGETAL_DECORATION))


    def test_fill_with_valid_categorie(self):
        obj = FeatureList()
        try:
            obj.fill_with_categorie_file("tests/json_files/forest_categorie.json", 1.0, 1.0)
            obj.fill_with_categorie_file("tests/json_files/vegetation_categorie.json", 1.0, 1.0)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_fill_with_invalid_categorie(self):
        obj = FeatureList()
        with self.assertRaises(KeyError): obj.fill_with_categorie_file("tests/json_files/wrong_vegetation_categorie.json", 1.0, 1.0)

    def test_fill_with_incompatible_temperature(self):
        obj = FeatureList()
        obj.fill_with_categorie_file("tests/json_files/forest_categorie.json", 1.0, 100.0)
        self.assertEqual(obj.VEGETAL_DECORATION, FeatureList().VEGETAL_DECORATION)

    def test_fill_with_incompatible_downfall(self):
        obj = FeatureList()
        obj.fill_with_categorie_file("tests/json_files/forest_categorie.json", 100.0, 1.0)
        self.assertEqual(obj.VEGETAL_DECORATION, FeatureList().VEGETAL_DECORATION)

