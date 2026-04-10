student = {"Name": "Sumeet", "Age": 20, "City": "Mumbai"}
print("Original Dictionary:", student)
student["Age"] = 21
student["City"] = "Pune"
print("After Update:", student)
print("After Removing city:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length:", len(student))
student.pop("City")
print("After Removing city:", student)