class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):
    c=0
    l3=ListNode()
    temp=l3

    while l1 or l2 or c:
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0

        total=v1+v2+c
        c=total//10
        d=total%10

        temp.val=d

        temp.next=ListNode(d)
        temp=temp.next

        if l1:
            l1=l1.next
        if l2:
            l2=l2.next

    return l3.next





