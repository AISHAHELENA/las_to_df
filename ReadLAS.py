import lasio
import os
import pandas as pd

def Get_Las_Files(path=None):
    Wellname = []
    CurveName = []
    Data = []
    frames = []
    rejected_files=[]


    x = os.listdir(path)


    #Get Well Name
    for files in x:
        f = str(files)
        try:
            las = lasio.read(path+f)
            #Get wellnames
            well = las.well.WELL.value
            Wellname.append(well)
            #Get curve names
            curves = las.keys()
            CurveName.append(curves)
            #Get data
            data = las.data
            Data.append(data)

            #Create dataframe per well
            df = pd.DataFrame(data = data, columns=curves)
            df["Wellname"] = well
            frames.append(df)
            
        except:
            rejected_files.append(files)

    #Concat all the df containing one well into one big df
    result = pd.concat(frames, sort=True)
    result.reset_index(inplace=True)
    
    return (result, rejected_files)
    
