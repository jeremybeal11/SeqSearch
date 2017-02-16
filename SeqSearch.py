class SequentialStringList:
   
   
    def add(self, sce):
        test = sce.split()
        if test == '':
            print("nothing stored")

        else:
             UserL = test
             #print(UserL)
             return UserL

    def find (self, sce, gogo):
        found = False
        count = 0
        #gofind = self.findstr.split()
        hey = sce.split()
        while count < len(hey) and not found:
            if hey[count] == gogo:
                found = True
                print("it found", gogo )
            else:
                count = count + 1
                
                
        return found



newstring = "hey how are you ?"
findstr = "you"

Seq = SequentialStringList()
#print(newstring)
Seq.add(newstring)
print(Seq.find(newstring, findstr))

