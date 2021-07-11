email = input("What is your email address?: ")

email=email.strip()

a=email.index('@')

# Slice out the user name
user_name = email[:a]

# Slice the domain name
domain_name = email[a+1:]

# Format message
output = "your username is '{}' and domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)
