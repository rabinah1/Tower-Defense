file = "file_4.txt"
sql = "koe.sql"
mapfile = open(file, "r")
sqlfile = open(sql, "w")
c = " "
i = 1
j = 1
temp = 0

while i <= 10:
    j = 1
    while j < 1:
        mapfile.readline()
        j += 1
    while True:
        c = mapfile.read(1)
        if c == "\n":
            break
        c = mapfile.read(int(c))
        health = int(c)
        c = mapfile.read(1)
        c = mapfile.read(int(c))
        price = int(c)
        c = mapfile.read(1)
        color = c
        c = mapfile.read(1)
        speed = int(c)
        c = mapfile.read(1)
        resistant = int(c)
        c = mapfile.read(1)

        if color == "B":
            color = "black"
        elif color == "r":
            color = "red"
        elif color == "b":
            color = "blue"
        elif color == "y":
            color = "yellow"
        elif color == "g":
            color = "gray"

        if speed == 1:
            speed = "slow"
        elif speed == 2:
            speed = "fast"

        if resistant == 1:
            resistant = "red"
        elif resistant == 2:
            resistant = "blue"
        elif resistant == 3:
            resistant = "yellow"
        elif resistant == 4:
            resistant = "gray"
        elif resistant == 5:
            resistant = "none"

        text = ("('" + str(health) + "','" + str(price) + "','" + color + "','" + str(speed) +
                "','" + resistant + "','" + str(i) + "'),\n")
        sqlfile.write(text)
        if c == "%":
            c = mapfile.read(1)
            i = i + 1
            break
        elif c == "!":
            temp = 1
            break
    if temp == 1:
        break
mapfile.close()
sqlfile.close()
