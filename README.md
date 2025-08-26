# ✈️ AeroScout – Flight Deal Tracker

AeroScout is a Python project that helps users **find cheap flight deals**.  
Users sign up through a Google Form, get added automatically to a mailing list,  
and whenever flights to their chosen destinations drop below a threshold price,  
they receive an **instant email notification**.  

---

## 🌍 Features
- 🔎 Search flight offers using **Amadeus API**  
- 📊 Store user preferences (email, destination, price) in **Google Sheets** via Sheety  
- 📩 Send **automatic email alerts** when cheap flights are available  
- 📝 Easy sign-up flow through a **Google Form**  
- 🧩 Clean, modular structure for easy scaling  

---

## 🛠️ Tech Stack
- **Python 3**
- **Amadeus API** – for flight searches
- **Sheety API** – for Google Sheets integration
- **Twilio API** - for Cloud messaging
- **SMTP** – for email notifications
- **dotenv** – for managing environment variables

---

## 📂 Project Structure
Aero-Scout/
│── README.md
│── requirements.txt
│── Flight-Search-Project/
    │── main.py # orchestrates the program
    │── flight_search.py # handles flight API calls
    |── flight_data.py # stores all the flights data
    │── notification_manager.py # sends email notifications
    │── data_manager.py # manages Sheety/Google Sheets data
    │── .env.example # loads env variables

---

## ⚙️ Setup & Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/Rahil-Mokashi/Aero-Scout.git
   cd Aero-Scout/Flight-Search-Project