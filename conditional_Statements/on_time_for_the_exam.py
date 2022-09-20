hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

exam_total_minutes = hour_exam * 60 + min_exam
arrival_total_minutes = hour_arrival * 60 + min_arrival
result = abs(exam_total_minutes - arrival_total_minutes)

if exam_total_minutes > arrival_total_minutes:
    if exam_total_minutes <= 30 + arrival_total_minutes:
        print("On time")
    else:
        print("Early")
elif exam_total_minutes == arrival_total_minutes:
    print("On time")
else:
    print("Late")

if exam_total_minutes - arrival_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours before the start")
elif arrival_total_minutes - exam_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours after the start")
