"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #13 - Matrix Multiplication (matmux.py)


Author: Ainsley Ward

Difficulty Level: 6/10

Prompt: You want to get ahead in your linear analysis class, so you decide to make a program 
that calculates the product of two 2x2 matrices. Your inputs should be two arrays, each 
representing a 2x2 matrix to be multiplied. (Don’t use numpy tdo solve this!!)

Test Cases:
input: m1 = [[4, 2],[3, 1]]; m2 = [[5, 6], [3, 8]]; output = [[26, 40], [18, 26]]
input: m1 = [[0, 0],[0, 0]]; m2 = [[5, 6], [3, 8]]; output = [[0, 0], [0, 0]]
input: m1 = [[14, 2],[7, 1]]; m2 = [[8, 6], [0, 8]]; output = [[112, 100], [56, 50]]
"""

class Solution:
    def matrix_mult(self,m1, m2):
        # type m1: list
        # type m2: list
        # return: List[List[int]]
        
        # TODO: Write code below to return a nested list with the solution to the prompt
        com1 = []
        first = m1[0]*m2[0] + m1[1]* m2[2]
        second = m1[0]*m2[1] + m1[1]* m2[3]
        com1= list.append(first)
        com1 = list.append(second)
        third =m1[2]*m2[0] + m1[3]* m2[2]
        fourth = m1[2]*m2[1] + m1[3]* m2[2]
        com2 = []
        com2 = list.append(third)
        com2 = list.append(fourth)
        anw = []
        anw = list.append(com1)
        anw = list.append(com2)
        return anw

def main():
    array1 = input().split(" ")
    array2 = input().split(" ")
    array3 = input().split(" ")
    array4 = input().split(" ")

    for x in range (0, len(array1)):
        array1[x] = int(array1[x])

    for x in range (0, len(array2)):
        array2[x] = int(array2[x])

    for x in range (0, len(array3)):
        array3[x] = int(array3[x])

    for x in range (0, len(array4)):
        array4[x] = int(array4[x])

    ary1 = [array1,array2]
    ary2 = [array3,array4]

    tc1 = Solution()
    ans = tc1.matrix_mult(ary1,ary2)
    print(ans)

if __name__ == "__main__":
    main()