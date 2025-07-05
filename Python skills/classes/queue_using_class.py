class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return '<back> ['+','.join(map(str,self.queue))+'] <front>'

    def into(self,obj):
        self.queue.insert(0,obj) #push el in queue back
        return self

    def take(self):
        if self.queue:
            return self.queue.pop() #pop el from queue front
        else:
            return None

    def len(self):
        return len(self.queue)

    def front(self):
        if self.queue:
            return self.queue[len(self.queue)-1] #show first el of queue
        else:
            return not self.queue

    def back(self):
        if self.queue:
            return self.queue[0] #show last el of queue
        else:
            return None

    def empty(self):
        return not self.queue

    def clear(self):
        self.queue=[]

    #find el in queue and return indexses
    def find(self, key=lambda x: True): 
        try:
            indexlist = [ i for i in range(len(self.queue))
                         if key(self.queue[i]) ]
            return indexlist
        except:
           return []
        pass

    #pop el from position k
    def remove(self,k):
        if 0<=k<len(self.queue):
            y=self.queue[k]; del self.queue[k:k+1]; return y
        else:
            return None

    def all(self):
        return self.queue

def main():
    q=Queue()

main()
    
