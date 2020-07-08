class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for i in range(n-1):  
            #循环一次得到第二行的数列
            #循环两次得到第三行的数列
            #循环n-1次得到第n行的数列  i从0到n-2  循环了n-1次
            seq = self.getNext(seq)
        return seq
    def getNext(self,seq):
        result =''
        i = 0
        while i < len(seq):
            count = 1 
            while i < len(seq) -1 and seq[i] == seq[i+1]:
                count +=1
                i +=1
            result +=str(count)
            result +=(seq[i])
            i +=1
        return result             
