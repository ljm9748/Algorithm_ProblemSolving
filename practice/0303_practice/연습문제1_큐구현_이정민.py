# 리스트큐
class ListQueue:
    def __init__(self):
        self.queue=[]

    def enQueue(self,A):
        self.queue.append(A)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.queue[0]

# 배열큐
class ArrayQueue:
    def __init__(self,size):
        self.size=size
        self.queue=['']*size
        self.front=self.rear=-1

    def enQueue(self,A):
        if self.isFull():
            print('Queue is Already Full')
        else:
            self.rear+=1
            self.queue[self.rear]=A


    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            self.front+=1
            return_tmp=self.queue[self.front]
            self.queue[self.front]=''
            return return_tmp


    def isEmpty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def isFull(self):
        if self.size-1==self.rear:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.queue[self.front+1]

# 실행부분
print('LIST QUEUE')
listqueue=ListQueue()
print(listqueue.isEmpty())
listqueue.enQueue(1)
listqueue.enQueue(2)
listqueue.enQueue(3)
print(listqueue.deQueue())
print(listqueue.deQueue())
print(listqueue.deQueue())

print('ARRAY QUEUE')
arrayqueue=ArrayQueue(3)
print(arrayqueue.isEmpty())
arrayqueue.enQueue(1)
arrayqueue.enQueue(2)
arrayqueue.enQueue(3)
print(arrayqueue.isFull())
print(arrayqueue.deQueue())
print(arrayqueue.deQueue())
print(arrayqueue.deQueue())
