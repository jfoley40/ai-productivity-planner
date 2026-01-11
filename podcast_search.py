#!/usr/bin/env python3
"""
Podcast Search Tool
A comprehensive tool for searching and discovering podcasts using the iTunes API.
"""

import requests
import json
import csv
from typing import List, Dict, Optional
from datetime import datetime
import argparse


class PodcastSearchTool:
    """Main class for searching and managing podcast search results."""

    BASE_URL = "https://itunes.apple.com/search"

    def __init__(self):
        self.search_results = []
        self.last_search_query = ""

    def search_podcasts(
        self,
        query: str,
        limit: int = 20,
        country: str = "US",
        explicit: Optional[str] = None
    ) -> List[Dict]:
        """
        Search for podcasts using the iTunes API.

        Args:
            query: Search term (podcast name, topic, or keywords)
            limit: Maximum number of results (default: 20, max: 200)
            country: Country code for search results (default: US)
            explicit: Filter explicit content ('Yes', 'No', or None for all)

        Returns:
            List of podcast dictionaries with search results
        """
        params = {
            'term': query,
            'media': 'podcast',
            'entity': 'podcast',
            'limit': min(limit, 200),  # iTunes API max is 200
            'country': country
        }

        if explicit:
            params['explicit'] = explicit

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            self.search_results = self._process_results(data.get('results', []))
            self.last_search_query = query

            return self.search_results

        except requests.RequestException as e:
            print(f"Error searching podcasts: {e}")
            return []

    def _process_results(self, raw_results: List[Dict]) -> List[Dict]:
        """Process and format raw API results."""
        processed = []

        for item in raw_results:
            podcast = {
                'name': item.get('collectionName', 'N/A'),
                'artist': item.get('artistName', 'N/A'),
                'description': self._clean_description(item.get('description', 'No description available')),
                'genre': ', '.join(item.get('genres', [])),
                'episode_count': item.get('trackCount', 0),
                'artwork_url': item.get('artworkUrl600', item.get('artworkUrl100', 'N/A')),
                'feed_url': item.get('feedUrl', 'N/A'),
                'itunes_url': item.get('collectionViewUrl', 'N/A'),
                'release_date': item.get('releaseDate', 'N/A'),
                'country': item.get('country', 'N/A'),
                'explicit': 'Yes' if item.get('collectionExplicitness') == 'explicit' else 'No'
            }
            processed.append(podcast)

        return processed

    def _clean_description(self, description: str, max_length: int = 500) -> str:
        """Clean and truncate podcast descriptions."""
        if len(description) > max_length:
            return description[:max_length] + "..."
        return description

    def display_results(self, detailed: bool = False):
        """Display search results in a formatted way."""
        if not self.search_results:
            print("No results to display.")
            return

        print(f"\n{'='*80}")
        print(f"Found {len(self.search_results)} podcasts for: '{self.last_search_query}'")
        print(f"{'='*80}\n")

        for idx, podcast in enumerate(self.search_results, 1):
            print(f"{idx}. {podcast['name']}")
            print(f"   By: {podcast['artist']}")
            print(f"   Genre: {podcast['genre']}")
            print(f"   Episodes: {podcast['episode_count']}")

            if detailed:
                print(f"   Description: {podcast['description']}")
                print(f"   Feed URL: {podcast['feed_url']}")
                print(f"   iTunes URL: {podcast['itunes_url']}")
                print(f"   Explicit: {podcast['explicit']}")

            print()

    def search_by_category(self, category: str, limit: int = 20) -> List[Dict]:
        """Search podcasts by category/genre."""
        categories = {
            'business': 'business podcast',
            'comedy': 'comedy podcast',
            'education': 'education podcast',
            'news': 'news podcast',
            'technology': 'technology podcast',
            'true crime': 'true crime podcast',
            'health': 'health fitness podcast',
            'sports': 'sports podcast',
            'music': 'music podcast',
            'science': 'science podcast',
            'history': 'history podcast',
            'arts': 'arts podcast',
        }

        search_term = categories.get(category.lower(), f"{category} podcast")
        return self.search_podcasts(search_term, limit=limit)

    def filter_results(
        self,
        min_episodes: Optional[int] = None,
        genre: Optional[str] = None,
        explicit_only: bool = False
    ) -> List[Dict]:
        """Filter current search results based on criteria."""
        filtered = self.search_results.copy()

        if min_episodes:
            filtered = [p for p in filtered if p['episode_count'] >= min_episodes]

        if genre:
            filtered = [p for p in filtered if genre.lower() in p['genre'].lower()]

        if explicit_only:
            filtered = [p for p in filtered if p['explicit'] == 'Yes']

        return filtered

    def export_to_csv(self, filename: str = None):
        """Export search results to CSV file."""
        if not self.search_results:
            print("No results to export.")
            return

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"podcast_search_{timestamp}.csv"

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'artist', 'genre', 'episode_count',
                            'description', 'feed_url', 'itunes_url', 'explicit']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for podcast in self.search_results:
                    row = {k: podcast[k] for k in fieldnames}
                    writer.writerow(row)

            print(f"Results exported to {filename}")

        except IOError as e:
            print(f"Error exporting to CSV: {e}")

    def export_to_json(self, filename: str = None):
        """Export search results to JSON file."""
        if not self.search_results:
            print("No results to export.")
            return

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"podcast_search_{timestamp}.json"

        try:
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump({
                    'search_query': self.last_search_query,
                    'result_count': len(self.search_results),
                    'timestamp': datetime.now().isoformat(),
                    'podcasts': self.search_results
                }, jsonfile, indent=2, ensure_ascii=False)

            print(f"Results exported to {filename}")

        except IOError as e:
            print(f"Error exporting to JSON: {e}")

    def get_podcast_details(self, index: int) -> Optional[Dict]:
        """Get detailed information for a specific podcast by index."""
        if 0 <= index < len(self.search_results):
            return self.search_results[index]
        return None


def main():
    """Main function for CLI interface."""
    parser = argparse.ArgumentParser(
        description="Search and discover podcasts using iTunes API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search for podcasts about AI
  python podcast_search.py --query "artificial intelligence"

  # Search by category with limit
  python podcast_search.py --category technology --limit 10

  # Search and export to CSV
  python podcast_search.py --query "productivity" --export csv

  # Detailed results display
  python podcast_search.py --query "startups" --detailed
        """
    )

    parser.add_argument(
        '--query', '-q',
        type=str,
        help='Search query (keywords, podcast name, topic)'
    )

    parser.add_argument(
        '--category', '-c',
        type=str,
        choices=['business', 'comedy', 'education', 'news', 'technology',
                'true crime', 'health', 'sports', 'music', 'science', 'history', 'arts'],
        help='Search by category'
    )

    parser.add_argument(
        '--limit', '-l',
        type=int,
        default=20,
        help='Maximum number of results (default: 20, max: 200)'
    )

    parser.add_argument(
        '--country',
        type=str,
        default='US',
        help='Country code for search (default: US)'
    )

    parser.add_argument(
        '--detailed', '-d',
        action='store_true',
        help='Show detailed information for each podcast'
    )

    parser.add_argument(
        '--export', '-e',
        type=str,
        choices=['csv', 'json'],
        help='Export results to file (csv or json)'
    )

    parser.add_argument(
        '--min-episodes',
        type=int,
        help='Filter podcasts with minimum number of episodes'
    )

    parser.add_argument(
        '--no-explicit',
        action='store_true',
        help='Exclude explicit content'
    )

    args = parser.parse_args()

    # Initialize the search tool
    tool = PodcastSearchTool()

    # Perform search
    if args.query:
        explicit_filter = 'No' if args.no_explicit else None
        tool.search_podcasts(
            query=args.query,
            limit=args.limit,
            country=args.country,
            explicit=explicit_filter
        )
    elif args.category:
        tool.search_by_category(category=args.category, limit=args.limit)
    else:
        parser.print_help()
        return

    # Apply filters if specified
    if args.min_episodes:
        results = tool.filter_results(min_episodes=args.min_episodes)
        tool.search_results = results

    # Display results
    tool.display_results(detailed=args.detailed)

    # Export if requested
    if args.export == 'csv':
        tool.export_to_csv()
    elif args.export == 'json':
        tool.export_to_json()


if __name__ == "__main__":
    main()
