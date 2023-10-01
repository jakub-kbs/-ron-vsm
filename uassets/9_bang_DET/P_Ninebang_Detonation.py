import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# 107 Export table.
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

            # Table - most likely does nothing
    #           if item_data["Name"] == "Table":
    #               for table_data in item_data["Value"]:

    #                   if table_data["Name"] == "Values":

    #                        for tableVal in table_data["Value"]:
                            
    #                            tableVal_old = float(tableVal["Value"])
    #                            tableVal["Value"] = tableVal_old * 0.4

    # BrightnessOverLife
    if item["Name"] == "BrightnessOverLife":
        
        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.55
                continue

            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.55
                continue

    # LightExponent
    if item["Name"] == "RadiusScale":

        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.4
                continue
                    
            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.4
                continue

    # RadiusScale
    if item["Name"] == "RadiusScale":

        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.3
                continue
                    
            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.3
                continue


# 108 Export table.
for item in data["Exports"][108]["Data"]:

    # RadiusScale
    if item["Name"] == "RadiusScale":

        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.475
                continue
                    
            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.525
                continue

     # LightExponent
    if item["Name"] == "RadiusScale":

        for item_data in item["Value"]:

            # Min Value
            if item_data["Name"] == "MinValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.4
                continue
                    
            # Max Value
            if item_data["Name"] == "MaxValue":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.4
                continue

# 144 Export table.
for item in data["Exports"][144]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                            
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.35

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                            
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.4

# 145 Export table.
for item in data["Exports"][145]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                            
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.89

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                            
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.91

# 149 Export table.
for item in data["Exports"][149]["Data"]:
            
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                        
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.89

                    val_Y = float(minValVec["Value"]["Y"])
                    minValVec["Value"]["Y"] = val_Y * 0.65

                    val_Z = float(minValVec["Value"]["Z"])
                    minValVec["Value"]["Z"] = val_Z * 0.62

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                        
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.90

                    val_Y = float(maxValVec["Value"]["Y"])
                    maxValVec["Value"]["Y"] = val_Y * 0.775

                    val_Z = float(maxValVec["Value"]["Z"])
                    maxValVec["Value"]["Z"] = val_Z * 0.9

# 150 Export table.
for item in data["Exports"][150]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                            
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.6

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                            
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.45

# 151 Export table.
for item in data["Exports"][151]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value 
            if item_data["Name"] == "MinValue":
                val_X = float(item_data["Value"])
                item_data["Value"] = val_X * 0.45

            # Max Value Vector
            if item_data["Name"] == "MaxValue":
                val_X = float(item_data["Value"])
                item_data["Value"] = val_X * 0.4

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                        
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.275

                    val_Y = float(minValVec["Value"]["Y"])
                    minValVec["Value"]["Y"] = val_Y * 0.45

                    val_Z = float(minValVec["Value"]["Z"])
                    minValVec["Value"]["Z"] = val_Z * 0.8

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                        
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.5

                    val_Y = float(maxValVec["Value"]["Y"])
                    maxValVec["Value"]["Y"] = val_Y * 0.475

                    val_Z = float(maxValVec["Value"]["Z"])
                    maxValVec["Value"]["Z"] = val_Z * 0.55

# 152 Export table.
for item in data["Exports"][152]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                            
                for minValVec in item_data["Value"]:
                    val_X = float(minValVec["Value"]["X"])
                    minValVec["Value"]["X"] = val_X * 0.46

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                            
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.5

# 155 Export table.
for item in data["Exports"][155]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Max Value Vector
            if item_data["Name"] == "MaxValueVec":
                            
                for maxValVec in item_data["Value"]:
                    val_X = float(maxValVec["Value"]["X"])
                    maxValVec["Value"]["X"] = val_X * 0.35

                    val_Y = float(maxValVec["Value"]["Y"])
                    maxValVec["Value"]["Y"] = val_Y * 0.35

                    val_Z = float(maxValVec["Value"]["Z"])
                    maxValVec["Value"]["Z"] = val_Z * 0.35

# 156 Export table.
for item in data["Exports"][156]["Data"]:
        
    # StartSize
    if item["Name"] == "StartSize":

        for item_data in item["Value"]:

            # Min Value Vector
            if item_data["Name"] == "MinValueVec":
                for minValVec in item_data["Value"]:

                    val_Y = float(minValVec["Value"]["Y"])
                    minValVec["Value"]["Y"] = val_Y * 0.45

                    val_Z = float(minValVec["Value"]["Z"])
                    minValVec["Value"]["Z"] = val_Z * 0.25

# SAVE INTO FILE
json.dump(data, open(f"P_Ninebang_Detonation.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "P_Ninebang_Detonation.json"])