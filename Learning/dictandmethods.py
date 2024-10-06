# dict1 = {}
# b = set()
# print(dict1, type(dict1))
# print(b, type(b))

dict1 = {"good": "Something pleasant", "fetch": "to bring", "1": "The number 1"}
print(dict1["good"])

marks = {"Isha": 100, "Jytoi": 99, "Rahul": 98}
print(marks["Isha"])

marks["Ishita"] = 97
print(marks)

print(marks.get("Ishita Kulkarni"))
print(marks.get("Ishita"))
# .get helps with errors

print(marks.keys())
print(marks.values())
print(marks.items())
