# ALX Travel App 0x00

## Project Overview

This project is a Django-based travel application backend that manages travel listings, bookings, and reviews. It is a duplicate of the original `alx_travel_app` project and includes the following key features:

- Database models for Listings, Bookings, and Reviews.
- Serializers for API data representation.
- A custom management command to seed the database with sample data.

---

## Project Structure

- `listings/models.py` — Defines the Listing, Booking, and Review models with appropriate fields and relationships.
- `listings/serializers.py` — Contains serializers for the Listing and Booking models.
- `listings/management/commands/seed.py` — Custom management command to populate the database with sample listings.
- `alx_travel_app_0x00/` — Django project configuration, including settings and URL routing.

---
