file = open('fileprocessor.input', 'r')
lines = file.readlines()
file.close()

users_data = []

for line in lines:
    if not line.startswith('#'):
        data = line.strip().split(':')
        users_data.append(data)

print("Printing out User Data:\n")

for user_data in users_data:
    username = user_data[0]
    password = user_data[1]
    userid = user_data[2]
    groupid = user_data[3]
    print("The user " + username + " has a password of " + password + " and has userid " + userid + " and groupid " + groupid)

print("\nUser4 is skipped because it starts with a hashtag (is commented out)")
print("\nEnd of User Data")
