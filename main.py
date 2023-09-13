import streamlit as st


st.write("### Can you identify the sequence ?")

st.write("""
We've chosen a rule that some sequences of three numbers obey — and some do not. Your job is to guess what the rule is.

We'll start by telling you that the sequence 2, 4, 8 obeys the rule:

Now it's your turn. 
Enter a number sequence in the boxes below, and we’ll tell you whether it satisfies the rule or not. You can test as many sequences as you want.
    """)

inputs = []
pos = ['1st','2nd','3rd']
cols = st.columns(3)
for p,c in zip(pos,cols):
    with c:
        inputs.append(st.text_input("", key=f"n{p}", placeholder=f"Enter {p} number"))

def safe_parse_int(s):
    if not s.strip():
        return "Empty"
    s = s.strip()
    try:
        value = float(s)
    except ValueError:
        return "Not a number"
    
    try:
        value = float(value)
        return value
    except ValueError:
        return value


    
    
if st.button("Test sequence", type="primary"):
    message = ""
    values = []
    for p,i in zip(pos,inputs):
        value = safe_parse_int(i)
        if value=="Empty":
            st.write("You need to enter three numbers, one per box, before clicking on :red['Test sequence'].")
            break
        if value=="Not a number":
            st.markdown(f"""Sorry, the {p} input is not a number.  
You need to enter three numbers, one per box, before clicking on :red['Test sequence'].""")
            break
        values.append(value)
    else:
        # now check if match rule
        n1, n2, n3 = values
        if n1<n2<n3:
            st.info("Entered sequence does match rule. ")
        else:
            st.info("Entered sequence does NOT match rule. ")

