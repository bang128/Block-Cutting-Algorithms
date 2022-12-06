import time
import algorithms

def test(input_file):
    input = open(input_file, "r")
    data = input.readlines()
    block_weight = int(data[0])
    weight_cost = {}

    for i in range(1, len(data)):
        d = data[i].split()
        weight_cost.update({int(d[0]): int(d[1])})

    print("\tBrute_Force:")
    start = time.time()
    print("\t\tResult:", algorithms.brute_force(block_weight, weight_cost))
    end = time.time()
    print("\t\tElapsed time:", end - start)

    print("\tDynamic:")
    start = time.time()
    print("\t\tResult:", algorithms.dynamic(block_weight, weight_cost))
    end = time.time()
    print("\t\tElapsed time:", end - start)

    print("\tGreedy:")
    start = time.time()
    print("\t\tResult:", algorithms.greedy(block_weight, weight_cost))
    end = time.time()
    print("\t\tElapsed time:", end - start)

    print()

def main():
   print("Test case 1:")
   test("test1.txt")


   print("\nTest case 2:")
   """There are 2 optimal solutions:
      1. result = 78, [2, 3, 3, 3, 3, 3, 3] 
      2. result = 78, [3, 17]
   The actual results of 3 algorithms are all 78, [3, 17]
   -> Prioritize the shorter way
   """
   test("test2.txt")

   print("\nTest case 3:")
   test("test3.txt")

   print("\nTest case 4:")
   test("test4.txt")
   """There are 2 optimal solutions:
         1. result = 24, [9, 9] 
         2. result = 24, [6, 12]
         3. result = 24, [10, 6, 2]
      The actual results of brute-force and dynamic algorithms are both 24, [6, 12]
      The actual result of greedy algorithm is 24, [10, 6, 2]
      Knowing that both 10-weight and 12-weight pieces cost 16 (highest), and 10-weight appears before 12-weight 
      in the input file
   -> Brute-force and Dynamic tends to result in greedy and shorter solution if there are more than 1 solutions 
      with the same length
   -> Greedy algorithm tends to result in the first greedy solution if there are more than 1 greedy solutions.
   """

   print("\nTest case 5:")
   test("test5.txt")






if __name__ == '__main__':
    main()