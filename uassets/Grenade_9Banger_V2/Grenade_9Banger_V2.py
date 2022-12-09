import copy, json, random, subprocess

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# Enter into Default__Grenade_9Banger_V2_C
for item in data["Exports"][1]["Data"]:
    
    # Detonation Time                                   # VANILLA 1 SEC
    if item["Name"] == "DetonationTime":
        item["Value"] = 1.5 # SEC
        continue

    # Redetonation Time                                 # VANILLA 0.225 SEC
    if item["Name"] == "ReDetonationTime":
        item["Value"] = 0.25 # SEC
        continue

    # Detonation Light                                  # VANILLA 8 - TEST
    # if item["Name"] == "DetonationLight":
    #     item["Value"] = 4
    #     continue

    # # Detonation Loudness                               # VANILLA 2 - UNKNOWN
    # if item["Name"] == "DetonationLoudness":
    #     item["Value"] = 1.5
    #     continue

    # # Detonation Decal Size                             # VANILLA 25 - UNKNOWN
    # if item["Name"] == "DetonationDecalSize":

    #     for item_data in item["Value"]:
    #         item_data["Value"]["X"] = 10
    #         item_data["Value"]["Y"] = 10
    #         item_data["Value"]["Z"] = 10 
    #         continue


# SAVE INTO FILE
json.dump(data, open(f"Grenade_9Banger_V2.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "Grenade_9Banger_V2.json"])