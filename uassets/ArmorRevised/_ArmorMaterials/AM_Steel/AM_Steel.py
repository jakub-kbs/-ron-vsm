import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# For every item in the table.
for item in data["Exports"][0]["Data"]:

    if item["Name"] == "DamageReduction":
        item["Value"] = 1
        continue

    if item["Name"] == "MinDamageReduction":
        item["Value"] = 1
        continue

    if item["Name"] == "Durability":
        item["Value"] = 30
        continue

    if item["Name"] == "SpallingChance":
        item["Value"] = 0.6
        continue

    if item["Name"] == "MovementAccelerationModifier":
        item["Value"] = -0.13
        continue

# SAVE INTO FILE
json.dump(data, open(f"AM_Steel.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "AM_Steel.json"])