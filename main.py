import time
a = 0
n = float(input("Please enter the amount of satoshis you want to mine(Remember 1btc is 100,000,000 satoshis)\n"))
while True:
  import random
  r = int(random.randrange(1,5))
  print("Mining...")
  time.sleep(r)
  a = a + 1000000
  print("Mined", a,"Satoshis")
  if a < n: 
    continue
  if a == n:
    u = input("Please enter wallet address\n")
    print("Thank you for mining bitcoin your bitcoin will be deposited soon, please donate to the creator 12TNSDXceVZdksAiYLMfdi15t2Z5N2NwWt")
    exit()