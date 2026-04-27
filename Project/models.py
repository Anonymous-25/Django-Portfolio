from django.db import models
# =======[ Portfolio Category Model ]=======
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"
# =======[ Portfolio Item Model ]=======
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.URLField()
    categories = models.ManyToManyField(
        PortfolioCategory,
        related_name="projects",
        blank=True
    )
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    technologies = models.CharField(
        max_length=200,
        help_text="Example: Django, Python, React"
    )
    created_at = models.DateField()
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Portfolio Project"
        verbose_name_plural = "Portfolio Projects"
# =======[ Work Model ]=======
class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.URLField(
        help_text="Enter icon URL (for example: https://.../icon.svg)"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"