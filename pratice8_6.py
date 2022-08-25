for num in range(1, 51) :
    report_file = open("{0}주차.txt".format(num), "w", encoding = "utf8")
    print("- X 주차 주간보고 -", file = report_file)
    print("부서 : ", file = report_file)
    print("이름 : ", file = report_file)
    print("업무 요약 : ", file = report_file)
    report_file.close()
