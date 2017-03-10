import timeit
class bubbleStringList:

    def add(self, string):
        st1 = self
        st2 = string 
        split = string.split()

        if split == '':
            print("nothing stored")

        else:
             UserL = split
             return UserL

    def sort(self,astring):
        choose = list(astring) 
        #print(choose)
        
        for pass_n in range(len(choose) -1, 0, -1):
            for i in range (pass_n):
                if choose[i] > choose[i + 1]:
                    temp = choose[i]
                    choose[i] = choose[i + 1]
                    choose[i + 1] = temp
        return choose


            
cd = bubbleStringList()
astring = '3', '5', '8', '9', '4'

print("the initial string is" ,  astring)
print("the string sorted is " , cd.sort(astring))

#t = timeit.Timer("bubble.sort(self, astring)", "import bubble")
#results = t.repeat(5,1000)
#for i, item in enumerate(results):
    #print(i, "\t", item)




