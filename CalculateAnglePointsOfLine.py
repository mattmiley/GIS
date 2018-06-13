import math, arcpy


fc = 'C://Users//mmiley2//Projects//nrc//LineAngles.gdb//Water_Utilities//Water_Lines'
anglePoints = 'C://Users//mmiley2//Projects//nrc//LineAngles.gdb//Water_Utilities//anglePoints'
sr = arcpy.Describe(fc).spatialReference
arcpy.Delete_management(anglePoints)
arcpy.CreateFeatureclass_management('C://Users//mmiley2//Projects//nrc//LineAngles.gdb//Water_Utilities','anglePoints',"POINT",spatial_reference=sr)  
arcpy.AddField_management(anglePoints,'Angle',"DOUBLE")  
insCur = arcpy.da.InsertCursor(anglePoints,('SHAPE@','Angle'))  
with arcpy.da.SearchCursor(fc,["SHAPE@"]) as cursor:    
    for row in cursor:    
        for part in row[0]:      
            pt_count = 1    
            for pnt in part:    
                pnt = arcpy.PointGeometry(pnt,sr)    
                if pt_count > 1:    
                    if pt_count >2:    
                        distAB = oneBack.distanceTo(twoBack)    
                        distBC = pnt.distanceTo(oneBack)    
                        distAC = pnt.distanceTo(twoBack)    
                        FirNum = (((distAB*distAB)+(distBC*distBC))-(distAC*distAC))/(2*distAB*distBC)

                        if FirNum >= -1 and FirNum <= 1:
                            aacos = math.acos(FirNum)
                            angB = math.degrees(aacos)  
                            insCur.insertRow((oneBack,angB))   
                            print(str(angB))
                    twoBack = oneBack    
                oneBack = pnt    
                pt_count += 1  
del insCur