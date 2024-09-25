class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
    def frequency_table(columnName,dataset):
        frequency_table=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","cumsum"])
        frequency_table["Unique_values"]=dataset[columnName].value_counts().index
        frequency_table["Frequency"]=dataset[columnName].value_counts().values
        frequency_table["Relative_Frequency"]=(frequency_table["Frequency"]/103)
        frequency_table["cumsum"]=frequency_table["Relative_Frequency"]
        return frequency_table
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%",
                                    "IQR","1.5rule","Lesser","Greater","min","max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5* descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["min"]=dataset[columnName].min()
            descriptive[columnName]["max"]=dataset[columnName].max()
        return descriptive
    def outlier_columnName():
        Lesser=[]
        Greater=[]
        for columnName in quan:
            if(descriptive[columnName]["min"]<descriptive[columnName]["Lesser"]):
                Lesser.append(columnName)
            if(descriptive[columnName]["max"]>descriptive[columnName]["Greater"]):
                Greater.append(columnName) 
    def Replacing_outlier_columnName():
        
        for columnName in Lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
        for columnName in Greater: 
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]