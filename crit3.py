print("Part 1");
print("This program calculates the total amount of a meal purchased at a restaurant;" +
      "the charge for the food, 18 percent tip, and 7 percent sales tax.");
print("");
mealTotal = float(input("Enter the total amount of a meal purchased at a restaurant:"));
percentTip = mealTotal*.18;
salesTax = mealTotal*.07;

print("Meal cost:"+str(mealTotal)+", percent tip: " +str(percentTip)+", sales tax:"+ str(salesTax)+", Total price: " +str(mealTotal+percentTip+salesTax));
print("");
print("Part 2");
curentTime = int(input("Enter the time in hours only(24 hour):"));
alarm = int(input("Enter the amount of hours for alarm to go off from the current time:"));
total = curentTime + alarm;
  
while(total - 24)>= 0:
    total = total -24;

print("The alarm will go off at " +str(total));
  
