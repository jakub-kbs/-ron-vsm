import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# 108 Export table.
for item in data["Exports"][107]["Data"]:
    
    # ColorScaleOverLife
    if item["Name"] == "ColorScaleOverLife":

        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue

            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue
            
            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                        
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.25

                    val_Y = float(minValVec["Value"]["Y"])
                    minValVec["Value"]["Y"] = val_Y * 0.25

                    val_Z = float(minValVec["Value"]["Z"])
                    minValVec["Value"]["Z"] = val_Z * 0.25

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                        
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.45

                    val_Y = float(maxValVec["Value"]["Y"])
                    maxValVec["Value"]["Y"] = val_Y * 0.425

                    val_Z = float(maxValVec["Value"]["Z"])
                    maxValVec["Value"]["Z"] = val_Z * 0.45

            # Max Value Vector
            if item_data["Name"] == "Table":
                for table_data in item_data["Value"]:

                    if table_data["Name"] == "Values":

                        for tableVal in table_data["Value"]:
                            
                            tableVal_old = float(tableVal["Value"])
                            tableVal["Value"] = tableVal_old * 0.4


# SAVE INTO FILE
json.dump(data, open(f"P_Ninebang_Detonation.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "P_Ninebang_Detonation.json"])