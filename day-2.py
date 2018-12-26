from collections import defaultdict

def task_1(path_to_file):
    exactly_two = exactly_three = 0
    checksum = 0
    with open(path_to_file,"r") as input:
        for line in input:
            letter_dict = defaultdict(lambda:0)
            for letter in line.strip():
                letter_dict[letter] += 1
            letter_values = letter_dict.values()
            if( 2 in letter_values ):
                exactly_two += 1
            if( 3 in letter_values ):
                exactly_three += 1
    checksum = exactly_two * exactly_three
    return checksum

def task_2(path_to_file):
    with open(path_to_file,"r") as input:
        pattern_set = set()
        for line in input:
            line = line.strip()
            for i in range(len(line.strip())):
                pattern_string = line[:i] + '_' + line[i+1:]
                if pattern_string in pattern_set:
                    return ''.join(n for n in pattern_string if n != '_')
                    
                pattern_set.add(pattern_string)

result_1 = task_1("day-2-input.txt")
result_2 = task_2("day-2-input.txt")
print("Task 1 result = {}\nTask 2 result = {}".format(result_1, result_2))