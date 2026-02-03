# ✈️ Flight Routes Management System

A Django-based web application to manage airport routes using a **left/right directional tree structure**.  
The project includes a modern, airline-inspired UI and complete CRUD functionality.

---

## 📌 Project Overview

The **Flight Routes Management System** allows users to:

- Manage airports
- Define directional routes between airports (LEFT / RIGHT)
- Traverse routes in a specific direction
- Identify routes with the longest and shortest durations
- Use a modern dashboard-style interface inspired by top airline systems

---

## 🛠️ Technology Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap 5
- **Database:** SQLite (default)
- **UI Theme:** Custom airline-style
- **Version Control:** Git


---

## 🧩 Core Features

### 1️⃣ Airport Management
- Add, edit, and delete airports
- Modal-based delete confirmation
- Paginated airport listing
- Latest airports displayed on dashboard

### 2️⃣ Route Management
- Create, edit, and delete routes between airports
- Each airport can have:
  - One **LEFT** route
  - One **RIGHT** route
- Route includes duration (in minutes)
- Modal-based delete confirmation
- Validation prevents:
  - Parent and child being the same
  - Multiple routes in the same direction for one parent

### 3️⃣ Route Traversal (Task 1)
- Select a starting airport
- Choose direction (LEFT or RIGHT)
- System traverses until no further node exists
- Displays the **last reachable airport**

### 4️⃣ Route Statistics
- Find airport with **longest route duration**
- Find airport with **shortest route duration**

---

## 🗺️ URL Endpoints

| URL                       | Description                   |
|---------------------------|-------------------------------|
| `/`                       | Dashboard (homepage)          |
| `/airport/add/`           | Add Airport                   |     
| `/airport/<id>/edit/`     | Edit Airport                  |
| `/airport/<id>/delete/`   | Delete Airport (modal)        |
| `/route/add/`             | Add Airport Route             |
| `/route/<id>/edit/`       | Edit Airport Route            |
| `/route/<id>/delete/`     | Delete Airport Route (modal)  |
| `/search/`                | Find Last Reachable Airport   |
| `/stats/`                 | Route Statistics              |

---

## 🧠 Data Model Summary

### Airport
- `name` (unique)
- `created_at`
- `updated_at`

### AirportRoute
- `parent` (Airport)
- `child` (Airport)
- `position` (LEFT / RIGHT)
- `duration` (minutes)
- One LEFT and one RIGHT child per parent enforced

---

## 🎨 UI / UX Highlights

- Dashboard-style homepage
- Collapsible dark luxury sidebar (desktop & mobile)
- Icons-only sidebar mode when collapsed
- Airline-inspired color palette
- Card-based layout
- Bootstrap modals for destructive actions
- Clean forms with inline validation messages

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd flight_routes

python manage.py makemigrations
python manage.py migrate

python manage.py runserver



