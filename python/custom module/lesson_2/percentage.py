print("Enter Marks Obtained in 5 Subjects: ")
Maths = int(input("Maths: "))
English = int(input("English: "))
Science = int(input("Science: "))
History = int(input("History: "))
Geography = int(input("Geography: "))

sum = Maths + English + Science + History + Geography
print("total:", sum)

percentage = int((sum / 500) * 100)
print(end = "percentage marks :")
print(percentage)