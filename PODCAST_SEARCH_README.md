# Podcast Search Tool 🎙️

A comprehensive Python-based podcast search and discovery tool that leverages the iTunes API to help you find, filter, and organize podcast information.

## Features

✨ **Key Capabilities:**
- 🔍 Search podcasts by keywords, topics, or names
- 📂 Browse podcasts by category (Business, Technology, Education, etc.)
- 🎯 Filter results by episode count, genre, and explicit content
- 🌍 Search across different countries and regions
- 📊 Export results to CSV or JSON formats
- 📝 Detailed podcast information including feed URLs, artwork, and descriptions
- 💻 Both CLI and programmatic usage supported

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone this repository or download the files:
```bash
git clone <repository-url>
cd ai-productivity-planner
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface (CLI)

#### Basic Search
```bash
# Search for podcasts about a specific topic
python podcast_search.py --query "artificial intelligence" --limit 10

# Search with detailed information
python podcast_search.py --query "productivity" --detailed
```

#### Category Search
```bash
# Search by predefined category
python podcast_search.py --category technology --limit 15

# Available categories: business, comedy, education, news, technology,
# true crime, health, sports, music, science, history, arts
```

#### Filtering Options
```bash
# Exclude explicit content
python podcast_search.py --query "comedy" --no-explicit

# Filter by minimum episode count
python podcast_search.py --query "startups" --min-episodes 50
```

#### Export Results
```bash
# Export to CSV
python podcast_search.py --query "business" --export csv

# Export to JSON
python podcast_search.py --query "entrepreneurship" --export json
```

#### Country-Specific Search
```bash
# Search in specific country (default is US)
python podcast_search.py --query "news" --country GB
```

### Programmatic Usage

You can also use the `PodcastSearchTool` class in your own Python scripts:

```python
from podcast_search import PodcastSearchTool

# Initialize the tool
tool = PodcastSearchTool()

# Search for podcasts
results = tool.search_podcasts(query="AI", limit=10)

# Display results
tool.display_results()

# Get detailed information
tool.display_results(detailed=True)

# Filter results
filtered = tool.filter_results(min_episodes=20, genre="Technology")

# Export to files
tool.export_to_json("my_podcasts.json")
tool.export_to_csv("my_podcasts.csv")

# Search by category
tech_podcasts = tool.search_by_category("technology", limit=15)

# Get specific podcast details
podcast = tool.get_podcast_details(0)  # First result
print(podcast['name'])
print(podcast['feed_url'])
```

### Interactive Examples

Run the example script to see various usage patterns:

```bash
python example_usage.py
```

This will provide an interactive menu with the following examples:
1. Basic Search
2. Category Search
3. Detailed Search Results
4. Filtered Search
5. Export Results
6. Get Podcast Details
7. Multi-Country Search
8. Interactive Search Session

## API Reference

### PodcastSearchTool Class

#### Methods

##### `search_podcasts(query, limit=20, country="US", explicit=None)`
Search for podcasts using keywords.

**Parameters:**
- `query` (str): Search term (podcast name, topic, or keywords)
- `limit` (int): Maximum number of results (default: 20, max: 200)
- `country` (str): Country code for search results (default: "US")
- `explicit` (str): Filter explicit content ('Yes', 'No', or None)

**Returns:** List of podcast dictionaries

##### `search_by_category(category, limit=20)`
Search podcasts by predefined category.

**Parameters:**
- `category` (str): Category name (business, technology, etc.)
- `limit` (int): Maximum number of results

**Returns:** List of podcast dictionaries

##### `filter_results(min_episodes=None, genre=None, explicit_only=False)`
Filter current search results.

**Parameters:**
- `min_episodes` (int): Minimum number of episodes
- `genre` (str): Genre to filter by
- `explicit_only` (bool): Show only explicit content

**Returns:** Filtered list of podcast dictionaries

##### `display_results(detailed=False)`
Display search results in formatted output.

**Parameters:**
- `detailed` (bool): Show detailed information

##### `export_to_csv(filename=None)`
Export results to CSV file.

**Parameters:**
- `filename` (str): Output filename (auto-generated if None)

##### `export_to_json(filename=None)`
Export results to JSON file.

**Parameters:**
- `filename` (str): Output filename (auto-generated if None)

##### `get_podcast_details(index)`
Get detailed information for a specific podcast by index.

**Parameters:**
- `index` (int): Index in search results

**Returns:** Podcast dictionary or None

### Podcast Data Structure

Each podcast result contains the following information:

```python
{
    'name': str,              # Podcast title
    'artist': str,            # Creator/host name
    'description': str,       # Podcast description
    'genre': str,             # Comma-separated genres
    'episode_count': int,     # Number of episodes
    'artwork_url': str,       # High-resolution artwork URL
    'feed_url': str,          # RSS feed URL
    'itunes_url': str,        # iTunes/Apple Podcasts URL
    'release_date': str,      # Latest release date
    'country': str,           # Country code
    'explicit': str           # 'Yes' or 'No'
}
```

## Command Line Arguments

| Argument | Short | Description | Example |
|----------|-------|-------------|---------|
| `--query` | `-q` | Search query | `--query "AI"` |
| `--category` | `-c` | Search by category | `--category technology` |
| `--limit` | `-l` | Max results (max: 200) | `--limit 50` |
| `--country` | | Country code | `--country GB` |
| `--detailed` | `-d` | Show detailed info | `--detailed` |
| `--export` | `-e` | Export format | `--export csv` |
| `--min-episodes` | | Minimum episodes | `--min-episodes 20` |
| `--no-explicit` | | Exclude explicit content | `--no-explicit` |

## Examples

### Example 1: Find Top Business Podcasts
```bash
python podcast_search.py --category business --limit 20 --min-episodes 100
```

### Example 2: Search and Export
```bash
python podcast_search.py --query "machine learning" --detailed --export json
```

### Example 3: Family-Friendly Comedy Podcasts
```bash
python podcast_search.py --category comedy --no-explicit --limit 15
```

### Example 4: Programmatic Workflow
```python
from podcast_search import PodcastSearchTool

# Create tool instance
tool = PodcastSearchTool()

# Search for productivity podcasts
results = tool.search_podcasts("productivity tips", limit=30)

# Filter for established podcasts
established = tool.filter_results(min_episodes=50)

# Export the best ones
tool.search_results = established[:10]
tool.export_to_json("top_productivity_podcasts.json")

# Display summary
for podcast in tool.search_results:
    print(f"{podcast['name']} - {podcast['episode_count']} episodes")
```

## Output Formats

### Console Output (Basic)
```
Found 20 podcasts for: 'artificial intelligence'

1. AI in Business
   By: TechTalk Media
   Genre: Technology, Business
   Episodes: 145

2. The AI Podcast
   By: NVIDIA
   Genre: Technology
   Episodes: 200
```

### Console Output (Detailed)
```
1. AI in Business
   By: TechTalk Media
   Genre: Technology, Business
   Episodes: 145
   Description: Weekly discussions about artificial intelligence...
   Feed URL: https://feeds.example.com/ai-business
   iTunes URL: https://podcasts.apple.com/...
   Explicit: No
```

### CSV Export
```csv
name,artist,genre,episode_count,description,feed_url,itunes_url,explicit
AI in Business,TechTalk Media,"Technology, Business",145,"Weekly discussions...",https://...,https://...,No
```

### JSON Export
```json
{
  "search_query": "artificial intelligence",
  "result_count": 20,
  "timestamp": "2026-01-11T20:30:00",
  "podcasts": [
    {
      "name": "AI in Business",
      "artist": "TechTalk Media",
      "genre": "Technology, Business",
      "episode_count": 145,
      "description": "Weekly discussions...",
      "feed_url": "https://...",
      "itunes_url": "https://...",
      "explicit": "No"
    }
  ]
}
```

## Use Cases

### For Content Creators
- Research competitors in your niche
- Discover collaboration opportunities
- Analyze popular podcast formats and topics

### For Listeners
- Find new podcasts based on interests
- Filter by episode count to find established shows
- Export podcast lists for reference

### For Researchers
- Gather podcast data for analysis
- Export structured data for further processing
- Study podcast trends across categories

### For Developers
- Integrate podcast search into applications
- Build recommendation systems
- Create podcast aggregation tools

## Limitations

- Uses the iTunes API, which has the following constraints:
  - Maximum 200 results per search
  - Limited to podcasts available in Apple Podcasts
  - Rate limiting may apply for excessive requests
  - Some podcast metadata may be incomplete

## Tips & Best Practices

1. **Specific searches work better**: Instead of "podcasts", try "startup advice podcasts"
2. **Use filters effectively**: Combine `--min-episodes` with category searches to find established shows
3. **Export for later**: Save interesting results for future reference
4. **Try different countries**: Some podcasts are region-specific
5. **Check feed URLs**: Always validate feed URLs before subscribing programmatically

## Troubleshooting

### No results found
- Try broader search terms
- Check your internet connection
- Verify the API is accessible

### Export fails
- Ensure you have write permissions in the directory
- Check available disk space

### Slow searches
- Reduce the limit parameter
- iTunes API may have rate limiting

## Contributing

Contributions are welcome! Here are some ideas for improvements:
- Add support for additional podcast APIs (Spotify, PodcastIndex)
- Implement caching for faster repeated searches
- Add podcast episode search functionality
- Create a web interface
- Add RSS feed parser for episode details

## License

This project is provided as-is for educational and personal use.

## API Attribution

This tool uses the iTunes Search API. Apple, iTunes, and Apple Podcasts are trademarks of Apple Inc.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Happy Podcast Hunting! 🎧**
