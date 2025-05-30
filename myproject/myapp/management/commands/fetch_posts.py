import requests
from django.core.management.base import BaseCommand
from myapp.models import Post

class Command(BaseCommand):
    help = 'Fetch posts from mock API and save to database'

    def handle(self, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/posts'  # Replace with your mock API
        response = requests.get(url)

        if response.status_code == 200:
            posts_data = response.json()
            for item in posts_data:
                Post.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'title': item['title'],
                        'body': item['body'],
                        'user_id': item['userId'],
                    }
                )
            self.stdout.write(self.style.SUCCESS("Posts successfully fetched and saved!"))
        else:
            self.stderr.write(f"Failed to fetch posts. Status code: {response.status_code}")
