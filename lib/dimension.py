import json
from string import Template

class CheckerBoard:
    biomes:list[str]
    size:int = 2

    def __init__(self, size:int, biomes_ids:list[str]) -> None:
        self.size = size
        self.biomes = biomes_ids

    def create_dim(self, path:str):
        unpopulated_json:str = """
{"type":"minecraft:overworld","generator":{"type":"minecraft:noise","settings":"minecraft:overworld","biome_source":{"type":"minecraft:checkerboard","biomes":$biomes}}}
"""
        json_template:Template = Template(unpopulated_json)
        populated_json = json_template.substitute(biomes = json.dumps(self.biomes))
        file = open(path, "x")
        file.write(populated_json)
