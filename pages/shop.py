import streamlit as st

# Sample product data
products = [
    {"id": 1, "name": "Life shirt", "price": 17.99, "description": "A high-performance laptop with the latest features."},
    {"id": 2, "name": "Signed Life shirt. limited edition", "price": 49.99, "description": "This LIFE Shirt isn't just a LIFE Shirt... This is the LIMITED EDITION LIFE SHIRT WITH MR A SIGNATURE!!! (Long name). This rare shirt was found in the darkest places of the Autorregulation-verse. It is a gift to the champion, the number 1 Mr A follower. We only found 5 of them... Buy them before its too late!!!"},
]

# Initialize session state for the shopping cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Function to add a product to the cart
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        st.session_state.cart.append(product)
        st.success(f"{product['name']} added to cart!")

# Function to remove a product from the cart
def remove_from_cart(product_id):
    st.session_state.cart = [p for p in st.session_state.cart if p["id"] != product_id]
    st.success("Item removed from cart!")

# Shopping page layout
st.title("Shopping Page")

# Display available products
st.header("Available Products")
for product in products:
    st.write(f"**{product['name']}**")
    st.write(f"Price: ${product['price']:.2f}")
    st.write(f"Description: {product['description']}")
    if st.button(f"Add {product['name']} to Cart", key=f"add_{product['id']}"):
        add_to_cart(product['id'])
    st.write("---")

# Display the shopping cart
st.header("Your Shopping Cart")
if st.session_state.cart:
    for product in st.session_state.cart:
        st.write(f"**{product['name']}**")
        st.write(f"Price: ${product['price']:.2f}")
        if st.button(f"Remove {product['name']} from Cart", key=f"remove_{product['id']}"):
            remove_from_cart(product['id'])
        st.write("---")
    st.write(f"Total: ${sum(item['price'] for item in st.session_state.cart):.2f}")
else:
    st.write("Your cart is empty.")
