def f_input():
    with open("day3_input.txt", "r") as file:
        return [[ch for ch in line.strip()] for line in file.readlines()]


lines = f_input()
bits = len(lines[0])
len_lines = len(lines)
# data = {"0": 0, "1": 0}

# gamma = []
# epsilon = []

oxigen_lines = [1] * len_lines
co2_lines = [1] * len_lines

for bit in range(bits):
    data_o = {"0": 0, "1": 0}
    data_co2 = {"0": 0, "1": 0}
    count_o = len_lines
    count_co2 = len_lines

    for idx in range(len_lines):
        if oxigen_lines[idx] == 1:
            data_o[lines[idx][bit]] += 1
        if co2_lines[idx] == 1:
            data_co2[lines[idx][bit]] += 1
    if count_o > 1:
        if data_o["0"] > data_o["1"]:
            for idx in range(len_lines):
                if lines[idx][bit] != "0":
                    oxigen_lines[idx] = 0
                    count_o -= 1
        else:
            for idx in range(len_lines):
                if lines[idx][bit] != "1":
                    oxigen_lines[idx] = 0
                    count_o -= 1

    if count_co2 > 1:
        if data_co2["0"] < data_co2["1"]:
            for idx in range(len_lines):
                if lines[idx][bit] != "0":
                    co2_lines[idx] = 0
                    count_co2 -= 1
        else:
            for idx in range(len_lines):
                if lines[idx][bit] != "1":
                    co2_lines[idx] = 0
                    count_co2 -= 1

print(f"sum o {sum(oxigen_lines)}")
print(f"sum co {sum(co2_lines)}")
for idx in range(len_lines):
    if oxigen_lines[idx] == 1:
        print(f"oxigen = {lines[idx]}")
    if co2_lines[idx] == 1:
        print(f"co2 = {lines[idx]}")




    # if data["0"] > data["1"]:
    #     gamma.append("0")
    #     epsilon.append("1")
    # else:
    #     gamma.append("1")
    #     epsilon.append("0")


# gamma = int(str("".join(gamma)),2)
# epsilon = int(str("".join(epsilon)),2)
# print(f'power  = {gamma * epsilon}')






