from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Separate technologies with commas. Example: Django, Python, Bootstrap"
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def __str__(self):
        return self.title

    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
