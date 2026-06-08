# ==========================================
# REST API & JSON PROCESSING IN PYTHON
# BASIC TO ADVANCED
# ==========================================

import requests

# ------------------------------------------
# 1. SIMPLE API REQUEST
# ------------------------------------------

print("----- SIMPLE API REQUEST -----")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

# ------------------------------------------
# 2. CONVERT JSON TO PYTHON OBJECT
# ------------------------------------------

print("\n----- JSON DATA -----")

users = response.json()

print("Total Users:", len(users))

# Display first user
print("\nFirst User Details")
print("Name:", users[0]["name"])
print("Email:", users[0]["email"])

# ------------------------------------------
# 3. DISPLAY ALL USERS
# ------------------------------------------

print("\n----- ALL USERS -----")

for user in users:
    print(
        f"ID: {user['id']}, "
        f"Name: {user['name']}, "
        f"Email: {user['email']}"
    )

# ------------------------------------------
# 4. DISPLAY SPECIFIC FIELDS
# ------------------------------------------

print("\n----- USER CONTACTS -----")

for user in users:
    print(
        f"{user['name']} - "
        f"{user['phone']}"
    )

# ------------------------------------------
# 5. SEARCH USER BY ID
# ------------------------------------------

print("\n----- SEARCH USER -----")

search_id = int(input("Enter User ID (1-10): "))

for user in users:

    if user["id"] == search_id:

        print("\nUser Found")
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])

        break

else:
    print("User Not Found")

# ------------------------------------------
# 6. EXCEPTION HANDLING
# ------------------------------------------

print("\n----- EXCEPTION HANDLING -----")

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    posts = response.json()

    print("Total Posts:", len(posts))

except requests.exceptions.RequestException as e:

    print("API Error:", e)

# ------------------------------------------
# 7. ADVANCED DATA PROCESSING
# ------------------------------------------

print("\n----- ADVANCED PROCESSING -----")

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

posts = response.json()

# First 5 posts
for post in posts[:5]:

    print("\nPost ID:", post["id"])
    print("Title:", post["title"])

# ------------------------------------------
# 8. FILTER DATA
# ------------------------------------------

print("\n----- FILTER POSTS -----")

user_posts = [
    post
    for post in posts
    if post["userId"] == 1
]

print("Posts by User 1:", len(user_posts))

for post in user_posts[:3]:
    print(post["title"])

# ------------------------------------------
# 9. COUNT DATA
# ------------------------------------------

print("\n----- DATA ANALYSIS -----")

total_users = len(users)
total_posts = len(posts)

print("Total Users:", total_users)
print("Total Posts:", total_posts)

# ------------------------------------------
# 10. ADVANCED REPORT
# ------------------------------------------

print("\n----- USER REPORT -----")

for user in users:

    print("=" * 40)

    print("Name :", user["name"])
    print("Email:", user["email"])
    print("City :", user["address"]["city"])
    print("Company:", user["company"]["name"])

print("\nProgram Completed Successfully!")