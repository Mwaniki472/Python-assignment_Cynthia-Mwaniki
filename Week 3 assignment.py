#Function to calculate the final price after discount.
def calculate_final_price(original_price, discount_percentage):
    """
    Calculate the final price after applying a discount if it is 20% or higher
    otherwise return the original price.
    """
    if discount_percentage >= 20:
        #calculate the discount amount.
        discount_amount = (discount_percentage / 100) * original_price
        # subtract the discount amount from the original price.
        final_price = original_price - discount_amount
        return final_price
    else:
        return original_price
    
    #Get user input.
    price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    # Calculate the final price
    final_price = calculate_final_price(price, discount)
    if discount >= 20:
        print(f"After applying a {discount_percentage}% discount, the final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied, the final price is: ${final_price:.2f}")