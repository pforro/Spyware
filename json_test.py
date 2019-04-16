import json


def main():
    jsonStr = '{"name":"Peter Cs. Forr","age":29,"univ":["SOTE","BME"]}'
    tmpDict = json.loads(jsonStr)
    print(tmpDict.get('univ',''))
   
  


if __name__ == "__main__":
    main()