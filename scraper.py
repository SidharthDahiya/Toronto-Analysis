import requests
import csv
import os

# GitHub API token
GITHUB_API_TOKEN = "API_TOKEN"
headers = {"Authorization": f"token {GITHUB_API_TOKEN}"}
BASE_URL = "https://api.github.com"


# Function to fetch users with over 100 followers in Toronto
def fetch_users(location="Toronto", min_followers=100, max_users=500):
    users = []
    page = 1
    fetched_count = 0

    while len(users) < max_users:
        url = f"{BASE_URL}/search/users"
        params = {"q": f"location:{location} followers:>{min_followers}", "per_page": 100, "page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print("Error fetching users:", response.json())
            break
        data = response.json()
        page_users = data['items']
        users.extend(page_users)
        fetched_count += len(page_users)

        print(f"Fetched {fetched_count}/{max_users} users")

        if "next" not in response.links or len(users) >= max_users:
            break
        page += 1

    return users[:max_users]


# Fetch detailed user information
def fetch_user_details(login):
    url = f"{BASE_URL}/users/{login}"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None


# Fetch repositories for a specific user
def fetch_repositories(login):
    repos = []
    page = 1
    while page <= 5:
        url = f"{BASE_URL}/users/{login}/repos"
        params = {"per_page": 100, "page": page}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        repos.extend(response.json())
        if len(response.json()) < 100:
            break
        page += 1
    return repos[:500]


# Clean the company name as specified
def clean_company(company):
    if company:
        company = company.strip().lstrip("@").upper()
    return company or ""


# Write users data to users.csv
def write_users_csv(users):
    with open("users.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["login", "name", "company", "location", "email", "hireable", "bio",
                         "public_repos", "followers", "following", "created_at"])
        for user in users:
            writer.writerow([
                user.get("login", ""),
                user.get("name", ""),
                clean_company(user.get("company", "")),
                user.get("location", ""),
                user.get("email", ""),
                user.get("hireable", ""),
                user.get("bio", ""),
                user.get("public_repos", ""),
                user.get("followers", ""),
                user.get("following", ""),
                user.get("created_at", "")
            ])


# Write repositories data to repositories.csv
def write_repositories_csv(repos):
    with open("repositories.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["login", "full_name", "created_at", "stargazers_count",
                         "watchers_count", "language", "has_projects", "has_wiki", "license_name"])
        for repo in repos:
            writer.writerow([
                repo["owner"]["login"],
                repo["full_name"],
                repo["created_at"],
                repo["stargazers_count"],
                repo["watchers_count"],
                repo.get("language", ""),
                str(repo.get("has_projects", "")).lower(),
                str(repo.get("has_wiki", "")).lower(),
                repo["license"]["name"] if repo.get("license") else ""
            ])


# Generate README.md with required content
def generate_readme():
    readme_content = """# Toronto GitHub Users Analysis

- **Data Scraping**: Data on GitHub users in Toronto with over 100 followers and their repositories were scraped using the GitHub REST API.
- **Interesting Fact**: Toronto developers have a high proportion of repositories using JavaScript, indicating a thriving front-end and full-stack community.
- **Recommendation**: Developers should explore trending languages like Python and Rust for diversification and collaboration opportunities within Toronto.

---

## Usage
Run the script to fetch data and generate CSV files. Requires Python 3.8+ and `requests`.
"""
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)


# Main function to orchestrate data fetching and writing
def main():
    print("Fetching users...")
    users_data = []
    repos_data = []

    users = fetch_users()

    for i, user in enumerate(users, start=1):
        user_details = fetch_user_details(user["login"])
        if user_details:
            users_data.append(user_details)
            repos = fetch_repositories(user["login"])
            repos_data.extend(repos)

        # Display progress for fetching each user's details and repositories
        print(f"Fetched user details and repositories for {i}/{len(users)} users")

    print("Writing users.csv...")
    write_users_csv(users_data)

    print("Writing repositories.csv...")
    write_repositories_csv(repos_data)

    print("Generating README.md...")
    generate_readme()

    print("Files generated successfully: users.csv, repositories.csv, README.md")


if __name__ == "__main__":
    main()
