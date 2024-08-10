#POSITIVE SCENARIO

#TEST CASE 001
#TITLE: Add a single item to the cart and verify.

#PREREQUISITE - user logged in

#STEPS
#1. Navigate to the product listing page.
#2.Select a product and click "Add to Cart."
#3. Navigate to the cart page.
#4. Verify that the selected product is displayed in the cart.
#5. Check the quantity and price details.
#6. Expected Result: The selected product should be visible in the cart with the correct quantity and price.


#CHECKOUT
# Test Case 002

# TITLE: Checkout with valid payment information.

# PREREQUISITE- Items are added to the cart, and the user is logged in

# STEPS
# 1. Navigate to the cart page.
# 2. Click on "Checkout."
# 3. Enter valid shipping and payment details.
# 4. Confirm the order.
# Expected Result:
# 5 The order should be successfully placed, and a confirmation message should be displayed.




# NEGATIVE SCENARIO

# TESTCASE 003
# Title: Attempt to add an out-of-stock item to the cart.
# PREREQUISITE: User is logged in, AND a product not in stcok is listed.

# Steps:
# 1. Select product that is not in stock
# 2. Attempt to add it to the cart.

# Expected Result:
# 3. The user should see an error message indicating that the product is out of stock and cannot be added to the cart

