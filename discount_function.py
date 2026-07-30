#Implemented an apply_discount function in Python with input validation and discount calculation.

#Features:
#Validates that price and discount are numeric values.
#Ensures price is greater than 0.
#Ensures discount is between 0 and 100.
#Calculates and returns the final price after applying the discount.
#Practices Python functions, parameters, return statements, and conditional logic.

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'

    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'

    if price <= 0:
        return 'The price should be greater than 0'

    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price