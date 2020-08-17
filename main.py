num_str = input("Choose a number: ")
num = int(num_str)
squares_list = [f"{x} squared is {x*x}" for x in range(1, num + 1)]
print("\n".join(squares_list))
                



