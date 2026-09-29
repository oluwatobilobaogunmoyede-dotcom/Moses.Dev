from django.core.management.base import BaseCommand
from projects.models import Project

PROJECTS = [
    {
        "title": "Weather App",
        "slug": "weather-app",
        "description": "A responsive weather application built with Django and designed to present weather information in a clean interface.",
        "technologies": "Python, Django, Bootstrap, HTML, CSS",
        "featured": True,
        "github_url": "https://github.com/oluwatobilobaogunmoyede",
        "live_url": "",
    },
    {
        "title": "Memory Game",
        "slug": "memory-game",
        "description": "A browser-based memory matching game with dynamic cards, score tracking and JavaScript event handling.",
        "technologies": "HTML, CSS, JavaScript",
        "featured": True,
        "github_url": "https://github.com/oluwatobilobaogunmoyede",
        "live_url": "",
    },
    {
        "title": "Rock Paper Scissors",
        "slug": "rock-paper-scissors",
        "description": "A simple interactive Rock Paper Scissors game built to practice JavaScript logic, DOM manipulation and events.",
        "technologies": "HTML, CSS, JavaScript",
        "featured": True,
        "github_url": "https://github.com/oluwatobilobaogunmoyede-dotcom/Rock-paper-Scissors.git",
        "live_url": "",
    },
    {
        "title": "Student Result System",
        "slug": "student-result-system",
        "description": "A student-focused web project for presenting academic results and organizing school information.",
        "technologies": "HTML, CSS, JavaScript, Python, Django",
        "featured": False,
        "github_url": "https://github.com/oluwatobilobaogunmoyede",
        "live_url": "",
    },
    {
        "title": "AI Blog",
        "slug": "ai-blog",
        "description": "A blog project focused on AI content, with a backend architecture designed to support database-driven posts.",
        "technologies": "JavaScript, Node.js, MongoDB",
        "featured": False,
        "github_url": "https://github.com/oluwatobilobaogunmoyede",
        "live_url": "",
    },
]

class Command(BaseCommand):
    help = "Create sample portfolio projects"

    def handle(self, *args, **options):
        for data in PROJECTS:
            Project.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
        self.stdout.write(self.style.SUCCESS("Sample portfolio projects created/updated."))
