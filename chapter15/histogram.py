import matplotlib.pyplot as plt

#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards

fitness_test=[2901,1760,3000,2824,3235,2050,2265,2500,2400,2625,3550,1850,1890,3200,2900,2975,3000,2220,2250]
print(sorted(fitness_test))
plt.hist(fitness_test, bins=6, color='darkblue')
plt.ylabel("Number of students (19 tested)")
plt.xlabel("Distance (Yards)")
plt.suptitle("12 Minute Distance Test", color='gray')


plt.show()