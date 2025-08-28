class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list=[]
        for m in range(1,n+1):
            if m%3==0 and m%5==0:
                temp="FizzBuzz"
            elif m%3==0: temp="Fizz"
            elif m%5==0: temp="Buzz"
            else: temp=str(m)
            list.append(temp)
        return list