# update_leaderboard.py
import requests

# Fetch data from the GitHub API
# Calculate the leaderboard data
leaderboard_data = [
    {"rank": 1, "contributor": "user1", "merged_prs": 20},
    {"rank": 2, "contributor": "user2", "merged_prs": 15},
    # Add more contributors and data
]

# Generate the Markdown content for the leaderboard
markdown_content = """
# GitHub Leaderboard

| Rank | Contributor | Merged PRs |
| ---- | ----------- | ---------- |
{}
""".format("\n".join(
    f"| {entry['rank']} | @{entry['contributor']} | {entry['merged_prs']} |"
    for entry in leaderboard_data
))

# Write the Markdown content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(markdown_content)
