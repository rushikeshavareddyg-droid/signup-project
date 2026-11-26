def signup(username, password):
    if not username:
        return "Username is required"

    if len(password) < 6:
        return "Password must contain at least 6 characters"

    return "Signup successful"


print(signup("rushi", "123456"))
print(signup("", "123456"))
print(signup("rushi", "123"))