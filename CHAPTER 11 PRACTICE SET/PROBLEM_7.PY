# override THE len() method on vector problem 5 to display the dimentsion of the vector
class vector:
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)
    
#test the implementation
v1=vector([1,2,3])
print(len(v1))