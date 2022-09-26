
def nestedEvenSum(obj, sum=0):
  for key in obj:
    if type(obj[key]) is dict:
      nestedEvenSum(obj[key], sum)
    else:
      if type(obj[key]) is int and obj[key]%2 == 0:
        sum += obj[key]
        print(f"{key} + {sum}")
  return sum

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}
print(nestedEvenSum(obj2))