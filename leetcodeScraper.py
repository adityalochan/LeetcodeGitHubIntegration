import os
import requests

# Specify your LeetCode username
leetcode_username = "your_username"

# Specify the local Git repository folder path
repository_folder = "/path/to/local/repository"

# Specify the LeetCode solutions folder name within the repository
leetcode_folder = "LeetCode"

# Create the LeetCode folder if it doesn't exist
leetcode_path = os.path.join(repository_folder, leetcode_folder)
os.makedirs(leetcode_path, exist_ok=True)

# Fetch the LeetCode submissions
url = f"https://leetcode.com/api/submissions/{leetcode_username}"
response = requests.get(url)
submissions = response.json()["submissions_dump"]

# Process each submission
for submission in submissions:
    problem = submission["title"]
    code = submission["code"]

    # Create a file for each submission
    file_name = f"{problem}.txt"
    file_path = os.path.join(leetcode_path, file_name)

    # Write the code to the file
    with open(file_path, "w") as file:
        file.write(code)

# Print a success message
print("LeetCode submissions downloaded and saved to the local repository.")
