#Q2) Suppose that the tuition for a university is $10,000 this year and increases 5% every year. In 
#one year, the tuition will be $10,500. Write a program that computes the tuition in ten years 
#and the total cost of four years’ worth of tuition after the tenth year.

#given
tuition = 10000
increased_value = 0.05 #--> 5%

for i in range (1,11): #--> Write 11 to take 10
    tuition_in_ten_years = tuition * (1 + increased_value) #will give the tuition for each year
    total_cost = tuition_in_ten_years * 4
print("the tuition in ten years is: ", tuition_in_ten_years)
print("the total cost of four years is: ", total_cost)

#Q3 

raw = 8
x = 1
for i in range (1,raw +1):
    for j in range (1, raw-i, 1):
        print(" ", end=" ")
    for k in range(1,i+1):
        x=2**(k-1)
        print(x, end=" ")
    for m in range(i-1,0,-1):
        x=2**(m-1)
        print(x, end=" ")
    print()
