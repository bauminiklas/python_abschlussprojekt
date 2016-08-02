from PIL import Image,ImageDraw

class ReferenceSurvey:
    def __init__(self):
        self.referenceCorners = self.readOutLines()
                
    def readOutLines(self):
        with open("test_daten",'r') as f:
            data = f.readlines()
        referenceCorners = []
        for line in data:
            words = line.split()
            referenceCorners.append([int(i) for i in words])
        return referenceCorners
        f.close()



    def getReferenceCorners(self):
        return self.referenceCorners
        
    def getBoxPositions(self):        
        pass        
        
    def drawReferenceSurvey(self):        
        im = Image.open("boegen/Bogen1.jpg").convert("RGB")
        for i in range(0,len(self.referenceCorners)):
            x = self.referenceCorners[i][0]
            y = self.referenceCorners[i][1]
            r = 8
            draw = ImageDraw.Draw(im)
            draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,0))            
        im.save("boegen/Bogen1_marked.jpg")
        
referenceSurvey = ReferenceSurvey()
referenceSurvey.drawReferenceSurvey()