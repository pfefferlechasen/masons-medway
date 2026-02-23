# Project: Route Hospital Tracker — FL to WI

## Overview
Build a single-page web app that tracks a driver's real-time GPS location along the I-75/I-41 corridor from Lake Belvedere Estates, Florida to Appleton, Wisconsin (~1,400 miles). The app shows hospitals AHEAD of the driver on their route, hiding anything more than 10 minutes behind them. It should feel calm, clean, and easy to use while driving — not flashy or complex.

---

## Core Features

### 1. Real-Time GPS Tracking
- Use the browser Geolocation API with `watchPosition()` to continuously track the user's location
- Show the user's current position on a map (use Leaflet.js with OpenStreetMap tiles — free, no API key)
- Display a pulsing dot for current location
- Update position every 5-10 seconds

### 2. Route-Aware Hospital Filtering (THE KEY FEATURE)
- The driving route follows this corridor (approximate waypoints listed below in the data section)
- For each hospital, calculate whether it is AHEAD or BEHIND the driver based on route progress
- **Hide hospitals that are more than ~10 minutes of driving behind the user** (roughly 10 miles behind at highway speed)
- Show hospitals that are ahead on the route AND within ~5 miles of the highway corridor
- Sort visible hospitals by distance ahead (nearest upcoming first)

### 3. Hospital Cards
- Show hospital name, city, state, star rating, and "24H" badge
- Two action buttons per hospital: "Directions" (opens Google Maps with turn-by-turn from current location) and "Call" (tel: link)
- Show estimated distance ahead (e.g., "12 mi ahead")
- Color-code ratings: green ≥ 4.0, amber ≥ 3.0, red < 3.0

### 4. Simple Top Bar
- Show current state the driver is in (auto-detected from GPS)
- Show how many hospitals are upcoming
- A small "recenter" button for the map

---

## Design Requirements

### Aesthetic: Natural, calm, earthy
- **Background**: Warm off-white (#FAF8F5) or very light warm gray
- **Cards**: White with subtle warm shadow
- **Primary accent**: Muted forest green (#3D6B50) for buttons and highlights  
- **Secondary accent**: Warm terracotta/clay (#C4754B) for alerts/emergency
- **Text**: Dark charcoal (#2C2C2C) for primary, warm gray (#7A7670) for secondary
- **Font**: Use "Inter" from Google Fonts — clean and highly readable
- **Border radius**: Soft, 12px on cards, 8px on buttons
- **No gradients, no neon, no dark mode** — keep it light, natural, and easy on the eyes while driving
- Generous whitespace and padding
- Large touch targets (minimum 44px) for use while driving

### Layout (Mobile-First)
- Top: Compact status bar (current state, hospitals ahead count)
- Middle: Map (takes ~40% of screen height) showing route line, user position dot, and hospital pins
- Bottom: Scrollable list of upcoming hospitals sorted by distance ahead
- The map and list should stay in sync — tapping a card highlights the pin, tapping a pin scrolls to the card

---

## Hospital Data (57 facilities along the route)

```json
[
  {"name":"Good Samaritan Medical Center","city":"West Palm Beach","state":"FL","lat":26.7253,"lng":-80.0514,"rating":4.1,"phone":"+1 561-655-5511"},
  {"name":"St. Mary's Medical Center","city":"West Palm Beach","state":"FL","lat":26.7562,"lng":-80.0625,"rating":4.0,"phone":"+1 561-844-6300"},
  {"name":"HCA Florida JFK North Hospital","city":"West Palm Beach","state":"FL","lat":26.7616,"lng":-80.0876,"rating":4.1,"phone":"+1 561-842-6141"},
  {"name":"Palm Beach Gardens Medical Center","city":"Palm Beach Gardens","state":"FL","lat":26.8295,"lng":-80.0866,"rating":3.6,"phone":"+1 561-622-1411"},
  {"name":"HCA Florida Palms West Hospital","city":"Loxahatchee","state":"FL","lat":26.6841,"lng":-80.2514,"rating":4.3,"phone":"+1 561-798-3300"},
  {"name":"Orlando Health ORMC","city":"Orlando","state":"FL","lat":28.5263,"lng":-81.3785,"rating":4.5,"phone":"+1 321-841-5111"},
  {"name":"UCF Lake Nona Hospital","city":"Orlando","state":"FL","lat":28.3679,"lng":-81.2857,"rating":4.6,"phone":"+1 689-216-8000"},
  {"name":"Orlando Health Dr. P. Phillips","city":"Orlando","state":"FL","lat":28.4292,"lng":-81.4785,"rating":4.5,"phone":"+1 407-351-8500"},
  {"name":"HCA Florida Ocala Hospital","city":"Ocala","state":"FL","lat":29.1751,"lng":-82.137,"rating":4.0,"phone":"+1 352-401-1000"},
  {"name":"AdventHealth Ocala","city":"Ocala","state":"FL","lat":29.1756,"lng":-82.1389,"rating":4.2,"phone":"+1 352-351-7200"},
  {"name":"HCA Florida West Marion Hospital","city":"Ocala","state":"FL","lat":29.1403,"lng":-82.1998,"rating":4.3,"phone":"+1 352-291-3000"},
  {"name":"HCA Florida North Florida Hospital","city":"Gainesville","state":"FL","lat":29.6603,"lng":-82.4116,"rating":4.1,"phone":"+1 352-333-4000"},
  {"name":"UF Health Shands Hospital","city":"Gainesville","state":"FL","lat":29.6399,"lng":-82.3428,"rating":2.9,"phone":"+1 352-265-0111"},
  {"name":"HCA Florida Lake City Hospital","city":"Lake City","state":"FL","lat":30.1835,"lng":-82.6878,"rating":4.1,"phone":"+1 386-719-9000"},
  {"name":"SGMC Health - Main","city":"Valdosta","state":"GA","lat":30.8626,"lng":-83.2871,"rating":4.3,"phone":"+1 229-433-1000"},
  {"name":"SGMC Health - Smith Northview","city":"Valdosta","state":"GA","lat":30.8986,"lng":-83.3356,"rating":4.6,"phone":"+1 229-433-8000"},
  {"name":"Tift Regional Medical Center","city":"Tifton","state":"GA","lat":31.4715,"lng":-83.4919,"rating":2.8,"phone":"+1 229-382-7120"},
  {"name":"Atrium Health Navicent","city":"Macon","state":"GA","lat":32.8338,"lng":-83.6366,"rating":2.5,"phone":"+1 478-633-1000"},
  {"name":"Piedmont Macon","city":"Macon","state":"GA","lat":32.8473,"lng":-83.6187,"rating":4.0,"phone":"+1 478-765-7000"},
  {"name":"Southern Regional Medical Center","city":"Riverdale","state":"GA","lat":33.5794,"lng":-84.3895,"rating":2.9,"phone":"+1 770-991-8000"},
  {"name":"Grady Memorial Hospital","city":"Atlanta","state":"GA","lat":33.7518,"lng":-84.382,"rating":2.9,"phone":"+1 404-616-1000"},
  {"name":"Emory University Hospital","city":"Atlanta","state":"GA","lat":33.7924,"lng":-84.3216,"rating":3.8,"phone":"+1 404-712-2000"},
  {"name":"Piedmont Atlanta Hospital","city":"Atlanta","state":"GA","lat":33.8089,"lng":-84.3949,"rating":3.9,"phone":"+1 404-605-5000"},
  {"name":"Northside Hospital Atlanta","city":"Atlanta","state":"GA","lat":33.9094,"lng":-84.3546,"rating":3.2,"phone":"+1 404-851-8000"},
  {"name":"Erlanger Baroness Hospital","city":"Chattanooga","state":"TN","lat":35.0486,"lng":-85.2895,"rating":2.6,"phone":"+1 423-778-7000"},
  {"name":"Parkridge Medical Center","city":"Chattanooga","state":"TN","lat":35.0349,"lng":-85.2676,"rating":4.4,"phone":"+1 423-698-6061"},
  {"name":"Parkridge East Hospital","city":"Chattanooga","state":"TN","lat":34.9988,"lng":-85.2193,"rating":4.4,"phone":"+1 423-894-7870"},
  {"name":"UT Medical Center","city":"Knoxville","state":"TN","lat":35.94,"lng":-83.9432,"rating":2.9,"phone":"+1 865-305-9000"},
  {"name":"Parkwest Medical Center","city":"Knoxville","state":"TN","lat":35.917,"lng":-84.1006,"rating":3.6,"phone":"+1 865-373-1000"},
  {"name":"North Knoxville Medical Center","city":"Powell","state":"TN","lat":36.0536,"lng":-83.9977,"rating":4.4,"phone":"+1 865-859-8000"},
  {"name":"Albert B. Chandler Hospital","city":"Lexington","state":"KY","lat":38.031,"lng":-84.507,"rating":3.4,"phone":"+1 859-323-5000"},
  {"name":"Saint Joseph Hospital","city":"Lexington","state":"KY","lat":38.0327,"lng":-84.5235,"rating":4.3,"phone":"+1 859-313-1000"},
  {"name":"Baptist Health Lexington","city":"Lexington","state":"KY","lat":38.0182,"lng":-84.512,"rating":3.1,"phone":"+1 859-260-6100"},
  {"name":"The Christ Hospital","city":"Cincinnati","state":"OH","lat":39.1211,"lng":-84.5103,"rating":3.2,"phone":"+1 513-585-2000"},
  {"name":"Mercy Health West Hospital","city":"Cincinnati","state":"OH","lat":39.1807,"lng":-84.5963,"rating":3.3,"phone":"+1 513-215-5000"},
  {"name":"Cincinnati Children's Hospital","city":"Cincinnati","state":"OH","lat":39.1415,"lng":-84.5008,"rating":3.8,"phone":"+1 513-636-4200"},
  {"name":"Miami Valley Hospital","city":"Dayton","state":"OH","lat":39.7455,"lng":-84.1856,"rating":3.0,"phone":"+1 937-208-8000"},
  {"name":"Kettering Health Dayton","city":"Dayton","state":"OH","lat":39.7698,"lng":-84.2026,"rating":4.3,"phone":"+1 937-723-3200"},
  {"name":"Kettering Health Washington Twp","city":"Dayton","state":"OH","lat":39.6354,"lng":-84.2036,"rating":4.6,"phone":"+1 937-401-6000"},
  {"name":"Blanchard Valley Hospital","city":"Findlay","state":"OH","lat":41.0165,"lng":-83.6509,"rating":3.1,"phone":"+1 419-423-4500"},
  {"name":"ProMedica Toledo Hospital","city":"Toledo","state":"OH","lat":41.6722,"lng":-83.5952,"rating":2.8,"phone":"+1 419-291-4000"},
  {"name":"Mercy Health St. Vincent","city":"Toledo","state":"OH","lat":41.6685,"lng":-83.5427,"rating":3.4,"phone":"+1 419-251-3232"},
  {"name":"Mercy Health St. Anne","city":"Toledo","state":"OH","lat":41.6936,"lng":-83.6258,"rating":3.4,"phone":"+1 419-407-2663"},
  {"name":"Henry Ford Hospital","city":"Detroit","state":"MI","lat":42.3677,"lng":-83.0847,"rating":3.0,"phone":"+1 313-916-2600"},
  {"name":"DMC Harper University Hospital","city":"Detroit","state":"MI","lat":42.3518,"lng":-83.0564,"rating":3.6,"phone":"+1 313-745-8040"},
  {"name":"DMC Sinai Grace Hospital","city":"Detroit","state":"MI","lat":42.4186,"lng":-83.1822,"rating":2.6,"phone":"+1 313-966-3300"},
  {"name":"Beacon Kalamazoo Hospital","city":"Kalamazoo","state":"MI","lat":42.3076,"lng":-85.5601,"rating":3.4,"phone":"+1 269-226-7000"},
  {"name":"Bronson Methodist Hospital","city":"Kalamazoo","state":"MI","lat":42.2857,"lng":-85.5803,"rating":2.9,"phone":"+1 269-341-7654"},
  {"name":"Froedtert Hospital","city":"Milwaukee","state":"WI","lat":43.0409,"lng":-88.0245,"rating":2.6,"phone":"+1 414-805-3000"},
  {"name":"Aurora Sinai Medical Center","city":"Milwaukee","state":"WI","lat":43.0427,"lng":-87.9275,"rating":3.3,"phone":"+1 414-219-2000"},
  {"name":"Ascension St. Francis Hospital","city":"Milwaukee","state":"WI","lat":42.9857,"lng":-87.9353,"rating":3.7,"phone":"+1 414-647-5000"},
  {"name":"SSM Health St. Agnes Hospital","city":"Fond du Lac","state":"WI","lat":43.7776,"lng":-88.431,"rating":3.2,"phone":"+1 920-929-2300"},
  {"name":"ThedaCare MC Fond du Lac","city":"Fond du Lac","state":"WI","lat":43.7863,"lng":-88.4741,"rating":3.6,"phone":"+1 920-913-4400"},
  {"name":"Aurora MC Fond du Lac","city":"Fond du Lac","state":"WI","lat":43.782,"lng":-88.3985,"rating":4.4,"phone":"+1 920-907-7500"},
  {"name":"Aurora MC Oshkosh","city":"Oshkosh","state":"WI","lat":44.027,"lng":-88.5958,"rating":3.6,"phone":"+1 920-456-6000"},
  {"name":"Ascension Mercy Oshkosh","city":"Oshkosh","state":"WI","lat":44.0132,"lng":-88.6002,"rating":3.2,"phone":"+1 920-223-2000"},
  {"name":"ThedaCare RMC Appleton","city":"Appleton","state":"WI","lat":44.2787,"lng":-88.3939,"rating":3.1,"phone":"+1 920-731-4101"},
  {"name":"Ascension St. Elizabeth Appleton","city":"Appleton","state":"WI","lat":44.2483,"lng":-88.4024,"rating":3.0,"phone":"+1 920-738-2000"}
]
```

## Route Waypoints (for determining ahead/behind)

These approximate waypoints define the driving route from south to north. Use them to project the user's position onto the route and calculate which direction is "ahead."

```json
[
  [26.69, -80.10],
  [26.83, -80.09],
  [27.50, -80.35],
  [28.37, -81.29],
  [28.53, -81.38],
  [29.14, -82.14],
  [29.18, -82.14],
  [29.64, -82.34],
  [29.66, -82.41],
  [30.18, -82.69],
  [30.86, -83.29],
  [31.47, -83.49],
  [32.84, -83.64],
  [33.58, -84.39],
  [33.75, -84.38],
  [33.91, -84.35],
  [34.99, -85.22],
  [35.05, -85.27],
  [35.92, -84.10],
  [35.94, -83.94],
  [36.05, -84.00],
  [37.50, -84.30],
  [38.03, -84.51],
  [39.12, -84.51],
  [39.64, -84.20],
  [39.75, -84.19],
  [41.02, -83.65],
  [41.67, -83.60],
  [41.69, -83.63],
  [42.29, -83.75],
  [42.37, -83.08],
  [42.31, -85.56],
  [43.00, -87.93],
  [43.04, -88.02],
  [43.78, -88.43],
  [44.01, -88.60],
  [44.25, -88.40],
  [44.28, -88.39]
]
```

## Logic for "Ahead vs Behind" Filtering

1. **Snap user to route**: Find the closest route segment to the user's GPS coordinates
2. **Calculate route progress**: Express the user's position as a percentage of the total route (0% = Lake Belvedere Estates, 100% = Appleton)
3. **Snap each hospital to route**: Similarly express each hospital's position as a route percentage
4. **Filter**: Show hospitals where `hospital_progress > user_progress - 0.007` (the 0.007 ≈ 10 miles / 1400 miles ≈ roughly 10 min behind buffer)
5. **Sort**: By route progress ascending (nearest upcoming hospital first)

## Technical Requirements

- **Single page app** — one `index.html` file with inline CSS and JS
- **Map library**: Leaflet.js with OpenStreetMap tiles (free, no API key needed)
  - CDN: https://unpkg.com/leaflet@1.9.4/dist/leaflet.css and leaflet.js
- **No frameworks needed** — vanilla HTML/CSS/JS is fine
- **Mobile-first and responsive** — this will be used on a phone while driving
- **Directions links**: Use `https://www.google.com/maps/dir/?api=1&destination={lat},{lng}&travelmode=driving` — this opens Google Maps or Apple Maps natively on the phone
- **Call links**: Use `tel:{phone}` format
- **Fallback**: If GPS is denied, show all hospitals in a static list with a banner saying "Enable location for route tracking"
- **Host anywhere**: The final output should be a single HTML file deployable to Netlify, Cloudflare Pages, or Firebase Hosting via drag-and-drop

## What NOT to Do
- No dark mode or dark backgrounds
- No neon or bright gradients  
- No complex animations or transitions
- No login or authentication
- No backend or database
- No heavy frameworks (React, Vue, etc.) — keep it vanilla
- Don't overcomplicate the UI — a driver glancing at their phone needs to instantly see the nearest hospital and tap one button
