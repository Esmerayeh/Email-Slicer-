#email slicer
email = input("Enter Your Email: ").strip()
x=email.split(",")
for i in range (len(x)):  
    v=x[i]
    username = v[:email.index('@')]
    do = v[email.index('@') + 1:]
    domain= do.upper()
    print(f"Your username is {username} & domain is {domain}")