#!/usr/bin/env python3
"""
Example usage of the Podcast Search Tool
Demonstrates various ways to use the PodcastSearchTool class
"""

from podcast_search import PodcastSearchTool


def example_basic_search():
    """Example: Basic podcast search."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Search")
    print("="*80)

    tool = PodcastSearchTool()
    results = tool.search_podcasts(query="productivity", limit=5)

    if results:
        print(f"\nFound {len(results)} podcasts about productivity:")
        tool.display_results()


def example_category_search():
    """Example: Search by category."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Category Search")
    print("="*80)

    tool = PodcastSearchTool()
    results = tool.search_by_category(category="technology", limit=5)

    if results:
        print(f"\nFound {len(results)} technology podcasts:")
        tool.display_results()


def example_detailed_search():
    """Example: Search with detailed results."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Detailed Search Results")
    print("="*80)

    tool = PodcastSearchTool()
    results = tool.search_podcasts(query="AI", limit=3)

    if results:
        print(f"\nDetailed information for {len(results)} AI podcasts:")
        tool.display_results(detailed=True)


def example_filtered_search():
    """Example: Search with filters."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Filtered Search")
    print("="*80)

    tool = PodcastSearchTool()
    tool.search_podcasts(query="business", limit=20)

    # Filter for podcasts with at least 50 episodes
    filtered = tool.filter_results(min_episodes=50)

    print(f"\nBusiness podcasts with 50+ episodes: {len(filtered)}")
    for idx, podcast in enumerate(filtered[:5], 1):
        print(f"{idx}. {podcast['name']} - {podcast['episode_count']} episodes")


def example_export_results():
    """Example: Export search results."""
    print("\n" + "="*80)
    print("EXAMPLE 5: Export Results")
    print("="*80)

    tool = PodcastSearchTool()
    results = tool.search_podcasts(query="startups", limit=10)

    if results:
        # Export to JSON
        tool.export_to_json("startup_podcasts.json")

        # Export to CSV
        tool.export_to_csv("startup_podcasts.csv")

        print("\nResults exported to both JSON and CSV files!")


def example_podcast_details():
    """Example: Get details for a specific podcast."""
    print("\n" + "="*80)
    print("EXAMPLE 6: Get Podcast Details")
    print("="*80)

    tool = PodcastSearchTool()
    results = tool.search_podcasts(query="entrepreneurship", limit=5)

    if results:
        # Get details for the first podcast
        podcast = tool.get_podcast_details(0)

        if podcast:
            print("\nDetailed information for the first result:")
            print(f"Name: {podcast['name']}")
            print(f"Artist: {podcast['artist']}")
            print(f"Genre: {podcast['genre']}")
            print(f"Episodes: {podcast['episode_count']}")
            print(f"Description: {podcast['description']}")
            print(f"iTunes URL: {podcast['itunes_url']}")
            print(f"Feed URL: {podcast['feed_url']}")


def example_multiple_countries():
    """Example: Search in different countries."""
    print("\n" + "="*80)
    print("EXAMPLE 7: Multi-Country Search")
    print("="*80)

    tool = PodcastSearchTool()

    countries = ["US", "GB", "CA", "AU"]

    for country in countries:
        results = tool.search_podcasts(query="news", limit=3, country=country)
        if results:
            print(f"\nTop news podcasts in {country}:")
            for idx, podcast in enumerate(results, 1):
                print(f"  {idx}. {podcast['name']} by {podcast['artist']}")


def interactive_search():
    """Example: Interactive search session."""
    print("\n" + "="*80)
    print("EXAMPLE 8: Interactive Search")
    print("="*80)

    tool = PodcastSearchTool()

    while True:
        print("\n--- Podcast Search Menu ---")
        print("1. Search by keywords")
        print("2. Search by category")
        print("3. View last results")
        print("4. Export last results")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            query = input("Enter search keywords: ").strip()
            if query:
                limit = input("Number of results (default 10): ").strip() or "10"
                tool.search_podcasts(query=query, limit=int(limit))
                tool.display_results()

        elif choice == "2":
            print("\nCategories: business, comedy, education, news, technology,")
            print("            true crime, health, sports, music, science, history, arts")
            category = input("Enter category: ").strip()
            if category:
                tool.search_by_category(category=category)
                tool.display_results()

        elif choice == "3":
            if tool.search_results:
                tool.display_results(detailed=True)
            else:
                print("No previous search results.")

        elif choice == "4":
            if tool.search_results:
                format_choice = input("Export format (json/csv): ").strip().lower()
                if format_choice == "json":
                    tool.export_to_json()
                elif format_choice == "csv":
                    tool.export_to_csv()
                else:
                    print("Invalid format.")
            else:
                print("No results to export.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    """Run all examples or specific example."""
    print("\n" + "="*80)
    print("PODCAST SEARCH TOOL - EXAMPLE USAGE")
    print("="*80)

    print("\nSelect an example to run:")
    print("1. Basic Search")
    print("2. Category Search")
    print("3. Detailed Search Results")
    print("4. Filtered Search")
    print("5. Export Results")
    print("6. Get Podcast Details")
    print("7. Multi-Country Search")
    print("8. Interactive Search")
    print("9. Run all examples (1-7)")

    choice = input("\nEnter your choice (1-9): ").strip()

    examples = {
        "1": example_basic_search,
        "2": example_category_search,
        "3": example_detailed_search,
        "4": example_filtered_search,
        "5": example_export_results,
        "6": example_podcast_details,
        "7": example_multiple_countries,
        "8": interactive_search,
    }

    if choice in examples:
        examples[choice]()
    elif choice == "9":
        for i in range(1, 8):
            examples[str(i)]()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
