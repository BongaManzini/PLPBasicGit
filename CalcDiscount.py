def calculate_discount(price, discount_percent):

  # Calculate the final price after applying the discount. If the discount is 20% or higher, apply the discount. Otherwise, return the original price.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input.")
