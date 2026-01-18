"""
Vienna Route Metrics - Configuration File
TU Wien | Denkweisen der Informatik
"""

import os
from dotenv import load_dotenv

# =============================================================================
# LOAD ENVIRONMENT VARIABLES
# =============================================================================
# Load variables from .env file
load_dotenv()

# =============================================================================
# API CONFIGURATION
# =============================================================================
# Google Maps API Key
GOOGLE_MAPS_API_KEY:  str = os.getenv("GOOGLE_MAPS_API_KEY", "YOUR_API_KEY_HERE")

# Google Maps Directions API base URL
GOOGLE_MAPS_BASE_URL: str = "https://maps.googleapis.com/maps/api/directions/json"

# =============================================================================
# EMISSION FACTORS (CO₂ in grams per kilometer)
# =============================================================================
# Sources: Austrian Environmental Agency (Umweltbundesamt)
# These values represent average emissions for each transport mode
EMISSION_FACTORS:  dict[str, float] = {
    'driving': 140.0,    # Average car:  140g CO₂/km (includes fuel production)
    'transit': 40.0,     # Vienna public transit: ~40g CO₂/km per passenger
    'bicycling':  0.0,   # Zero direct emissions
    'walking': 0.0       # Zero direct emissions
}

# =============================================================================
# COST FACTORS (in EUR)
# =============================================================================
# Cost calculation basis: 
# - Car: fuel cost only (€0.15/km based on avg consumption and fuel price)
# - Transit: Vienna single ticket (Einzelfahrt)
# - Bicycle/Walking: No direct monetary cost
COST_FACTORS: dict[str, dict[str, float]] = {
    'driving': {
        'per_km': 0.15,       # €0.15 per km (fuel cost only)
        'flat_rate': 0.0
    },
    'transit':  {
        'per_km':  0.0,
        'flat_rate':  2.40    # Vienna single ticket:  €2.40
    },
    'bicycling': {
        'per_km': 0.0,
        'flat_rate': 0.0
    },
    'walking':  {
        'per_km':  0.0,
        'flat_rate': 0.0
    }
}

# =============================================================================
# TRANSPORT MODE LABELS
# =============================================================================
# User-friendly labels for the UI
MODE_LABELS: dict[str, str] = {
    'driving': '🚗 Auto',
    'transit': '🚌 Öffentlich',
    'bicycling': '🚴 Fahrrad',
    'walking': '🚶 Zu Fuß'
}

# Mode labels without emoji (for data processing)
MODE_LABELS_PLAIN: dict[str, str] = {
    'driving': 'Auto',
    'transit':  'Öffentliche Verkehrsmittel',
    'bicycling': 'Fahrrad',
    'walking': 'Zu Fuß'
}

# =============================================================================
# MAP CONFIGURATION
# =============================================================================
# Default map center (Vienna city center - Stephansplatz)
DEFAULT_MAP_CENTER: tuple[float, float] = (48.2082, 16.3738)

# Default zoom level for Vienna
DEFAULT_MAP_ZOOM: int = 13

# Route colors for different transport modes
ROUTE_COLORS: dict[str, str] = {
    'driving':  '#EF4444',   # Red for car
    'transit': '#3B82F6',    # Blue for public transit
    'bicycling': '#22C55E',  # Green for bicycle
    'walking': '#F59E0B'     # Orange/Yellow for walking
}

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================
# Supported transport modes (Google Maps API mode values)
SUPPORTED_MODES: list[str] = ['driving', 'transit', 'bicycling', 'walking']

# Request timeout for API calls (in seconds)
API_TIMEOUT: int = 10

# Maximum retries for failed API requests
MAX_RETRIES: int = 3