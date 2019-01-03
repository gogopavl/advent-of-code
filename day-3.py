from collections import defaultdict

claim_dict = defaultdict(int)

def task_1(path_to_file):
    for line in open(path_to_file, "r"):
        parts = line.strip().split()
        # claim_id = parts[0].strip()
        first_coord, second_coord = parts[2].strip().split(",")
        first_coord, second_coord = int(first_coord), int(second_coord[:-1])
        width, height = parts[3].strip().split("x")
        width, height = int(width), int(height)

        for h in range(height):
            for w in range(width):
                claim_dict[(first_coord+w, second_coord+h)] +=1
    overlapping_in = 0

    for key, val in claim_dict.iteritems():
        if val >= 2:
            overlapping_in += 1

    return overlapping_in

def task_2(path_to_file):
    for line in open(path_to_file, "r"):
        parts = line.strip().split()
        claim_id = parts[0].strip()
        first_coord, second_coord = parts[2].strip().split(",")
        first_coord, second_coord = int(first_coord), int(second_coord[:-1])
        width, height = parts[3].strip().split("x")
        width, height = int(width), int(height)

        non_overlapping = True
        for h in range(height):
            for w in range(width):
                if claim_dict[(first_coord+w, second_coord+h)] > 1:
                    non_overlapping = False
                    break
        if non_overlapping:
            return claim_id

result_1 = task_1("day-3-input.txt")
result_2 = task_2("day-3-input.txt")

print("Task 1 answer = {}\nTask 2 answer = {}".format(result_1, result_2))
