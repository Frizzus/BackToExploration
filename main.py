import os, sys, shutil, json
from lib.dimension import CheckerBoard 

# suppression du datapack précédent

try:
    shutil.rmtree("bte")
except:
    print("bte datapack not found, creating one")

# création du template du datapack

datapack_templating:list[str] = ["bte", "bte/data", "bte/minecraft", "bte/minecraft/dimension", "bte/data/worldgen", "bte/data/worldgen/biome", "bte/data/worldgen/configured_feature", "bte/data/worldgen/placed_feature"]

for directory in datapack_templating:
    os.mkdir(directory)

mc_meta = open("bte/pack.mcmeta", "x")

mc_meta.write(
"""{
    "pack":{
        "pack_format":15,
        "description":"Discover all the possibilities !"
    }
}""")

# soon to be replaced by a simple overworld.json in the assets
debug_dim:CheckerBoard = CheckerBoard("3", ["minecraft:forest", "minecraft:meadow"])
debug_dim.create_dim("bte/minecraft/dimension/overworld.json")

print("basic template loaded")

shutil.copytree("assets/configured_feature", "bte/data/worldgen/configured_feature", dirs_exist_ok=True)
print("configured features loaded")

shutil.copytree("assets/placed_feature", "bte/data/worldgen/placed_feature", dirs_exist_ok=True)
print("placed features loaded")

print("datapack created")