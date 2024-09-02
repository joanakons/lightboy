from django import forms
from configurator.models import Configurator

ROOM_TYPES_OPTIONS = {
    "foyer_entryway": "Foyer/Entryway",
    "staircase": "Staircase",
    "mud_room": "Mud Room",
    "pantry": "Pantry",
    "butlers_pantry": "Butler's Pantry",
    "kitchen": "Kitchen",
    "dining_room": "Dining Room",
    "living_rooms": "Living Rooms",
    "family_room": "Family Room",
    "powder_room_half_bath": "Powder Room/Half Bath",
    "primary_bathroom": "Primary Bathroom",
    "guest_bathroom": "Guest Bathroom",
    "en_suite": "En Suite",
    "primary_bedroom": "Primary Bedroom",
    "kids_bedroom": "Kids' Bedroom",
    "nursery": "Nursery",
    "guest_room": "Guest Room",
    "walk_in_closet": "Walk-in Closet",
    "dressing_room": "Dressing Room",
    "playroom": "Playroom",
    "laundry_room": "Laundry Room",
    "linen_room": "Linen Room",
    "gym_exercise_room": "Gym/Exercise Room",
    "meditation_room": "Meditation Room",
    "home_theater": "Home Theater",
    "game_room": "Game Room",
    "billiards_room": "Billiards Room",
    "home_spa": "Home Spa",
    "media_room": "Media Room",
    "music_room": "Music Room",
    "craft_room_art_studio": "Craft Room/Art Studio",
    "home_office": "Home Office",
    "library_study": "Library/Study",
    "study_nook": "Study Nook",
    "study_room": "Study Room",
    "wine_cellar": "Wine Cellar",
    "wine_storage_room": "Wine Storage Room",
    "wine_tasting_room": "Wine Tasting Room",
    "home_bar": "Home Bar",
    "pet_room": "Pet Room",
    "safe_room": "Safe Room",
    "conservatory": "Conservatory",
    "observatory": "Observatory",
    "sun_room": "Sun Room",
    "loft": "Loft",
    "attic": "Attic",
    "storage_room": "Storage Room",
    "utility_mechanical_room": "Utility/Mechanical Room",
    "basement": "Basement",
    "cellar": "Cellar",
    "den": "Den",
    "garage": "Garage",
    "workshop": "Workshop",
    "bonus_room": "Bonus Room"
}


class ConfiguratorForm(forms.ModelForm):
    class Meta:
        model = Configurator
        fields = ['room', 'area', 'number_of_outlets']

        widgets = {
            'room': forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=ROOM_TYPES_OPTIONS,
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Select Room Type'
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please enter a category'
                }
            ),
            'number_of_outlets': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please enter a category'
                }
            )
        }
