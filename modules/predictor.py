def EAR_Predictor(val, threshold):
    if (sum(val)/len(val)) < threshold:
        return 1
    else:
        return 0
    
def MAR_Predictor(val, threshold):
    if (sum(val)/len(val)) < threshold:
        return 1
    else:
        return 0
    
def classify(ear, mar, thresholds):
    if thresholds == "default":
        thresholds = [0.2, 1.5]
    ear = EAR_Predictor(ear, thresholds[0])
    mar = MAR_Predictor(mar, thresholds[1])
    
    if (ear == 1 or mar == 1):
        return 1
    else:
        return 0