from django.core.management.base import BaseCommand
from crops.models import Crop

class Command(BaseCommand):
    help = 'Populates the database with sample crop data'
    
    def handle(self, *args, **kwargs):
        crops_data = [
            {
                'name': 'Maize',
                'scientific_name': 'Zea mays',
                'description': 'A staple cereal crop grown for grain and fodder.',
                'optimal_temp_min': 18,
                'optimal_temp_max': 30,
                'rainfall_min': 500,
                'rainfall_max': 1200,
                'soil_types': 'well-drained loam, clay loam',
                'planting_season': 'Long rains (March-May)',
                'harvest_period': 'August-September'
            },
            {
                'name': 'Beans',
                'scientific_name': 'Phaseolus vulgaris',
                'description': 'Legume crop grown for protein-rich seeds.',
                'optimal_temp_min': 20,
                'optimal_temp_max': 25,
                'rainfall_min': 400,
                'rainfall_max': 600,
                'soil_types': 'well-drained, fertile soils',
                'planting_season': 'Short rains (October-November)',
                'harvest_period': 'January-February'
            },
            # Add more crops...
        ]
        
        for crop_data in crops_data:
            Crop.objects.get_or_create(**crop_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated crop data'))