from django.db import models
# ===============[ Web Settings Model ] ===============
class WebSettings(models.Model):
    favicon = models.URLField(help_text="URL of website favicon")
    title = models.CharField(max_length=200)
    background = models.URLField(help_text="URL of website favicon")
    second_title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    def save(self, *args, **kwargs):
        if not self.pk and WebSettings.objects.exists():
            raise Exception("Only one WebSettings instance is allowed")
        return super().save(*args, **kwargs)
    def __str__(self):
        return "Website Settings"
    class Meta:
        verbose_name = "Web Setting"
        verbose_name_plural = "Web Settings"
# ===============[ SEO Settings Model ] ===============
from django.db import models
from django.core.exceptions import ValidationError
class SEOSettings(models.Model):
    meta_keywords = models.CharField(max_length=300, blank=True)
    meta_image = models.URLField(blank=True)
    canonical_url = models.URLField(blank=True)
    robots = models.CharField(
        max_length=50,
        default="index, follow",
        help_text="Example: index, follow or noindex, nofollow"
    )
    google_site_verification = models.CharField(max_length=200, blank=True)
    bing_site_verification = models.CharField(max_length=200, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk and SEOSettings.objects.exists():
            raise ValidationError("Only one SEOSettings instance allowed.")
        return super().save(*args, **kwargs)
    def __str__(self):
        return "SEO Settings"
    class Meta:
        verbose_name = "SEO Setting"
        verbose_name_plural = "SEO Settings"