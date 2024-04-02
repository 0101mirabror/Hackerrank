def CodelandUsernameValidation(strParam):

  # code goes here
  return True if len(strParam) > 4 and len(strParam) < 25 and strParam[-1] != "_" and strParam[0].isalpha() and strParam.replace('_', '').isalnum() else False
# keep this function call here 
print(CodelandUsernameValidation(input()))