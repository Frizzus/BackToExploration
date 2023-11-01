import os, shutil, json, lib.bte_errors, logging
from lib.EnvTemplate import EnvTemplate

try:
    logs = os.remove("logs.txt")
except:
    pass

logging.basicConfig(filename="logs.txt", level=logging.INFO)

# suppression du datapack précédent

try:
    shutil.rmtree("bte")
except:
    logging.info("bte datapack not found, creating one")

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

mc_meta.close()

logging.info("basic template loaded")
print("basic template loaded")

shutil.copytree("assets/configured_feature", "bte/data/worldgen/configured_feature", dirs_exist_ok=True)
logging.info("configured features loaded")
print("configured features loaded")

shutil.copytree("assets/placed_feature", "bte/data/worldgen/placed_feature", dirs_exist_ok=True)
logging.info("placed features loaded")
print("placed features loaded")

shutil.copy("assets/overworld.json", "bte/minecraft/dimension/overworld.json")

# biome creation time
env_templates = os.listdir("assets/env_template")
biome_mcpaths:list[str] = []

for template in env_templates:
    if os.path.isdir("assets/env_template/"+template):
        logging.error("\nFound an unexpected directory : assets/env_template/" + template)
        raise lib.bte_errors.UnexpectedDirectoryError("\nFound an unexpected directory : assets/env_template/" + template)

tmp = EnvTemplate()

for template in env_templates:
    logging.info("creating biomes for : assets/env_template/" + template)
    tmp.set_current_template("assets/env_template/"+template)
    biome_mcpaths.append(tmp.create_biome())
    


logging.info("datapack created")
print("datapack created")