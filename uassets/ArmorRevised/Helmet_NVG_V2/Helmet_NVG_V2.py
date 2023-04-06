import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'


# For every item in the table.
for item in data["Exports"][5]["Data"][3]["Value"]:

    if item["Name"] == "GrainIntensity":
        item["Value"] = 0.4
        continue

    if item["Name"] == "BloomIntensity":
        item["Value"] = 1.25
        continue

    # if item["Name"] == "BloomThreshold":
    #     item["Value"] = 1
    #     continue

    if item["Name"] == "AutoExposureMinBrightness":
        item["Value"] = -4
        continue

    if item["Name"] == "AutoExposureMaxBrightness":
        item["Value"] = 4
        continue

    if item["Name"] == "AutoExposureSpeedUp":
        item["Value"] = 2
        continue

    if item["Name"] == "AutoExposureSpeedDown":
        item["Value"] = 2
        continue

    if item["Name"] == "IndirectLightingIntensity":
        item["Value"] = 0.5
        continue

    if item["Name"] == "DepthOfFieldFocalDistance":
        item["Value"] = 100
        continue

    if item["Name"] == "DepthOfFieldDepthBlurAmount":
        item["Value"] = 1000
        continue

    if item["Name"] == "DepthOfFieldDepthBlurRadius":
        item["Value"] = 10
        continue

#data["Exports"][5]["Data"][3]["Value"][66]["Value"] = 1

# SAVE INTO FILE
json.dump(data, open(f"Helmet_NVG_V2.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "Helmet_NVG_V2.json"])