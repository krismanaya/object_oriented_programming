#python2
"""Create a simple class, MaxSizeList, 
	   that acts a little bit like a list, 
	   with a pre-configured limit on its size."""

class MaxSizeList:
    
    def __init__(self,val): 
        self.val = val 
        self.list = []
        
    def push(self,str):
        self.str = str 
        return self.list.append(self.str)
    
    def get_list(self):
        max_size = True 
        while max_size: 
            if len(self.list) > self.val: 
                self.list.pop(0)
            else: 
                max_size = False 
        return self.list


a = MaxSizeList(3) #instances 
b = MaxSizeList(1) #instances

a.push('hey')
a.push('hi')
a.push("let's")
a.push('go')

b.push('hey')
b.push('hi')
b.push("let's")
b.push('go')

print(a.get_list())
print(b.get_list())
	# ['hi','lets','go']
	# ['go']


#teacher's answer it's faster
class MaxSizeList(object): 

	def __init__(self,max): 
		self.max = max
		self.innerlist = []

	def push(self,obj): 
		self.innerlist.append(obj)
		if len(self.innerlist) > self.max: 
			self.innerlist.pop(0)

	def get_list(self): 
		return self.innerlist