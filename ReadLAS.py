import lasio
import os
import pandas as pd

def Get_Las_Files(path=None, filename=None):
    Wellname = []
    CurveName = []
    Data = []
    frames = []
    rejected_files=[]


    #path = "Open_Source_data_KGS/Logs/"
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

    result = pd.concat(frames, sort=True)
    result.reset_index(inplace=True)
    result.to_csv(filename)
    print (f'The rejected files in the directory are {rejected_files}')