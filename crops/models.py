from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    """Model for different crop types"""
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    optimal_temp_min = models.IntegerField()
    optimal_temp_max = models.IntegerField()
    rainfall_min = models.IntegerField(help_text="Minimum annual rainfall in mm")
    rainfall_max = models.IntegerField(help_text="Maximum annual rainfall in mm")
    soil_types = models.CharField(max_length=200, help_text="Comma-separated soil types")
    planting_season = models.CharField(max_length=100)
    harvest_period = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crops/', blank=True)
    
    def __str__(self):
        return self.name

class Recommendation(models.Model):
    """Model for crop recommendations based on location"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2)
    reasoning = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-confidence_score']
    
    def __str__(self):
        return f"{self.user.username} - {self.crop.name}"

class PlantingSchedule(models.Model):
    """Model for planting schedules"""
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    optimal_planting_start = models.DateField()
    optimal_planting_end = models.DateField()
    days_to_harvest = models.IntegerField()
    care_instructions = models.TextField()
    
    def __str__(self):
        return f"{self.crop.name} in {self.region}"