class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not typed or len(typed) < len(name):
            return False
        if name[0] != typed[0]:
            return False
        
        p1 = 1 # p1: name  p2: typed
        p2 = 1
        while p2 <= len(typed) -1 and p1 <= len(name) -1:
            if typed[p2] == typed[p2-1] and typed[p2] != name[p1]:
                p2 +=1
            elif typed[p2] == name[p1]:
                p1 +=1
                p2 +=1
            elif typed[p2] != name[p1]:
                return False
        if p1 == len(name) and p2 == len(typed): #p1,p2都走完了
            return True
        elif p1 < len(name): #p1 name没走完
            return False
        elif p2 < len(typed):#p2 typed没走完
            if len(set(typed[p2-1:])) == 1:
                return True
            else:
                return False
        else:
            return False