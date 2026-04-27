from django.db import models
# ===============[ Profile Model ] ===============
class Profile(models.Model):
    icon = "fa-solid fa-user"
    # BASIC
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=100)
    location = models.TextField()
    # LINKS
    github = models.URLField(blank=True, null=True)
    linkedin = models.CharField(blank=True, null=True, max_length=100)
    discord = models.URLField(blank=True, null=True)
    reddit = models.URLField(blank=True, null=True)
    dev = models.URLField(blank=True, null=True)
    # DESCRIPTION
    about = models.TextField()
    location_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.pk and Profile.objects.exists():
            raise Exception("Only one Profile instance is allowed")
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
# ===============[ Education Model ] ===============
class Education(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.institution}"
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
# ===============[ Certification Model ] ===============
class Certification(models.Model):
    certificate_name = models.CharField(max_length=200)
    provider_name = models.CharField(max_length=200)
    provider_icon = models.URLField(blank=True, null=True)
    verification_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.certificate_name} - {self.provider_name}"
    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
# ===============[ Experience Model ] ===============
class Experience(models.Model):
    designation = models.CharField(max_length=200)
    work_type = models.CharField(max_length=100) 
    organization = models.CharField(max_length=200)
    duration = models.CharField(max_length=50) 
    description = models.TextField()
    def __str__(self):
        return f"{self.designation} at {self.organization}"
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
# ===============[ Skill Model ] ===============
class Skill(models.Model):
    from django.core.validators import MinValueValidator, MaxValueValidator
    skill_name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],help_text="Enter value between 0 and 100"
    )
    def __str__(self):
        return self.skill_name
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"