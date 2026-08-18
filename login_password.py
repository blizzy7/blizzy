# Receive the user's email and password.
# Look up the stored password for that email.
# If the email is not found, return "Account does not exist."
# Compare the entered password with the stored password.
# If the passwords match, return "Login successful."
# If the passwords do not match, return "Incorrect password."

def login(email, password):
    account = {
        user@gmail.com: "me2026",
        admin@gmail: "admin2025"
    }
    if email not in account:
        return "Account does not exist."
    stored_password = account[gmail]
    if password == stored_password:
        return "login successful."
    else:
        return "Incorrect password."