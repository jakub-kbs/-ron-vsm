import copy, json, random, subprocess, math

file = open('vanilla.json')
data = json.load(file)

path_to_uasset = 'D:\\_Work\\Unreal Tools\\UAassetGUI\\UAssetGUI.exe'

# For every item in the table.
for item in data["Exports"][0]["Table"]["Data"]:

    #----------- GLOBAL CHANGES
        
        for item_data in item["Value"]:

            # ADS ZOOM
            if item_data["Name"] == "ADSZoom":
                item_data["Value"] = 0.9
                continue

            # ADS ZOOM IN
            if item_data["Name"] == "ADSZoomInSpeed":
                item_data["Value"] = 10
                continue
                
            # ADS ZOOM OUT
            if item_data["Name"] == "ADSZoomOutSpeed":
                item_data["Value"] = 10
                continue

            # INERTIA
            if item_data["Name"] == "InertiaDragAimRotation":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue

            if item_data["Name"] == "InertiaDragAimLocation":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue

            if item_data["Name"] == "InertiaDragStrafeRotation":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue

            if item_data["Name"] == "InertiaDragStrafeLocation":
                val = float(item_data["Value"])
                item_data["Value"] = val / 2
                continue
            
            # RECOIL CONTROL STRENGTH
            if item_data["Name"] == "RecoilDampStrength":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.5
                continue

            # RECOIL FIRE STRENGTH FIRST
            if item_data["Name"] == "RecoilFireStrength":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.85
                continue

            # RECOIL FIRE STRENGTH
            if item_data["Name"] == "RecoilFireStrengthFirst":
                val = float(item_data["Value"])
                item_data["Value"] = val * 0.9
                continue

        array_smg = ["MP5A2", "MP5A3", "MP510", "MPX", "MP9", "SPC9", "UMP45", "MP7", "P90", "TAC700"]
        array_ar = ["MK18", "SBR", "SR16", "HK416", "BCM_MK1", "SCARL", "G36C", "AR18", "SLR47", "FAL", "VKS"]
        array_sg = ["Beanbag", "870mcs", "P1301_Entryman", "P1301", "BenelliM4", "S590_Breach"]
        
        array_hg = ["G19", "PFC9", "M2011", "Python", "M92A3", "Taser", "FiveSeven", "USP", "P229"]

        array_tac = ["M32A1", "M320_Gas", "M320_Bang", "M320_Stinger", "Mirrorgun"]

        # MESHSPACE DEFAULT - SMGs
        index_smg = 0
        while index_smg < len(array_smg):
            if item["Name"] == array_smg[index_smg]:

                for item_data in item["Value"]:

                    if item_data["Name"] == "MeshspaceTransform_Default":
                        
                        for def_meshspace in item_data["Value"]:

                            # ENTER TRANSLATION ARRAY
                            if def_meshspace["Name"] == "Translation":
                                    
                                # ENTER TRANSLATION OBJECT
                                for translation_array in def_meshspace["Value"]:
                                    translation_array["Value"]["X"] = 7
                                    translation_array["Value"]["Y"] = -1
                                    translation_array["Value"]["Z"] = -1
                                    continue
                                
                            # ENTER ROTATION ARRAY
                            if def_meshspace["Name"] == "Rotation":
                                    
                                # ENTER ROTATION OBJECT
                                for rotation_array in def_meshspace["Value"]:
                                    rotation_array["Value"]["Y"] = 0.05
                                    continue

                    if item_data["Name"] == "MeshspaceTransform_Back":
                    
                        for back_meshspace in item_data["Value"]:
                            
                            # ENTER TRANSLATION ARRAY
                            if back_meshspace["Name"] == "Translation":
                                
                                # ENTER TRANSLATION OBJECT
                                for translation_array in back_meshspace["Value"]:
                                    translation_array["Value"]["X"] = -60
                                    translation_array["Value"]["Y"] = -0
                                    translation_array["Value"]["Z"] = -20
                                    continue
            index_smg+=1

        # MESHSPACE DEFAULT - ARs
        index_ar = 0
        while index_ar < len(array_ar):
            if item["Name"] == array_ar[index_ar]:

                for item_data in item["Value"]:

                    if item_data["Name"] == "MeshspaceTransform_Default":
                        
                        for def_meshspace in item_data["Value"]:

                            # ENTER TRANSLATION ARRAY
                            if def_meshspace["Name"] == "Translation":
                                    
                                # ENTER TRANSLATION OBJECT
                                for translation_array in def_meshspace["Value"]:
                                    translation_array["Value"]["X"] = 7
                                    translation_array["Value"]["Y"] = -1
                                    translation_array["Value"]["Z"] = -1.25
                                    continue
                                
                            # ENTER ROTATION ARRAY
                            if def_meshspace["Name"] == "Rotation":
                                    
                                # ENTER ROTATION OBJECT
                                for rotation_array in def_meshspace["Value"]:
                                    rotation_array["Value"]["Y"] = 0.05
                                    continue

                    if item_data["Name"] == "MeshspaceTransform_Back":
                    
                        for back_meshspace in item_data["Value"]:
                            
                            # ENTER TRANSLATION ARRAY
                            if back_meshspace["Name"] == "Translation":
                                
                                # ENTER TRANSLATION OBJECT
                                for translation_array in back_meshspace["Value"]:
                                    translation_array["Value"]["X"] = -60
                                    translation_array["Value"]["Y"] = -0
                                    translation_array["Value"]["Z"] = -20
                                    continue
            index_ar+=1

        # MESHSPACE DEFAULT - SHOTGUNSs
        index_sg = 0
        while index_sg < len(array_sg):
            if item["Name"] == array_sg[index_sg]:

                for item_data in item["Value"]:

                    if item_data["Name"] == "MeshspaceTransform_Default":
                        
                        for def_meshspace in item_data["Value"]:

                            # ENTER TRANSLATION ARRAY
                            if def_meshspace["Name"] == "Translation":
                                    
                                # ENTER TRANSLATION OBJECT
                                for translation_array in def_meshspace["Value"]:
                                    translation_array["Value"]["X"] = 6
                                    translation_array["Value"]["Y"] = -1
                                    translation_array["Value"]["Z"] = -1.25
                                    continue
                                
                            # ENTER ROTATION ARRAY
                            if def_meshspace["Name"] == "Rotation":
                                    
                                # ENTER ROTATION OBJECT
                                for rotation_array in def_meshspace["Value"]:
                                    rotation_array["Value"]["Y"] = 0.05
                                    continue

                    if item_data["Name"] == "MeshspaceTransform_Back":
                    
                        for back_meshspace in item_data["Value"]:
                            
                            # ENTER TRANSLATION ARRAY
                            if back_meshspace["Name"] == "Translation":
                                
                                # ENTER TRANSLATION OBJECT
                                for translation_array in back_meshspace["Value"]:
                                    translation_array["Value"]["X"] = -60
                                    translation_array["Value"]["Y"] = -0
                                    translation_array["Value"]["Z"] = -20
                                    continue
            index_sg+=1

        # MESHSPACE DEFAULT - TACTICALs
        index_tac = 0
        while index_tac < len(array_tac):
            if item["Name"] == array_tac[index_tac]:

                for item_data in item["Value"]:

                    if item_data["Name"] == "MeshspaceTransform_Default":
                        
                        for def_meshspace in item_data["Value"]:

                            # ENTER TRANSLATION ARRAY
                            if def_meshspace["Name"] == "Translation":
                                    
                                # ENTER TRANSLATION OBJECT
                                for translation_array in def_meshspace["Value"]:
                                    translation_array["Value"]["X"] = 7
                                    translation_array["Value"]["Y"] = -1
                                    translation_array["Value"]["Z"] = -1.25
                                    continue
                                
                            # ENTER ROTATION ARRAY
                            if def_meshspace["Name"] == "Rotation":
                                    
                                # ENTER ROTATION OBJECT
                                for rotation_array in def_meshspace["Value"]:
                                    rotation_array["Value"]["Y"] = 0.05
                                    continue

                    if item_data["Name"] == "MeshspaceTransform_Back":
                    
                        for back_meshspace in item_data["Value"]:
                            
                            # ENTER TRANSLATION ARRAY
                            if back_meshspace["Name"] == "Translation":
                                
                                # ENTER TRANSLATION OBJECT
                                for translation_array in back_meshspace["Value"]:
                                    translation_array["Value"]["X"] = -60
                                    translation_array["Value"]["Y"] = -0
                                    translation_array["Value"]["Z"] = -20
                                    continue  
            index_tac+=1                             

        # MESHSPACE DEFAULT - HANDGUNS
        index_hg = 0
        while index_hg < len(array_hg):
            if item["Name"] == array_hg[index_hg]:

                for item_data in item["Value"]:

                    if item_data["Name"] == "MeshspaceTransform_Default":
                        
                        for def_meshspace in item_data["Value"]:
                                
                            # ENTER ROTATION ARRAY
                            if def_meshspace["Name"] == "Rotation":
                                    
                                # ENTER ROTATION OBJECT
                                for rotation_array in def_meshspace["Value"]:
                                    rotation_array["Value"]["Y"] = 0.1
                                    continue

                    if item_data["Name"] == "MeshspaceTransform_Back":
                    
                        for back_meshspace in item_data["Value"]:
                            
                            # ENTER TRANSLATION ARRAY
                            if back_meshspace["Name"] == "Translation":
                                
                                # ENTER TRANSLATION OBJECT
                                for translation_array in back_meshspace["Value"]:
                                    translation_array["Value"]["X"] = -25
                                    translation_array["Value"]["Y"] = 0
                                    continue 
            index_hg+=1

    #----------- PRIMARY WEAPONS

        # BEANBAG
        if item["Name"] == "Beanbag":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Wilson Combat Less Lethal CQB"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "This 'Less Lethal' version of Wilson Combat CQB shotgun is designed to be easily identified as a less lethal option for use in a crowd control or riot situation. Special Hogue blaze orange stocks are used to quickly designate the 'Less lethal' loaded firearm in your armory."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.34
                    continue

                # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(4.75, 5.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(4.75, 5.25)
                #                     continue

        # MK18
        if item["Name"] == "MK18":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Mk 18 Mod 0"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "This shorter-barreled M4A1 designated as Mk 18 Mod 0 is a weapon significantly more compact, thus making it easier to use in, and around, vehicles and in tight, confined spaces."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.72
                    continue

                # PUSHBACK RANGE
                if item_data["Name"] == "PushbackRange":
                    item_data["Value"] = 160
                    continue

                # LOW-READY RANGE
                if item_data["Name"] == "LowReadyRange":
                    item_data["Value"] = 73
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.1
                #     continue

                # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 90521
                #     continue

                # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 32.5
                #     continue

                # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.4000000059604645:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.3, 1.4)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.4000000059604645:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.3, 1.4)
                #                     continue
                
        # Benelli M4
        if item["Name"] == "BenelliM4":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Benelli M4"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "This gas powered combat shotgun is widely considered the best of its breed. Reliable and fast firing, its only major drawback is how quickly you'll empty it if you're not careful."
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 47.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.25
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 8.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue

        # 870 MCS
        if item["Name"] == "870mcs":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Wilson Combat CQB"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "This take on the Remington Model 870 shotgun by Wilson Combat has been developed at the request of tactical shotgunners looking for the ideal tactical shotgun package with the added adjustability and modularity inherent to a collapsible AR-compatible buttstock."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.85
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 47.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.25
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 8.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue

        # P1301
        if item["Name"] == "P1301":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Beretta 1301 Tactical"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "A sturdy tactical shotgun hailing from Italy. Its unique bolt design reduces muzzle climb compared to its counterparts."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.9
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 47.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.25
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 8.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue

        # P1301 Entryman
        if item["Name"] == "P1301_Entryman":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Beretta 1301 Tactical \"Entryman\""
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "A sturdy tactical shotgun hailing from Italy. Its unique bolt design reduces muzzle climb compared to its counterparts."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.9
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 47.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.25
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 8.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(5.75, 6.25)
                #                     continue

        # FAL
        if item["Name"] == "FAL":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "DSA SA-58 OSW"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 4.0799999237060547
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.7
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE 
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 65
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.2
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.2
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.75:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.75, 2.85)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.75:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.75, 2.85)
                #                     continue
                
        # G36C
        if item["Name"] == "G36C":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K G36C"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3
                    continue

                # LOW-READY RANGE
                if item_data["Name"] == "LowReadyRange":
                    item_data["Value"] = 70
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.48
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.15
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 78774
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 30
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                
        # UMP45
        if item["Name"] == "UMP45":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K UMP-45"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.65
                    continue

                # PUSHBACK RANGE
                if item_data["Name"] == "PushbackRange":
                    item_data["Value"] = 120
                    continue

                # LOW-READY RANGE
                if item_data["Name"] == "LowReadyRange":
                    item_data["Value"] = 60
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.55
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.15
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 40
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 12
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.8, 0.95)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.8, 0.95)
                #                     continue

        # MP5A2
        if item["Name"] == "MP5A2":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K MP5A2"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.7300000190734863
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.32
                    continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 20
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue
                
        # MP5A3
        if item["Name"] == "MP5A3":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K MP5A3"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.1
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.32
                    continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 20
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.85, 0.95)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.85, 0.95)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.85, 0.95)
                #                     continue

        # MP5/10
        if item["Name"] == "MP510":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K MP5/10"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.2
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.55
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.15
                    continue

                # DAMAGE
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 37.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.07
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 17
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1, 1.2)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1, 1.2)
                #                     continue

        # MPX
        if item["Name"] == "MPX":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "SIG-Sauer MPX"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.7000000476837158
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.31999999284744263
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.10000000149011612
                    continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 40000
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 20
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue

        # SPC9
        if item["Name"] == "SPC9":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "B&T SPC9 SBR"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.650
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.31999999284744263
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.10000000149011612
                    continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 40000
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 20
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.9)
                #                     continue

        # MP7
        if item["Name"] == "MP7":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K MP7-A2"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 1.9
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.55
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE 
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 24
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 30000
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 22
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.95)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.75, 0.95)
                #                     continue

        # MP9
        if item["Name"] == "MP9":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "B&T MP9-N"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 1.4
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.31999999284744263
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.10000000149011612
                    continue

                # DAMAGE 
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 28
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.125
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 30000
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 18
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.65, 0.85)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(0.65, 0.85)
                #                     continue
                
        # AR18
        if item["Name"] == "AR18":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Brownells BRN-180S"
                    continue

                # PUSHBACK RANGE
                if item_data["Name"] == "PushbackRange":
                    item_data["Value"] = 160
                    continue

                # LOW-READY RANGE
                if item_data["Name"] == "LowReadyRange":
                    item_data["Value"] = 75
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.9
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.6
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 52.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.1
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 36.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.4)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.4)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.11999999731779099:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.4)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.05000000074505806:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.4)
                #                     continue

        # SR16
        if item["Name"] == "SR16":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "KAC SR-16 CQB"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.79
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 100886
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 40
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.15000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.6)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.6)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.20999999344348908:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.6)
                #                     continue
                
        # BCM MK1
        if item["Name"] == "BCM_MK1":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "BCM CQB-11"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.5799999237060547
                    continue

                # PUSHBACK RANGE
                if item_data["Name"] == "PushbackRange":
                    item_data["Value"] = 160
                    continue

                # LOW-READY RANGE
                if item_data["Name"] == "LowReadyRange":
                    item_data["Value"] = 65
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 100886
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 40
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.15000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.35)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.35)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.20999999344348908:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.2, 1.35)
                #                     continue

        # SBR
        if item["Name"] == "SBR":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Wilson Combat SBR Tactical"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.63
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 99159
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 38
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.25, 1.35)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.25, 1.35)
                #                     continue

        # HK416
        if item["Name"] == "HK416":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K HK416 A5"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.12
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 92145
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 37
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.30000001192092896:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.35, 1.55)
                #                     continue
                
        # SCAR-L
        if item["Name"] == "SCARL":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "FN MK 16 MOD 0"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.04
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.53
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 50
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 87757
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 32.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.3, 1.45)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.3, 1.45)
                #                     continue

        # SLR47
        if item["Name"] == "SLR47":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Arsenal SLR-107UR"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 2.75
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.7
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 55
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.2
                #     continue

                # # MUZZLE VELOCITY
                # if item_data["Name"] == "ProjectileMovementSpeed":
                #     item_data["Value"] = 90525
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 38.5
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.34999999403953552:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.85, 2.1)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.34999999403953552:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.85, 2.1)
                #                     continue

        # P90
        if item["Name"] == "P90":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "FN P90 TR"
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.65
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.2
                    continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

    #----------- HANDGUNS

        # TASER
        if item["Name"] == "Taser":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M26 Taser"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:
                        
                        # TRANSLATION
                        if def_meshspace["Name"] == "Translation":
                            
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.87
                                continue

        # G19
        if item["Name"] == "G19":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Glock 19 Gen. 5"
                    continue

                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "Chambered in 9x19mm, the Glock 19's dependability and high capacity in an age when revolvers still ruled the world have found it a permanent home in public and private security agencies worldwide."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.61
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.245
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.06
                    continue

                # MAG SIZE
                if item_data["Name"] == "MagazineSize":
                    item_data["Value"] = 20
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:
                        
                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["X"] = 7
                                translation_array["Value"]["Y"] = -4.85
                                translation_array["Value"]["Z"] = -0.75
                                continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 25
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 13
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.35, 1.5)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.35, 1.5)
                #                     continue

        # PFC9
        if item["Name"] == "PFC9":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Polymer80 PFC9"
                    continue

                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "Chambered in 9x19mm, the Glock 19's dependability and high capacity in an age when revolvers still ruled the world have found it a permanent home in public and private security agencies worldwide."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.61
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.18
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.06
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:
                        
                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["X"] = 7
                                translation_array["Value"]["Y"] = -4.85
                                translation_array["Value"]["Z"] = -0.75
                                continue
                
                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 25
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 13
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.35, 1.5)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.35, 1.5)
                #                     continue

        # M2011
        if item["Name"] == "M2011":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Colt M45A1"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 1.7
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.34999999403953552
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.15000000596046448
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.85
                                continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 32.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.025
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.1, 2.25)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.1, 2.25)
                #                     continue

        # USP
        if item["Name"] == "USP":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K USP.45 Tactical"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.88999998569488525
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -3.38
                                translation_array["Value"]["Z"] = -0.5
                                continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 32.5
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.025
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2, 2.2)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2, 2.2)
                #                     continue

        # FiveSeven
        if item["Name"] == "FiveSeven":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "FN Five-Seven USG"
                    continue

                # MAG WEIGHT FULL
                if item_data["Name"] == "MagazineWeightFull":
                    item_data["Value"] = 0.35
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.135
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.62
                                continue

                # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1.05
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.075
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue
                
        # Python
        if item["Name"] == "Python":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Colt Python"
                    continue

                # MAG WEIGHT EMPTY
                if item_data["Name"] == "MagazineWeightEmpty":
                    item_data["Value"] = 0.125
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.81
                                continue

                # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.6, 2.8)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.20000000298023224:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.6, 2.8)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.10000000149011612:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(2.6, 2.8)
                #                     continue
        
        # M92A3
        if item["Name"] == "M92A3":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Beretta M92X Performance"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.4
                                continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 25
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 13
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue

        # P229
        if item["Name"] == "P229":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Sig-Sauer P229"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.964
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["X"] = 7
                                translation_array["Value"]["Y"] = -3.75
                                continue

                # DAMAGE
                # if item_data["Name"] == "Damage":
                #     item_data["Value"] = 25
                #     continue

                # # DAMAGE SEVERITY MULTIPLIER
                # if item_data["Name"] == "DamageSeverityMultiplier":
                #     item_data["Value"] = 1
                #     continue

                # # DAMAGE SEVERITY CHANCE
                # if item_data["Name"] == "DamageSeverityChance":
                #     item_data["Value"] = 0.025
                #     continue

                # # BLEEDOUT DAMAGE MULTIPLIER
                # if item_data["Name"] == "BleedoutDamageMultiplier":
                #     item_data["Value"] = 0.05
                #     continue

                # # BLEEDOUT DAMAGE CHANCE
                # if item_data["Name"] == "BleedoutDamageChance":
                #     item_data["Value"] = 0.05
                #     continue

                # # PENETRATION
                # if item_data["Name"] == "PenetrationDistance":
                #     item_data["Value"] = 13
                #     continue

                # # RECOIL PATTERN
                # if item_data["Name"] == "RecoilPattern":
                    
                #     for recoil_main in item_data["Value"]:
                        
                #         # ENTER RECOIL ARRAY
                #         if recoil_main["Name"] == "RecoilPattern":
                            
                #             # ENTER RECOIL OBJECT
                #             for recoil_array in recoil_main["Value"]:
                #                 if recoil_array["Value"]["Yaw"] == -0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.5:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == 0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue
                #                 elif recoil_array["Value"]["Yaw"] == -0.40000000596046448:
                #                     recoil_array["Value"]["Pitch"] = random.uniform(1.4, 1.55)
                #                     continue

    #----------- LONG TACTICAL

        # VKS
        if item["Name"] == "VKS":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "PepperBall VKS"
                    continue

        # BREACHING SHOTGUN
        if item["Name"] == "S590_Breach":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M500 Cruiser - Breaching Shotgun"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "This version of the Mossberg 500 allows you to quickly and effectively blow open doors using frangible slugs. Not ideal for combat."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.2
                    continue

        # M32A1
        if item["Name"] == "M32A1":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M32A1 MGL Flashbang Launcher"
                    continue

        # M320 GAS
        if item["Name"] == "M320_Gas":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K M320 Gas Grenade"
                    continue

        # M320 BANG
        if item["Name"] == "M320_Bang":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K M320 Flashbang"
                    continue

        # M320 STINGER
        if item["Name"] == "M320_Stinger":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K M320 Stinger"
                    continue

        # MIRRORGUN - EMPTY
        if item["Name"] == "Mirrorgun":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                continue

        # BATTERING RAM
        if item["Name"] == "BatteringRam":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "Knock, knock. Used for getting past doors. Just don't get caught in one of those fail compilations..."
                    continue

        # TAC700
        if item["Name"] == "TAC700":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "TAC-700"
                    continue
                
    #----------- GRENADES

        # 9-BANGER
        if item["Name"] == "9Banger":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "CTS 7290-9 9 Banger"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "Just as the M84, this grenade blinds and disorients those caught in its blast but detonates 9 times at intervals of 0.25 seconds."
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.55
                    continue

        # CS GAS
        if item["Name"] == "CSGas":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M7A3 CS Gas Grenade"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.44
                    continue

        # M84 FLASHBANG
        if item["Name"] == "Flashbang":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M84 Stun Grenade"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.37
                    continue

        # STINGER
        if item["Name"] == "Stinger":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Model 9590 Stingball"
                    continue
                
                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 0.275
                    continue

    #----------- OTHER EQUIPMENT

        # BALLISTIC MASK
        if item["Name"] == "BallisticMask":

            for item_data in item["Value"]:

                if item_data["Name"] == "ItemCategories":
                    dic = item_data["Value"][0].copy()
                    dic["Value"] = "EItemCategory::IC_Goggles"
                    item_data["Value"].append(dic)
                    continue  

    #----------- NOT USED

        #----------- PRIMARIES

        # AKS74U
        if item["Name"] == "AKS74U":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "AKS-74U"
                    continue

        # M16A4 - EMPTY
        if item["Name"] == "M16A4":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                continue
                
        # G3A3
        if item["Name"] == "G3A3":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "H&K G3A3"
                    continue
                
        # M37
        if item["Name"] == "M37":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Wincherster Model 1897"
                    continue
                
        # MPL
        if item["Name"] == "MPL":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Walther MPL"
                    continue
                
        # AKM
        if item["Name"] == "AKM":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "AKM"
                    continue
                
        # UZI
        if item["Name"] == "UZI":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "IMI Uzi"
                    continue
                
                # DESCRIPTION
                if item_data["Name"] == "ItemDescription":
                    item_data["CultureInvariantString"] = "The Uzi is a Izraeli open-bolt, blowback-operated submachine gun first designed in the late 1940s and finished in 1950. Since then The Uzi has been exported to over 90 countries and it's been sold to more military, law enforcement and security markets than eny other submachine gun ever made."
                    continue

        # M14
        if item["Name"] == "M14":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M14"
                    continue
                
        # AK102
        if item["Name"] == "AK102":
            
            # For every piece of the item data.
            for item_data in item["Value"]:

                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "AK-102"
                    continue
                
        # AK103
        if item["Name"] == "AK103":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "AK-103"
                    continue
                
        # M76
        if item["Name"] == "M76":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Smith & Wesson Model 76"
                    continue

        # Sawnoff
        if item["Name"] == "Sawnoff":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "12 Gauge Double Barreled Sawed-Off"
                    continue

        # M249
        if item["Name"] == "M249":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "M249 Para"
                    continue

        # S590 Assault V2
        if item["Name"] == "S590_Assault_V2":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Mossberg 500"
                    continue

                # WEIGHT
                if item_data["Name"] == "ItemWeight":
                    item_data["Value"] = 3.2
                    continue
                
        # Saiga12
        if item["Name"] == "Saiga12":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Izhmash KS-K"
                    continue
                
        # SCARH
        if item["Name"] == "SCARH":
            
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "FN MK 17 MOD 0"
                    continue

        #----------- HANDGUNS

        # P250
        if item["Name"] == "P250":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Sig-Sauer P250"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -7.35
                                translation_array["Value"]["Z"] = -1.5
                                continue

        # M9A1
        if item["Name"] == "M92FS":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Beretta M92FS"
                    continue

            # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:
                        
                        # TRANSLATION
                        if def_meshspace["Name"] == "Translation":
                            
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -6.4
                                translation_array["Value"]["Z"] = -2
                                continue
        
        # Makarov
        if item["Name"] == "Makarov":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Makarov PM"
                    continue

        # Tec9
        if item["Name"] == "Tec9":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Intratec TEC-9"
                    continue

        # G18
        if item["Name"] == "G18":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Glock 18C"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["X"] = 7
                                translation_array["Value"]["Y"] = -4.85
                                translation_array["Value"]["Z"] = -0.75
                                continue

        # M1911
        if item["Name"] == "M1911":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Colt M1911A1"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:
                        
                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -4.85
                                continue

        # P99
        if item["Name"] == "P99":
            # For every piece of the item data.
            for item_data in item["Value"]:
                
                # NAME
                if item_data["Name"] == "ItemName":
                    item_data["CultureInvariantString"] = "Walther PPQ"
                    continue

                # MESHSPACE DEFAULT
                if item_data["Name"] == "MeshspaceTransform_Default":
                    
                    for def_meshspace in item_data["Value"]:

                        # ENTER TRANSLATION ARRAY
                        if def_meshspace["Name"] == "Translation":
                            
                            # ENTER TRANSLATION OBJECT
                            for translation_array in def_meshspace["Value"]:
                                translation_array["Value"]["Y"] = -6.85
                                translation_array["Value"]["Y"] = -0.5
                                continue

# SAVE INTO FILE
json.dump(data, open(f"ItemDataTable.json", "w"), indent = 1)

# OPEN UASSET
subprocess.call([path_to_uasset, "ItemDataTable.json"])
