import math

print("みんなで割り勘")
bill = int(input("お会計はいくらですか？"))
people = int(input("何人で支払いますか？"))
per = bill / people
print(math.ceil(per))
