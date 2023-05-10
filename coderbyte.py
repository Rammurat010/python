
#Q1......
def FirstReverse(input):
  strParam=''
  for i in input:
    strParam=i+strParam

  # code goes here
  return strParam

input='coderbyte'
# keep this function call here 
print(FirstReverse(input)