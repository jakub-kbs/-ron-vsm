import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# For every item in the table.
for item in data["Exports"][1]["Data"]:

    if item["Name"] == "TotalSlots":
        item["Value"] = 14
        continue

    if item["Name"] == "DefaultPrimaryAmmoSlots":
        item["Value"] = 5
        continue

    if item["Name"] == "DefaultSecondaryAmmoSlots":
        item["Value"] = 2
        continue

    if item["Name"] == "DefaultGrenadeSlots":
        item["Value"] = 4
        continue

    if item["Name"] == "DefaultTacticalDeviceSlots":
        item["Value"] = 3
        continue

# SAVE INTO FILE
json.dump(data, open(f"Armor_Light_V2.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "Armor_Light_V2.json"])