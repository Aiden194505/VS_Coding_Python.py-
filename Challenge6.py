import turtle as trtl

print("There is Zombie aploclypse outbrack! You lock your self in the Computer Scince room to stay safe. You are sent a dacumant of how many people are afected Right Now and how many people each zombie affects each day.")

ii=input("How many people are affected today")
aa=input("How many people each Zombie affects each day")
dd=input("Each day more and mare people are affected. You wander how many people will be affed in [Number] of days?")


zpd = reslot = int(ii) * int(aa) 
zd = reslot = int(zpd) * int(dd)

print("In", dd, "days there will be", zd, "zombies")


wn = trtl.Screen