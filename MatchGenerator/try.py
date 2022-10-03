def collectStrings(obj):
    lst = []
    for key in obj:
        if type(obj[key]) is str:
            lst += [obj[key]]
            # return lst
        else:
            if type(obj[key]) is dict:
                return lst + collectStrings(obj[key])
    return lst

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
print(collectStrings(obj)) # ['foo', 'bar', 'baz']
