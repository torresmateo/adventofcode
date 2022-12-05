count_fc = 0
count_ol = 0
for line in open("day4.input"):
    r1, r2 = line.strip().split(",")
    r1_l, r1_h = [int(i) for i in r1.split("-")]
    r2_l, r2_h = [int(i) for i in r2.split("-")]
    if (r1_l <= r2_l and r1_h >= r2_h) or (r2_l <= r1_l and r2_h >= r1_h):
        count_fc += 1
        count_ol += 1
    elif r2_l <= r1_h <= r2_h or r1_l <= r2_h <= r1_h:
        count_ol += 1

print(f"part 1: {count_fc}")
print(f"part 2: {count_ol}")
        

