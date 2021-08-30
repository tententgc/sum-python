try:
    a = input("ป้อนหมายเลขของคุณ : ") 

    if len(a) != 6:
        print(x)
    y = int(a)

    r1 = "046750"
    r2 = ("666", "421")
    r3 = ("355", "160")
    r4 = "23"

    sum_ans = 0
    if a == r1:
        sum_ans += 6000000
    if a[-2:] == r4:
        sum_ans += 2000

    for i in range(2):
        if a[:3] == r2[i]:
            sum_ans += 4000
        if a[-3:] == r3[i]:
            sum_ans += 4000


    if sum_ans >= 6000000:
        print("ยินดีด้วย! คุณได้รับรางวัลที่ 1")
    if sum_ans > 0:
        print("คุณได้รับรางวัล " + str(sum_ans), "บาท")
    else:
        print("เสียใจด้วย คุณไม่ถูกรางวัล")


except:
    print("หมายเลขไม่ถูกต้อง")
