import streamlit as st

# Sample product data
products = [
    {"id": 1, "name": "Life shirt", "price": 17.99, "description": "This is the classical life shirt. It looks simple but its backstory is complex. This word \"LIFE\" means a lot to our community, it means that you have to fight for your dreams even if life gets in your way, it means never stop trying. It means... LIFE."},
    {"id": 2, "name": "Signed Life shirt. Limited edition", "price": 49.99, "description": "This LIFE Shirt isn't just a LIFE Shirt... This is the LIMITED EDITION LIFE SHIRT WITH MR A SIGNATURE!!! (Long name). This rare shirt was found in the darkest places of the Autorregulation-verse. It is a gift to the champion, the number 1 Mr A follower. We only found 5 of them... Buy them before its too late!!!"},
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

# Custom CSS for styling buttons

custom_css = """
<style>
    /* Hide the sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    /* Adjust main content area */
    .main > div {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Style buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Shopping page layout
st.title("Shopping Page")

# Display available products
st.header("Available Products")
for product in products:
    st.write(f"**{product['name']}**")
    st.write(f"Price: €{product['price']:.2f}")
    st.write(f"Description: {product['description']}")
    if st.button(f"Add {product['name']} to Cart", key=f"add_{product['id']}"):
        add_to_cart(product['id'])
    st.write("---")

# Display the shopping cart
st.header("Your Shopping Cart")
if st.session_state.cart:
    for product in st.session_state.cart:
        st.write(f"**{product['name']}**")
        st.write(f"Price: €{product['price']:.2f}")
        if st.button(f"Remove {product['name']} from Cart", key=f"remove_{product['id']}"):
            remove_from_cart(product['id'])
        st.write("---")
    st.write(f"Total: €{sum(item['price'] for item in st.session_state.cart):.2f}")
    """
    # PayPal integration
    st.write("---")
    st.write("### Proceed to Payment")
    paypal_button = f'''
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
        <input type="hidden" name="cmd" value="_xclick">
        <input type="hidden" name="business" value="your-paypal-email@example.com">
        <input type="hidden" name="lc" value="US">
        <input type="hidden" name="item_name" value="Shopping Cart">
        <input type="hidden" name="amount" value="{total:.2f}">
        <input type="hidden" name="currency_code" value="EUR">
        <input type="hidden" name="button_subtype" value="products">
        <input type="hidden" name="no_note" value="0">
        <input type="hidden" name="cn" value="Add special instructions to the seller">
        <input type="hidden" name="no_shipping" value="2">
        <input type="hidden" name="rm" value="1">
        <input type="hidden" name="return" value="your-return-url.com">
        <input type="hidden" name="cancel_return" value="your-cancel-url.com">
        <input type="hidden" name="bn" value="PP-BuyNowBF:btn_buynowCC_LG.gif:NonHosted">
        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
        <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>
    '''
    st.markdown(paypal_button, unsafe_allow_html=True)"""
else:
    st.write("Your cart is empty.")

button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([1, 2, 3])
    with col1:
        ModelIsClicked=st.button("About us",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/about_us.py")
    with col2:
        ModelIsClicked=st.button("Login",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/login.py")
    with col3:
        ModelIsClicked=st.button("Main Page", use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/main_page.py")
