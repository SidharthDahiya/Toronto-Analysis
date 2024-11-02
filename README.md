# Toronto GitHub Users Analysis

- **Data Collection**: This project gathered information on GitHub users based in Toronto with over 100 followers, including user profiles and repositories, using the GitHub REST API.
- **Insightful Findings**: JavaScript and Python are widely used among Toronto's developers, with many contributing to open-source projects that emphasize web development and data science.
- **Actionable Advice**: Developers should consider publishing detailed documentation and tutorials in their repositories to attract more community engagement and stars.

## Project Overview

This project uses the GitHub API to scrape and analyze data on Toronto-based GitHub users with over 100 followers. Data on users and their repositories were collected, cleaned, and analyzed to gain insights into popular programming languages, active contributors, and user affiliations.

### Data Files

- **users.csv**: Contains detailed profile information for each user, including their username, name, company affiliation, bio, and other profile details.
- **repositories.csv**: Lists up to 500 of each user's repositories, with details such as the repository name, creation date, primary language, star count, and license type.

### Methodology

1. **Data Extraction**: Using the GitHub API, we searched for users in Toronto with more than 100 followers. For each user, up to 500 of their most recent public repositories were retrieved.
2. **Data Cleaning**: Company names were standardized by removing leading `@` symbols, trimming whitespace, and converting names to uppercase. Empty fields were left as blank strings for consistency.
3. **Data Analysis**: Analysis of the CSV data provided insights into the tech ecosystem in Toronto, examining trends in programming languages, repository stars, and collaboration practices.

### Key Findings

- **High Engagement in Web Development**: A significant portion of users favored JavaScript, particularly for front-end and full-stack projects.
- **Prevalence of MIT License**: Among open-source repositories, the MIT license is common, reflecting a preference for permissive licensing.
- **Company Affiliations**: Many top users work at prominent companies or are engaged in independent tech initiatives, highlighting Toronto as a tech hub.

### Analysis Results

Using statistical analysis, we explored questions such as:
- The popularity of different programming languages among Toronto-based developers.
- Patterns in repository creation dates relative to user join dates.
- Relationships between user followers, repository stars, and open-source contributions.

### Repository Structure

```plaintext
|-- users.csv               # User profile data from GitHub
|-- repositories.csv        # Repository data from GitHub users
|-- README.md               # Project overview and key insights
|-- scraper.py              # Script to scrape data from GitHub API
```
