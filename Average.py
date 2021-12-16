# # Average of two numbers
# num1 = int(input("Enter num 1 : "))
# num2 = int(input("Enter num 2 : "))

# avg = (num1 + num2) / 2
# print(f"Average of two numbers is : {avg}")


# #Average of numbers in a list

# ls = [10,20,30,40,50]
# sum = 0
# for l in ls:
#     sum = l + sum
# avg = sum / ls.count
# print (f"Sum : {sum}")

#Pass Fail based on marks secured

ls = [70, 50, 86, 50, 90]
sum = 0
avg = 0
for l in ls:
    sum = sum + l
avg = sum / ls.count
print (f"Avg : {avg}")
if (avg > 45):
    print (f"Student has passed with an average of : {avg}")
else:
    print (f"Student has failed with an average of : {avg}")
    