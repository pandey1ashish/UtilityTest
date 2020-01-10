#! /usr/bin/python3

class MathUtil():
    def addFun(self, numOne, numTwo):
        return numOne + numTwo




try:
    obj = MathUtil()
    print(obj)
    print(obj.addFun(1,2))
except Exception as e:
    print('Exception: %s'%e)
finally:
    print('Final Clouser Block')
