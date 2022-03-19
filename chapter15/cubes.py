import matplotlib.pyplot as plt


inputVal=[1, 2, 3, 4, 5]

# plot 1
cubed=[]
for num in inputVal:
    cubed.append(num**3) 
ax1 = plt.subplot(1,2,1)
ax1 = plt.plot(inputVal,cubed, marker='*', lw='2.5', ls='--', c='red')
plt.grid()
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")

# plot #2
pow=[]
for num in inputVal:
    pow.append(num**2) 
ax2 = plt.subplot(1,2,2)
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.style.use('seaborn-paper')
ax2 = plt.plot(inputVal, pow, c="darkorange",lw="2")
plt.title("Numbers Raised", color = 'green')
plt.grid(color='lemonchiffon')

plt.suptitle("Fun with Numbers",c="red",fontfamily="Comic Sans MS", fontsize="18")
plt.subplots_adjust(wspace=.4, top=.8)
plt.show()