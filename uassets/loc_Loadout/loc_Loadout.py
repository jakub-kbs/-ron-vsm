import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# For every item in the table.
for item in data["Exports"][0]["Table"]["Value"]:
    
    if item[0] == "armor.Kevlar":
        item[1] = "NIJ IIIA/Kevlar"
        continue

    if item[0] == "armor.Ceramic":
        item[1] = "NIJ III/Ceramic"
        continue

    if item[0] == "armor.Steel":
        item[1] = "NIJ IV/Steel"
        continue

# SAVE INTO FILE
json.dump(data, open(f"loc_Loadout.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "loc_Loadout.json"])