# AI Productivity Planner

A collection of productivity tools to help you plan, organize, and discover content for your creative projects.

## Tools Included

### 1. Project Power Prep Tool 📋
An interactive HTML-based tool for project planning and idea validation.

**Features:**
- Pre-launch checklist management
- Idea validator with refinement questions
- Export to PDF or copy to clipboard
- Browser-based with local storage

**Files:**
- `Python_Script_to_Create_ZIP_File.ipynb` - Colab notebook that generates the tool
- Generated output: `podcast_prep_tool.zip` containing `pod_prep.html` and instructions

### 2. Podcast Search Tool 🎙️
A powerful Python-based podcast discovery tool using the iTunes API.

**Features:**
- Search podcasts by keywords, topics, or categories
- Filter by episode count, genre, and explicit content
- Multi-country search support
- Export results to CSV or JSON
- Both CLI and programmatic usage

**Quick Start:**
```bash
# Install dependencies
pip install -r requirements.txt

# Search for podcasts
python podcast_search.py --query "productivity" --limit 10

# Search by category
python podcast_search.py --category technology --export json

# Run interactive examples
python example_usage.py
```

**Files:**
- `podcast_search.py` - Main podcast search tool
- `example_usage.py` - Interactive examples and usage patterns
- `requirements.txt` - Python dependencies
- `PODCAST_SEARCH_README.md` - Detailed documentation

## Getting Started

### Prerequisites
- Modern web browser (for Project Power Prep Tool)
- Python 3.7+ (for Podcast Search Tool)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/jfoley40/ai-productivity-planner.git
cd ai-productivity-planner
```

2. For Python tools, install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Examples

### Podcast Search Tool

**CLI Usage:**
```bash
# Basic search
python podcast_search.py --query "artificial intelligence"

# Detailed results with export
python podcast_search.py --query "startups" --detailed --export csv

# Filter by minimum episodes
python podcast_search.py --category business --min-episodes 50
```

**Python Usage:**
```python
from podcast_search import PodcastSearchTool

tool = PodcastSearchTool()
results = tool.search_podcasts("AI", limit=20)
tool.display_results(detailed=True)
tool.export_to_json("ai_podcasts.json")
```

## Documentation

- **Podcast Search Tool**: See [PODCAST_SEARCH_README.md](PODCAST_SEARCH_README.md) for detailed documentation
- **Project Power Prep**: Instructions included in the generated ZIP file

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is available for educational and personal use.