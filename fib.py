class Fibonacci:

    def __init__(self):
        pass

    def sequence(self, n):
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ... 
        
        # first is 0, second is 1, third is 1, ... so its fib(n-1) + fib(n-2)

        if n <= 1:
            return n
        else:
            return self.sequence(n-1) + self.sequence(n-2)

def main():
    myObj = Fibonacci()
    print(myObj.sequence(6))

main()