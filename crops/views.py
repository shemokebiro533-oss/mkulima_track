from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def crop_recommendation(request):
    """Crop recommendation view"""
    
    # Sample crop data
    sample_crops = [
        {
            'name': 'Maize',
            'description': 'Staple food crop suitable for most regions',
            'season': 'Long rains (March-May)',
            'rainfall': '500-1200 mm',
            'soil': 'Well-drained loam',
            'suitability': 'High',
            'icon': '🌽',
            'id': 'maize'
        },
        {
            'name': 'Beans',
            'description': 'Protein-rich legume, good for intercropping',
            'season': 'Short rains (Oct-Nov)',
            'rainfall': '400-600 mm',
            'soil': 'Fertile, well-drained',
            'suitability': 'High',
            'icon': '🫘',
            'id': 'beans'
        },
        {
            'name': 'Coffee',
            'description': 'Cash crop for high altitude areas',
            'season': 'Main crop (Oct-Dec)',
            'rainfall': '1000-2000 mm',
            'soil': 'Volcanic, well-drained',
            'suitability': 'Medium',
            'icon': '☕',
            'id': 'coffee'
        },
        {
            'name': 'Tea',
            'description': 'Perennial crop for high rainfall areas',
            'season': 'Year-round',
            'rainfall': '1200-3000 mm',
            'soil': 'Acidic, well-drained',
            'suitability': 'Medium',
            'icon': '🍃',
            'id': 'tea'
        },
        {
            'name': 'Potatoes',
            'description': 'Versatile tuber crop',
            'season': 'Depend on rainfall',
            'rainfall': '500-700 mm',
            'soil': 'Loamy, well-drained',
            'suitability': 'High',
            'icon': '🥔',
            'id': 'potatoes'
        },
    ]
    
    if request.method == 'POST':
        # Get form data
        location = request.POST.get('location', 'Central Kenya')
        soil_type = request.POST.get('soil', 'Loam')
        
        # Filter crops based on selection (simplified logic)
        recommended_crops = []
        for crop in sample_crops:
            if soil_type.lower() in crop['soil'].lower():
                recommended_crops.append(crop)
        
        if not recommended_crops:
            recommended_crops = sample_crops[:3]  # Default recommendations
        
        context = {
            'crops': recommended_crops,
            'location': location,
            'soil_type': soil_type,
            'is_result': True
        }
        return render(request, 'crops/recommendations.html', context)
    
    # GET request - show the form
    return render(request, 'crops/recommendation_form.html')

def crop_details(request, crop_name):
    """View for individual crop details"""
    # Crop database
    crops_db = {
        'maize': {
            'name': 'Maize',
            'scientific_name': 'Zea mays',
            'description': 'Maize is a staple food crop in Kenya, grown for both human consumption and animal feed.',
            'planting_season': 'Long rains: March-May, Short rains: Oct-Nov',
            'rainfall': '500-1200 mm annually',
            'temperature': '18-30°C',
            'soil': 'Well-drained loamy soils',
            'spacing': '75cm between rows, 30cm between plants',
            'fertilizer': 'NPK 23:23:0 at planting, CAN for top dressing',
            'pests': 'Stem borers, armyworms, weevils',
            'diseases': 'Maize streak virus, leaf blight, rust',
            'harvest': '3-8 months depending on variety',
            'yield': '15-40 bags per acre',
            'icon': '🌽'
        },
        'beans': {
            'name': 'Beans',
            'scientific_name': 'Phaseolus vulgaris',
            'description': 'Beans are a protein-rich legume, important for food security and soil fertility.',
            'planting_season': 'Short rains: Oct-Nov, Long rains: March-April',
            'rainfall': '400-600 mm',
            'temperature': '20-25°C',
            'soil': 'Well-drained fertile soils',
            'spacing': '50cm between rows, 10cm between plants',
            'fertilizer': 'DAP at planting, foliar feeds during flowering',
            'pests': 'Aphids, bean fly, bruchids',
            'diseases': 'Bean anthracnose, angular leaf spot, root rot',
            'harvest': '2-3 months',
            'yield': '4-10 bags per acre',
            'icon': '🫘'
        },
        'coffee': {
            'name': 'Coffee',
            'scientific_name': 'Coffea arabica',
            'description': 'Coffee is a major cash crop in Kenya, known for its high quality.',
            'planting_season': 'April-May with onset of rains',
            'rainfall': '1000-2000 mm',
            'temperature': '15-24°C',
            'soil': 'Volcanic, well-drained, rich in organic matter',
            'spacing': '2.5m x 2.5m',
            'fertilizer': 'Coffee-specific fertilizer twice a year',
            'pests': 'Coffee berry borer, leaf miners',
            'diseases': 'Coffee berry disease, leaf rust',
            'harvest': 'October-December (main crop)',
            'yield': '2-5 kg per tree',
            'icon': '☕'
        },
        'tea': {
            'name': 'Tea',
            'scientific_name': 'Camellia sinensis',
            'description': 'Tea is a perennial crop, one of Kenya\'s leading foreign exchange earners.',
            'planting_season': 'March-April or September-October',
            'rainfall': '1200-3000 mm',
            'temperature': '13-30°C',
            'soil': 'Deep, well-drained acidic soils (pH 4.5-5.5)',
            'spacing': '1.2m x 0.75m',
            'fertilizer': 'NPK 25:5:5, Sulphate of Ammonia',
            'pests': 'Tea mosquito bug, red spider mite',
            'diseases': 'Blister blight, root rot',
            'harvest': 'Year-round with peaks',
            'yield': '1500-3000 kg per hectare',
            'icon': '🍃'
        },
        'potatoes': {
            'name': 'Potatoes',
            'scientific_name': 'Solanum tuberosum',
            'description': 'Potatoes are a versatile tuber crop grown for food and cash.',
            'planting_season': 'Depends on rainfall patterns',
            'rainfall': '500-700 mm',
            'temperature': '15-20°C',
            'soil': 'Well-drained loamy soils',
            'spacing': '75cm between rows, 30cm between plants',
            'fertilizer': 'NPK 17:17:17 at planting',
            'pests': 'Potato tuber moth, aphids',
            'diseases': 'Late blight, bacterial wilt',
            'harvest': '3-4 months',
            'yield': '10-20 tons per acre',
            'icon': '🥔'
        },
    }
    
    # Get crop data or show 404
    crop = crops_db.get(crop_name.lower())
    if not crop:
        # Return a default crop or show error
        crop = {
            'name': crop_name.title(),
            'description': f'Information about {crop_name} will be available soon.',
            'planting_season': 'Varies by region',
            'rainfall': 'Check local recommendations',
            'icon': '🌱'
        }
    
    return render(request, 'crops/details.html', {'crop': crop})