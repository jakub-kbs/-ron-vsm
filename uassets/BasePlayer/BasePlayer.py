import copy, json, random, subprocess

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# Enter into Default__BasePlayer_C
for item in data["Exports"][20]["Data"]:

    # Run Speed                                 # VANILLA 320
    if item["Name"] == "RunSpeed":
        item["Value"] = 336 
        continue    
    
    # Walk Speed Multiplier                     # VANILLA 1
    if item["Name"] == "WalkSpeedMultiplier":
        item["Value"] = 3
        continue

    # Min. Walk Speed %                         # VANILLA 0.25
    if item["Name"] == "MinWalkSpeedPercent":
        item["Value"] = 0.3
        continue

    # Speed Modifier Aim                        # VANILLA 0.85
    if item["Name"] == "SpeedModifier_Aim":
        item["Value"] = 0.85
        continue

    # Speed Modifier Focus Aim                  # VANILLA 0.5
    if item["Name"] == "SpeedModifier_AimFocus":
        item["Value"] = 0.5
        continue

    # Lean Speed Multiplier                     # VANILLA 0.5
    if item["Name"] == "LeanSpeedMultiplier":
        item["Value"] = 0.75                                
        continue

    # Speed % Loss Per Leg Injury               # VANILLA 0.025
    if item["Name"] == "SpeedPercentLossPerLegInjury":
        item["Value"] = 0.125                               
        continue

    # Speed % Loss When Carrying                # VANILLA 0.0625
    if item["Name"] == "SpeedPercentLossWhenCarrying":
        item["Value"] = 0.2                                 
        continue

    # Suppression Shake Scale                   # VANILLA 0.3
    if item["Name"] == "SuppressionShakeScale":
        item["Value"] = 0.25                               
        continue

    # Freelook Settings -- YAW                  # VANILLA 65 DEG                         
    if item["Name"] == "FreelookSetting":

        for item_data in item["Value"]:

            if item_data["Name"] == "PitchMax":
                item_data["Value"] = 65
                continue

            if item_data["Name"] == "YawMin":
                item_data["Value"] = -100    
                continue

            if item_data["Name"] == "YawMax":
                item_data["Value"] = 100 
                continue

for item in data["Exports"][26]["Data"]:
    
    # Collision cylinder radius                 # VANILLA 38
    if item["Name"] == "CapsuleRadius":
        item["Value"]= 34
        continue

# SAVE INTO FILE
json.dump(data, open(f"BasePlayer.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "BasePlayer.json"])

