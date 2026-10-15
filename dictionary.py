mark = {
    "test": 55,
    "assignment": 75,
    "project": 85,
    "final": 90
}
# print(type(mark))
# print(mark["test"])
# print(mark.keys())
# print(mark.items())
# print(mark.values())
mark.update({"test": 61, "power": 100})
print(mark)
print(mark.get("test"))
print(mark.get("power"))
