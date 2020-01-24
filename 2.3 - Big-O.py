#O(n^2) algorithm to find smallest number in a list

def smallestNumber1(input_list):
    print("HI!")
    smallest = input_list[0]
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i == j:
                continue
            if input_list[i] < input_list[j]:
                if input_list[i] < smallest:
                    smallest = input_list[i]
    return smallest

#O(N) algorithm to find smallest number in a list
def smallestNumber2(input_list):
    smallest = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] < smallest:
            smallest = input_list[i]
    return smallest


def main():
    list1 = [9,5,2,1,7]

    print(smallestNumber1(list1))
    print(smallestNumber2(list1))

main()
