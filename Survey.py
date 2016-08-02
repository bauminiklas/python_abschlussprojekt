from PIL import Image
from ReferenceSurvey import ReferenceSurvey


class Survey:
    def __init__(self, name, referenceSurvey):
        self.name = name
        self.calculateTransformation(referenceSurvey)
   
        
    def calculateTransformation(self, referenceSurvey):
        referenceCorners = referenceSurvey.getReferenceCorners()


        im = Image.open("boegen/" + self.name)

        ul = Image.open("masks/ul.png")
        ur = Image.open("masks/ur.png")        
        lr = Image.open("masks/lr.png")
        ll = Image.open("masks/ll.png")     


#        cropbox_ul = (referenceCorners[0][0], referenceCorners[0][1], ul.size[0] + referenceCorners[0][0], ul.size[1] + referenceCorners[0][1])
#        cropbox_ur = (referenceCorners[1][0], referenceCorners[1][1], ur.size[0], ur.size[1])
#        cropbox_lr = (referenceCorners[2][0], referenceCorners[2][1], lr.size[0], lr.size[1])
#        cropbox_ll = (referenceCorners[3][0], referenceCorners[3][1], ll.size[0], ll.size[1])
#        im_ul = im.crop(cropbox_ul)
#        print(ul.histogram())
#        im_ul.show()
        
        im.paste(ul, (referenceCorners[0][0], referenceCorners[0][1]))
        im.show()

    def transformation(self):
        pass
    
refsurv = ReferenceSurvey()
survey = Survey("Bogen1.jpg",refsurv)