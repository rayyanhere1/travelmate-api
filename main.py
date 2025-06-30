from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# CORS for frontend-backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
class Destination(BaseModel):
    name: str
    description: str
    image: str

class Hotel(BaseModel):
    name: str
    description: str
    image: str

class Flight(BaseModel):
    airline: str
    from_: str
    to: str
    departure: str
    return_: Optional[str] = None
    price: str
    image: str
    class_: str

class Booking(BaseModel):
    type: str  # 'destination', 'hotel', 'flight'
    name: str
    email: str
    details: dict

# In-memory data
DESTINATIONS = [
    {
        "name": "Rome, Italy",
        "description": "Walk through ancient history and vibrant piazzas.",
        "image": "/rome.jpg",
        "gallery": ["/rome.jpg", "/hero-bg.jpg"],
        "details": "Rome is a city rich in history, culture, and cuisine. Explore the Colosseum, Trevi Fountain, and more.",
    },
    {
        "name": "Santorini, Greece",
        "description": "Explore the stunning blue domes and sunsets.",
        "image": "/santorini.jpg",
        "gallery": ["/santorini.jpg", "/canaves-oia.jpg"],
        "details": "Santorini is famous for its whitewashed villages, blue domes, and breathtaking sunsets over the Aegean Sea.",
    },
    {
        "name": "Kyoto, Japan",
        "description": "Discover ancient temples and cherry blossoms.",
        "image": "/kyoto.jpg",
        "gallery": ["/kyoto.jpg", "/hoshinoya-kyoto.jpg"],
        "details": "Kyoto offers tranquil temples, beautiful gardens, and the magic of cherry blossom season.",
    },
    {
        "name": "Barcelona, Spain",
        "description": "Marvel at Gaudí's masterpieces and Mediterranean vibes.",
        "image": "/barcelona.jpg",
        "gallery": ["/barcelona.jpg", "/ritz-paris.jpg"],
        "details": "Barcelona is a vibrant city with unique architecture, delicious food, and lively beaches.",
    },
    {
        "name": "Paris, France",
        "description": "Experience the romance and art of Paris.",
        "image": "/paris.jpg",
        "gallery": ["/paris.jpg", "/ritz-paris.jpg"],
        "details": "Paris is the city of lights, love, and world-class cuisine. Visit the Eiffel Tower, Louvre, and more.",
    },
    {
        "name": "New York, USA",
        "description": "The city that never sleeps, full of energy and sights.",
        "image": "/newyork.jpg",
        "gallery": ["/newyork.jpg", "/hero-bg.jpg"],
        "details": "New York offers iconic landmarks, Broadway, and a melting pot of cultures.",
    },
    {
        "name": "Istanbul, Turkey",
        "description": "Where East meets West in a city of wonders.",
        "image": "/istanbul.jpg",
        "gallery": ["/istanbul.jpg", "/hero-bg.jpg"],
        "details": "Istanbul is a city of history, vibrant bazaars, and stunning mosques.",
    },
    {
        "name": "Cape Town, South Africa",
        "description": "A city of mountains, beaches, and adventure.",
        "image": "/capetown.jpg",
        "gallery": ["/capetown.jpg", "/hero-bg.jpg"],
        "details": "Cape Town is known for Table Mountain, beautiful coastlines, and rich culture.",
    },
]

HOTELS = [
    {
        "name": "The Ritz Paris",
        "description": "Luxury stay in the heart of Paris.",
        "image": "/ritz-paris.jpg",
        "gallery": ["/ritz-paris.jpg"],
        "details": "The Ritz Paris offers timeless luxury, exquisite dining, and a prime location.",
    },
    {
        "name": "Canaves Oia Suites, Santorini",
        "description": "Elegant suites with breathtaking views.",
        "image": "/canaves-oia.jpg",
        "gallery": ["/canaves-oia.jpg"],
        "details": "Canaves Oia Suites provide a luxurious escape with stunning caldera views.",
    },
    {
        "name": "Hoshinoya Kyoto",
        "description": "Riverside retreat blending tradition and comfort.",
        "image": "/hoshinoya-kyoto.jpg",
        "gallery": ["/hoshinoya-kyoto.jpg"],
        "details": "Hoshinoya Kyoto is a serene riverside retreat with traditional Japanese hospitality.",
    },
]

FLIGHTS = [
    {
        "airline": "Emirates",
        "from": "Dubai (DXB)",
        "to": "New York (JFK)",
        "departure": "2024-07-10 08:00",
        "return": "2024-07-20 22:00",
        "price": "$2,400",
        "image": "/emirates.jpg",
        "class": "First Class",
        "duration": "14h 30m",
        "stops": "Non-stop",
        "baggage": "2 x 32kg checked, 1 x 7kg cabin",
        "amenities": ["Wi-Fi", "Gourmet Meals", "Flatbed Seat", "Lounge Access"],
    },
    {
        "airline": "Singapore Airlines",
        "from": "Singapore (SIN)",
        "to": "London (LHR)",
        "departure": "2024-08-05 09:30",
        "return": "2024-08-15 21:00",
        "price": "$2,100",
        "image": "/singapore.jpg",
        "class": "Business Class",
        "duration": "13h 10m",
        "stops": "Non-stop",
        "baggage": "2 x 32kg checked, 1 x 7kg cabin",
        "amenities": ["Wi-Fi", "Premium Meals", "Recliner Seat", "Onboard Bar"],
    },
    {
        "airline": "Qatar Airways",
        "from": "Doha (DOH)",
        "to": "Paris (CDG)",
        "departure": "2024-09-01 07:45",
        "return": "2024-09-10 20:30",
        "price": "$2,250",
        "image": "/qatar.jpg",
        "class": "First Class",
        "duration": "7h 30m",
        "stops": "Non-stop",
        "baggage": "2 x 32kg checked, 1 x 7kg cabin",
        "amenities": ["Wi-Fi", "Private Suite", "Gourmet Dining", "Shower Spa"],
    },
    {
        "airline": "Lufthansa",
        "from": "Frankfurt (FRA)",
        "to": "Tokyo (HND)",
        "departure": "2024-10-12 13:00",
        "return": "2024-10-22 23:00",
        "price": "$2,300",
        "image": "/lufthansa.jpg",
        "class": "Business Class",
        "duration": "11h 45m",
        "stops": "1 stop",
        "baggage": "2 x 32kg checked, 1 x 7kg cabin",
        "amenities": ["Wi-Fi", "Lie-flat Seat", "Fine Dining", "Amenity Kit"],
    },
]

BOOKINGS = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the TravelMate API!"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/destinations")
def get_destinations():
    return DESTINATIONS

@app.get("/hotels")
def get_hotels():
    return HOTELS

@app.get("/flights")
def get_flights():
    return FLIGHTS

@app.get("/bookings")
def get_bookings():
    return BOOKINGS

@app.post("/bookings")
async def create_booking(booking: Booking):
    BOOKINGS.append(booking)
    return {"message": "Booking created!"} 