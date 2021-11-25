
marks = int(input("Enter your marks: "))
print(type(marks),marks)

if marks < 35:
    print("Fail")
elif marks >=35 and marks<45:
    print("Pass class")
elif marks >=45 and marks<60:
    print("Second class")
elif marks >=60 and marks<85:
    print("First class")
elif marks >=85 and marks<=100:
    print("Top class")
else:
    print("Enter correct marks")