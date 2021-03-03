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
    def queueLen(self):
        return len(self.queue)

mychu=20
next=2
mychuq=ListQueue()
mychuq.enQueue([1,1])
tmp_front=''
while mychu>0:
    tmp_front=mychuq.deQueue()
    mychu-=tmp_front[1]
    tmp_front[1]+=1
    mychuq.enQueue(tmp_front)
    mychuq.enQueue([next,1])
    next+=1
    input('엔터를 치면 현황을 알 수 있습니다')
    print('큐에 있는 사람 수: {}, 지금 {}에게 나눠준 사탕의 수: {}, 현재까지 나눠준 사탕의 수: {}'.format(mychuq.queueLen(), tmp_front[0], tmp_front[1], 20-mychu))
print('마지막꺼는 {}가 가져간다  \\>o</'.format(tmp_front[0]))