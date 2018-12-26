def task_1(path_to_file):
    final_sum = 0
    with open(path_to_file,"r") as input:
        for line in input:
            num = int(line.strip())
            final_sum += num
    return final_sum         

def task_2(path_to_file):
    diff_values = set()
    no_reoccurrence = True
    temp_sum = 0
    diff_values.add(temp_sum) # Adding 0 as first occurrence!
    while(no_reoccurrence):
        with open(path_to_file,"r") as input:
            for line in input:
                num = int(line.strip())
                temp_sum += num
                if temp_sum in diff_values:
                    reoccurrence = temp_sum
                    return reoccurrence
                else:
                    diff_values.add(temp_sum)

result_1 = task_1("day-1-input.txt")
result_2 = task_2("day-1-input.txt")
print("Task 1 result = {}\nTask 2 result = {}".format(result_1, result_2))