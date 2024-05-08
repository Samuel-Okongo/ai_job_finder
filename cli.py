# cli.py
import click
from main import search_jobs

@click.group()
def cli():
    """A simple command-line tool to find AI-related jobs using OpenAI."""
    pass

@click.command()
@click.option('--skills', prompt='Enter your skills',
              help='Your skills and technologies you are proficient in.')
@click.option('--preferences', prompt='Enter your job preferences',
              help='Preferred job characteristics, like remote, specific industries, etc.')
def search(skills, preferences):
    """Search for jobs that match your skills and preferences."""
    try:
        results = search_jobs(skills, preferences)
        if results:
            print("\nJob Opportunities:")
            print(results)
        else:
            print("No jobs found matching the criteria.")
    except Exception as e:
        print(f"An error occurred: {e}")

cli.add_command(search)

if __name__ == '__main__':
    cli()


