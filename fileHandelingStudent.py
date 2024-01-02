f = open("student.txt", "w")
f.write("joe 10 15 20 30 40\n")
f.write("bill 23 16 19 22\n")
f.write("sue 8 22 17 14 32 17 24 21 2 9 11 17\n")
f.write("grace 12 28 21 45 26 10\n")
f.write("john 14 32 25 16 89\n")
f.close()

f = open("student.txt", "r")
for lines in f:
    words = lines.split()
    if(len(words)>7):
        print(lines)
f.close()
