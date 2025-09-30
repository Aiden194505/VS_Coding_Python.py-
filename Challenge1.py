import turtle as trtl

print("The following qustions will ask your birth year, month, and day")

By=input("birth year ")
Bm=input("birth month number ")
Bd=input("birth day ")

Ay = result = 2024 - int(By)
Am = result = int(Bm) - 1
Ad = result = 30 - int(Bd)

# problem A

Ya = result = int(Ay) * 365
Ma = result = int(Am) * 30

print("You have been alive for")

aa = result = int(Ya) + int(Ma) + int(Ad) + 29
print("days    ", aa)

bb = result = int(By) -2024 / -10
print("decades ", bb)

cc = result = int(aa) / 7
print("weeks   ", cc)

dd = result = int(aa) * 24 * 60 + 840
print("minutes ", dd)



wn = trtl.Screen
#wn.mainloop()