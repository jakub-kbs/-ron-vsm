import copy, json, random, subprocess

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# NAME MAP
dic_nm = [
    '/Game/Blueprints/Items/WeaponsRevised/Grenade_9Banger_V2',
    'Grenade_9Banger_V2_C',
    'Default__Grenade_9Banger_V2_C',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Grenade_9Banger_V2_1024x2048.Grenade_9Banger_V2_1024x2048',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Warrior_Grenade_9Banger_1024x2048.Warrior_Grenade_9Banger',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Warrior_Grenade_9Banger_1024.Warrior_Grenade_9Banger',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Grenade_9Banger_V2_1024.Grenade_9Banger_V2',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/WarriorIcon_Grenade_9Banger_2048.WarriorIcon_Grenade_9Banger',
    '/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Grenade_9Banger_V2_2048.Grenade_9Banger_V2']

# APPEND DIC_NM TO NAME MAP -- .append(dic) doesn't work for some reason :C
i = 0
while i < len(dic_nm):
    data["NameMap"].append(dic_nm[i])
    i+=1

# IMPORTS
dic_1 = {
      "$type": "UAssetAPI.Import, UAssetAPI",
      "ClassPackage": "/Script/CoreUObject",
      "ClassName": "Package",
      "ObjectName": "/Game/Blueprints/Items/WeaponsRevised/Grenade_9Banger_V2",
      "OuterIndex": 0
    }

dic_2 = {
      "$type": "UAssetAPI.Import, UAssetAPI",
      "ClassPackage": "/Script/Engine",
      "ClassName": "BlueprintGeneratedClass",
      "ObjectName": "Grenade_9Banger_V2_C",
      "OuterIndex": -1164
    }

dic_3 = {
      "$type": "UAssetAPI.Import, UAssetAPI",
      "ClassPackage": "/Game/Blueprints/Items/WeaponsRevised/Grenade_9Banger_V2",
      "ClassName": "Grenade_9Banger_V2_C",
      "ObjectName": "Default__Grenade_9Banger_V2_C",
      "OuterIndex": -1164
    }

# APPEND DIC_1/2/3 TO IMPORTS
data["Imports"].append(dic_1)
data["Imports"].append(dic_2)
data["Imports"].append(dic_3)

# EXPORTS

dic_4 = {"$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
              "StructType": "DeviceData",
              "SerializeNone": 1,
              "StructGUID": "00000000-0000-0000-0000-000000000000",
              "Name": "TacticalItems",
              "DuplicationIndex": 0,
              "Value": [
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.StrPropertyData, UAssetAPI",
                  "Name": "Name",
                  "DuplicationIndex": 0,
                  "Value": "9Banger"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI",
                  "ID": 0,
                  "Name": "Image",
                  "DuplicationIndex": 0,
                  "Value": "/Game/ReadyOrNot/UI/Icons/Weapons/Grenades/Grenade_9Banger_V2_1024.Grenade_9Banger_V2_1024"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI",
                  "ID": 0,
                  "Name": "CarouselImage1",
                  "DuplicationIndex": 0,
                  "Value": "/Game/ReadyOrNot/UI/Menu/T_UI_Carousel_Flashbang_01.T_UI_Carousel_Flashbang_01"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI",
                  "ID": 0,
                  "Name": "CarouselImage2",
                  "DuplicationIndex": 0,
                  "Value": "/Game/ReadyOrNot/UI/Menu/T_UI_Carousel_Flashbang_01.T_UI_Carousel_Flashbang_01"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI",
                  "ID": 0,
                  "Name": "CarouselImage3",
                  "DuplicationIndex": 0,
                  "Value": "/Game/ReadyOrNot/UI/Menu/T_UI_Carousel_Flashbang_01.T_UI_Carousel_Flashbang_01"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI",
                  "Flags": 0,
                  "HistoryType": "Base",
                  "Namespace": "",
                  "CultureInvariantString": "10m",
                  "Name": "EffectiveRange",
                  "DuplicationIndex": 0,
                  "Value": "5EA369154D37A4E4421898B38F09BFEA"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI",
                  "Flags": 0,
                  "HistoryType": "Base",
                  "Namespace": "",
                  "CultureInvariantString": "Stuns targets",
                  "Name": "Use",
                  "DuplicationIndex": 0,
                  "Value": "7CEB733042FE80DBFF052C99B15DF796"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI",
                  "Flags": 0,
                  "HistoryType": "Base",
                  "Namespace": "",
                  "CultureInvariantString": "Blinding and deafening",
                  "Name": "Effects",
                  "DuplicationIndex": 0,
                  "Value": "6D1CD0CB416106EAE455898287208C52"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI",
                  "Flags": 0,
                  "HistoryType": "Base",
                  "Namespace": "",
                  "CultureInvariantString": "Moderate",
                  "Name": "Risk",
                  "DuplicationIndex": 0,
                  "Value": "C9341E0942EA0032265740BD123F6F08"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI",
                  "Flags": 0,
                  "HistoryType": "Base",
                  "Namespace": "",
                  "CultureInvariantString": "Wear protective face masks.",
                  "Name": "ToMitigate",
                  "DuplicationIndex": 0,
                  "Value": "1578D9DA4988CF899E580C8EE2CC1617"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.EnumPropertyData, UAssetAPI",
                  "EnumType": "EItemClass",
                  "Name": "ItemClass",
                  "DuplicationIndex": 0,
                  "Value": "EItemClass::IC_Grenade"
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.IntPropertyData, UAssetAPI",
                  "Name": "MaxInInventory",
                  "DuplicationIndex": 0,
                  "Value": 4
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.IntPropertyData, UAssetAPI",
                  "Name": "ItemsPerSlot",
                  "DuplicationIndex": 0,
                  "Value": 1
                },
                {
                  "$type": "UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI",
                  "Name": "Blueprint",
                  "DuplicationIndex": 0,
                  "Value": -1165
                }
              ]
            }

for item in data["Exports"][0]["Data"]:

    # ENTER TACTICAL ITEMS ARRAY
    if item["Name"] == "TacticalItems":
        item["Value"].append(dic_4)
        item["Value"][4]["Value"][12]["Value"] = 3

# SAVE INTO FILE
json.dump(data, open(f"ItemData.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "ItemData.json"])