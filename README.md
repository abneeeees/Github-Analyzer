# GitHub Analyzer
A Python web scraping tool that extracts comprehensive statistics from GitHub user profiles using Selenium WebDriver.

## Features

- 📊 **Basic Profile Info**: Extract name and username from GitHub profiles
- 🔗 **Social Links**: Scrape social media links from user profiles  
- 📈 **Repository Analysis**: Get total repositories, stars, and commits
- 💻 **Language Detection**: Find programming languages used across repositories
- 👥 **Social Stats**: Followers, following count and ratio calculation
- 🤖 **Headless Browsing**: Automated Chrome browser in headless mode

## Requirements

- Python 3.6+
- Chrome browser installed
- ChromeDriver (managed by selenium)

## Installation

1. **Install required packages:**
   ```bash
   pip install selenium
   ```

2. **Ensure Chrome is installed** on your system

## Usage

Run the script:
```bash
python github_scraper.py
```

Enter the GitHub username when prompted:
```
PASTE YOUR ACCOUNT'S URL : username
```

## Code Structure

The script contains three main classes:

### `BasicInf0`
Handles basic profile information extraction.

**Methods:**
- `name()` - Extracts full name and username
- `socials()` - Gets social media links from profile
- `repo()` - Collects all repository URLs

### `RepoInsider(BasicInf0)` 
Inherits from BasicInf0 and analyzes repository details.

**Methods:**
- `no_of_stars()` - Counts stars for current repository
- `no_of_commits()` - Extracts commit count using regex
- `no_of_languages()` - Identifies programming languages
- `all_repo_insider()` - Iterates through all repos for analysis

### `Personal`
Handles follower/following statistics and ratios.

**Methods:**
- `followers_and_follwing()` - Extracts follower/following counts
- `no_of_repos()` - Displays total repository count
- `follower_to_follwing_ratio()` - Calculates and prints ratio

## What It Scrapes

| Data Type | CSS Selector Used | Description |
|-----------|-------------------|-------------|
| **Name** | `span.p-name.vcard-fullname.d-block.overflow-hidden` | Full name |
| **Username** | `span.p-nickname.vcard-username.d-block` | GitHub username |
| **Social Links** | `li.vcard-detail.pt-1 > a` | Social media URLs |
| **Repository Names** | `h3.wb-break-all > a` | Repo names and links |
| **Repository Descriptions** | `div.col-10.col-lg-9.d-inline-block > div:nth-child(2)` | Repo descriptions |
| **Stars** | `a.Link.Link--muted > strong` | Star count per repo |
| **Commits** | `span.fgColor-default` | Commit count per repo |
| **Languages** | `span.color-fg-default.text-bold.mr-1` | Programming languages |
| **Social Stats** | `div.mb-3 > a > span` | Followers/following |

## Sample Output

```
John Doe @johndoe
Twitter : https://twitter.com/johndoe
LinkedIn : https://linkedin.com/in/johndoe
{'Python', 'JavaScript', 'HTML', 'CSS', 'Java'}
Total stars : 150
Total commits : 1250
5
1.75
```

## Code Flow

1. **Initialize**: Creates headless Chrome browser instance
2. **Get URL**: Prompts user for GitHub username
3. **Basic Info**: Scrapes name, username, and social links
4. **Repository Collection**: Navigates to repositories tab and collects all repo URLs
5. **Repository Analysis**: 
   - Visits each repository individually
   - Extracts stars, commits, and languages
   - Accumulates totals across all repositories
6. **Social Analysis**: Calculates follower-to-following ratio
7. **Display Results**: Prints all collected statistics

## Key Features of Original Code

### Selenium Configuration
```python
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
```

### Data Collection Pattern
```python
# Collects repository URLs for later analysis
self.to_store_repos.append(ele1.get_attribute('href'))
```

### Regex Usage for Commits
```python
# Extracts numbers from commit text
numbers = re.findall(r'\d+', commits.text)
commit_list = [int(nums) for nums in numbers]
```

### Set Usage for Languages
```python
# Uses set to avoid duplicate languages
self.total_lang = set()
self.total_lang.add(a.text)
```

## Limitations

- **No Error Handling**: Original code lacks try-catch blocks
- **Fixed Selectors**: CSS selectors may break if GitHub updates their layout
- **No Rate Limiting**: May overwhelm GitHub's servers with rapid requests
- **Input Handling**: Limited validation of user input
- **Resource Management**: Browser instance not properly closed

## Potential Issues

1. **Element Not Found**: CSS selectors may fail on different profile layouts
2. **Dynamic Content**: Some elements may not load immediately
3. **Private Repositories**: Cannot access private repo data
4. **Rate Limiting**: GitHub may block excessive requests

## Usage Notes

- The script navigates between different GitHub pages automatically
- Uses headless Chrome to avoid opening browser windows
- Processes all repositories sequentially which may take time for users with many repos
- Accumulates statistics across all public repositories

## Legal Considerations

- Only accesses publicly available GitHub data
- Respects GitHub's public profile information
- Use responsibly and respect GitHub's terms of service
- Consider using GitHub's official API for production use

## Future Improvements

- Add error handling and exception management
- Implement delays between requests
- Add input validation
- Proper browser cleanup
- Export results to files
- Progress indicators for long operations

## Dependencies

```
selenium
re (built-in)
```

Make sure ChromeDriver is compatible with your installed Chrome version.
