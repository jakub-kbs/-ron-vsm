import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

dic_nm = ['Durability', 'ArmourLevel']

i_nm = 0
while i_nm < len(dic_nm):
    data["NameMap"].append(dic_nm[i_nm])
    i_nm+=1

dic_ex = [
    {
        "$type": "UAssetAPI.PropertyTypes.Objects.FloatPropertyData, UAssetAPI",
        "Value": 10,
        "Name": "Durability",
        "DuplicationIndex": 0
    },
    {
        "$type": "UAssetAPI.PropertyTypes.Objects.FloatPropertyData, UAssetAPI",
        "Value": 3,
        "Name": "ArmourLevel",
        "DuplicationIndex": 0
    }
]

# For every item in the table.
for item in data["Exports"][2]["Data"]:

    if item["Name"] == "DamageReduction":
        item["Value"] = 1
        continue

i_ex = 0
while i_ex < len(dic_ex):
    data["Exports"][2]["Data"].append(dic_ex[i_ex])
    i_ex+=1

# SAVE INTO FILE
json.dump(data, open(f"Helmet_None.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "Helmet_None.json"])