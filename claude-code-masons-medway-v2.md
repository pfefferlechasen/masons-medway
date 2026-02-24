# Claude Code Prompt: Mason's MedWay v2 — Dynamic Route Hospital Finder

## What to Build

Transform Mason's MedWay from a hardcoded single-route app into a **dynamic route hospital finder** that works on ANY route in the US. The user enters a start and end address, the app calculates the driving route, finds all hospitals within 15 minutes of the interstate along that route, tracks the driver's live GPS, and categorizes hospitals as "ahead" or "recently passed."

The app is currently deployed at: https://github.com/pfefferlecasen/masons-medway
Clone that repo and rebuild it with the new functionality described below.

---

## Core Architecture

### Tech Stack
- **Frontend**: Single `index.html` with inline CSS/JS (keep it deployable as a static site)
- **Map**: Leaflet.js with CartoDB Dark Matter tiles (already in current version)
- **Routing**: Google Directions API (to calculate the driving route)
- **Hospital Search**: Google Places API (Nearby Search) to find hospitals dynamically along the route
- **GPS Tracking**: Browser Geolocation API with `watchPosition()`
- **Animations**: GSAP + ScrollTrigger (already in current version)
- **Hosting**: Static deploy to Vercel/Netlify

### API Keys Needed
The app will need a Google Maps API key with these APIs enabled:
- Directions API
- Places API (Nearby Search)
- Maps JavaScript API (optional, since we use Leaflet)

Add a setup screen where the user can paste their Google API key on first use, and store it in the URL hash or a simple prompt so it persists but never hits a server. Alternatively, hardcode a key placeholder `YOUR_GOOGLE_API_KEY` that I can replace before deploying.

---

## User Flow

### Step 1: Route Entry Screen
When the app loads and no route is active, show a clean entry screen:
- App title "MASON'S MEDWAY" at top
- Large heading: "Enter your route"
- Two input fields:
  - **Start**: text input with placeholder "Starting address or city"
  - **End**: text input with placeholder "Destination address or city"
- A "Use my current location" button next to the Start field that auto-fills with GPS coordinates
- Big **"Find Hospitals"** button
- Keep the dark, premium Inversa-style aesthetic from the current version

### Step 2: Route Calculation & Hospital Discovery
When the user submits:
1. **Call Google Directions API** to get the driving route polyline
2. **Decode the polyline** into lat/lng points
3. **Sample points along the route** every ~20 miles
4. **For each sample point, call Google Places Nearby Search** for `type=hospital` within a 15-minute driving radius (~15 miles as the crow flies, to approximate)
5. **Deduplicate hospitals** (same place_id)
6. **For each hospital, calculate its "route distance"** — how far along the route it sits (as a percentage or mile marker)
7. **Display the route on the map** and show all hospital pins
8. **Transition to the tracking view**

### Step 3: Live Tracking View (main experience)
Once the route and hospitals are loaded:
- Show the full-screen map with route line and hospital markers
- Start GPS tracking with `watchPosition()`
- Continuously update the user's position on the map
- **Categorize every hospital into one of three groups:**

#### Hospital Categories:

**🟢 UPCOMING** (ahead on route)
- Hospital's route progress > user's route progress
- Show with GREEN markers on map
- Sort by nearest upcoming first
- Show "X mi ahead" label

**🟡 RECENTLY PASSED** (behind, but within 15 min / ~15 miles)
- Hospital's route progress < user's route progress
- Distance behind is ≤ 15 miles (or route progress difference × total route miles ≤ 15)
- Show with YELLOW/AMBER markers on map
- Show "X mi behind — passed ~Y min ago" label
- Display in a separate section BELOW upcoming hospitals
- Add a subtle banner: "You've passed these, but they're still reachable"

**🔴 OUT OF RANGE** (too far behind)
- Hospital's route progress < user's route progress by more than 15 miles
- **Remove from the list entirely** — don't show these
- Fade their map markers to near-invisible or remove them

---

## Detailed UI Sections (Tracking View)

### Nav Bar (Fixed)
- Left: "MASON'S MEDWAY"
- Center: Route summary (e.g., "Orlando, FL → Appleton, WI")
- Right: GPS status pulse dot (green = active, red = no GPS)
- "Change Route" button (small, top-right) — returns to route entry screen

### Hero: Full-Screen Map
- Leaflet map with dark tiles
- Route drawn as a glowing line
- User position: pulsing blue dot
- Hospital markers color-coded:
  - Green dots = upcoming
  - Amber dots = recently passed
  - Markers should show hospital name on hover/tap
- Map auto-pans to keep user centered, but user can manually pan (disable auto-pan while user is interacting, re-enable after 10 seconds of no interaction)

### 001 · Status Dashboard
- **Current Location**: City, State (reverse geocode from GPS or just nearest city)
- **Next Hospital**: Name + "X mi ahead"
- **Hospitals Ahead**: Count
- **Recently Passed**: Count (with amber color)

### 002 · Upcoming Hospitals
- Section header: "002 · UPCOMING HOSPITALS"
- Subtext: "Facilities ahead of you, within 15 minutes of the highway"
- Hospital cards sorted by distance ahead (nearest first):
  - Hospital name (bold)
  - City, State (muted)
  - Star rating (green ≥4.0, amber ≥3.0, red <3.0)
  - "24H" or "Open" / "Closed" badge (from Places API hours data)
  - Distance: "12 mi ahead · 3 mi off highway"
  - Two buttons: **📍 Directions** (Google Maps link) and **📞 Call** (tel: link)
- Staggered scroll-reveal animation

### 003 · Recently Passed (IMPORTANT — NEW SECTION)
- Section header: "003 · RECENTLY PASSED"
- Amber/yellow accent color for this section
- Subtext: "You've passed these hospitals, but they're still within 15 minutes behind you"
- Same card format as upcoming, but with:
  - Distance: "8 mi behind · ~10 min back"
  - Amber left border on cards instead of green
  - Slightly dimmed opacity (0.85) compared to upcoming
- If no hospitals are recently passed, show: "No recently passed hospitals"
- As the driver progresses, hospitals move from "Upcoming" → "Recently Passed" → removed from list (animated transition)

### 004 · Emergency Quick Actions
- 🚨 **Call 911** — big red button
- 📍 **Nearest Hospital Now** — Google Maps hospital search from current location
- 📋 **Back to Top** — scroll to map

### Footer
- Route info, disclaimer, © 2025

---

## Hospital Data Enrichment

For each hospital found via Google Places API, store and display:
- `name` — from Places API
- `place_id` — for deduplication
- `lat`, `lng` — coordinates
- `rating` — Google rating
- `rating_count` — number of reviews
- `phone` — from Place Details API (make a details call for each hospital)
- `open_now` — whether currently open
- `address` — formatted address
- `route_mile` — calculated: which mile marker on the route is this hospital nearest to
- `distance_from_route` — how far off the highway (straight-line distance from nearest route point)

---

## Route Progress Calculation

```
function calculateRouteProgress(userLat, userLng, routePoints):
    // Find the closest point on the route to the user
    // Return the cumulative distance from route start to that point
    // Express as both miles and percentage of total route

    minDist = Infinity
    closestIndex = 0
    
    for i in range(len(routePoints)):
        d = haversineDistance(userLat, userLng, routePoints[i].lat, routePoints[i].lng)
        if d < minDist:
            minDist = d
            closestIndex = i
    
    // Calculate cumulative distance to closestIndex
    cumulativeMiles = 0
    for i in range(1, closestIndex + 1):
        cumulativeMiles += haversineDistance(
            routePoints[i-1].lat, routePoints[i-1].lng,
            routePoints[i].lat, routePoints[i].lng
        )
    
    return {
        miles: cumulativeMiles,
        percent: cumulativeMiles / totalRouteMiles,
        nearestRoutePoint: routePoints[closestIndex]
    }
```

Apply the same function to each hospital to get its `route_mile`. Then:
- **Upcoming**: `hospital.route_mile > user.route_mile`
- **Recently Passed**: `user.route_mile - hospital.route_mile <= 15` (miles)
- **Out of Range**: `user.route_mile - hospital.route_mile > 15`

---

## Google API Calls

### Directions API (route calculation)
```
GET https://maps.googleapis.com/maps/api/directions/json?
  origin={start_address}
  &destination={end_address}
  &key={API_KEY}
```
Response includes `overview_polyline.points` — decode this to get route coordinates.

NOTE: Since this is a frontend-only app, use the **Google Maps JavaScript API DirectionsService** instead of the REST API to avoid CORS issues:

```javascript
const directionsService = new google.maps.DirectionsService();
directionsService.route({
  origin: startAddress,
  destination: endAddress,
  travelMode: 'DRIVING'
}, (result, status) => {
  if (status === 'OK') {
    const path = result.routes[0].overview_path; // array of LatLng
    const routePoints = path.map(p => ({ lat: p.lat(), lng: p.lng() }));
    // Use routePoints for everything
  }
});
```

### Places Nearby Search (hospital discovery)
For each sample point along the route:
```javascript
const service = new google.maps.places.PlacesService(map);
service.nearbySearch({
  location: { lat: sampleLat, lng: sampleLng },
  radius: 24140, // 15 miles in meters
  type: 'hospital'
}, (results, status) => {
  // Collect and deduplicate by place_id
});
```

### Place Details (phone numbers, hours)
For each unique hospital:
```javascript
service.getDetails({
  placeId: hospital.place_id,
  fields: ['formatted_phone_number', 'opening_hours', 'website']
}, (place, status) => {
  hospital.phone = place.formatted_phone_number;
  hospital.open_now = place.opening_hours?.isOpen();
  hospital.website = place.website;
});
```

**IMPORTANT**: Place Details calls are expensive. Batch them and only call for the nearest 30-40 hospitals to the user, not all of them at once. Load more details as the user progresses along the route.

---

## Design Specifications

Keep the exact same Inversa.com-inspired aesthetic from the current version:

### Color Palette
| Token              | Value     | Usage                                    |
|--------------------|-----------|------------------------------------------|
| `--bg`             | `#0A0A0A` | Page background                          |
| `--surface`        | `#111111` | Card backgrounds                         |
| `--surface-hover`  | `#1A1A1A` | Card hover state                         |
| `--border`         | `#1F1F1F` | Subtle borders                           |
| `--text-primary`   | `#F5F5F0` | Headings                                 |
| `--text-secondary` | `#8A8A82` | Body text                                |
| `--text-muted`     | `#4A4A45` | Labels, faded elements                   |
| `--accent`         | `#C8D96F` | Primary accent — sage green              |
| `--danger`         | `#E85D5D` | Emergency, 911                           |
| `--amber`          | `#D4A54A` | Recently passed, medium ratings          |
| `--success`        | `#5DAE72` | Upcoming, high ratings, GPS active       |
| `--route-glow`     | `#C8D96F33`| Route line glow                         |

### Typography
- Font: Inter (Google Fonts)
- Hero: 48-64px mobile, 80-120px desktop
- Section numbers: monospace, faded
- Labels: uppercase, letter-spaced
- Body: 14-16px, line-height 1.6-1.8

### Animations
- GSAP ScrollTrigger for section reveals
- Staggered card animations
- Smooth transitions when hospitals move from Upcoming → Recently Passed

### Mobile First
- Min touch target: 48px
- Large call/directions buttons
- 911 button must be most prominent
- Test 375px-430px width

---

## Loading States

### While calculating route:
- Show a fullscreen loading overlay with the dark theme
- Pulsing line animation
- Text: "Calculating route..."

### While finding hospitals:
- Show the map with route drawn
- Progress indicator: "Finding hospitals along your route... (12 of ~30 points searched)"
- Hospital pins appear on map in real-time as they're discovered

### While fetching details:
- Hospital cards show name and rating immediately
- Phone number shows "Loading..." then populates
- Open/Closed badge appears once details load

---

## Edge Cases

1. **No GPS**: Show all hospitals along route without ahead/behind categorization. Banner: "Enable location for live tracking"
2. **User off route**: If user is >5 miles from the route, show a banner: "You appear to be off route. Showing nearest hospitals instead." and fall back to a simple radius search
3. **Very short route**: If route is <20 miles, search every 5 miles instead of every 20
4. **Very long route**: If route is >1000 miles, search every 30 miles to reduce API calls
5. **API key missing**: Show a setup prompt asking the user to enter their Google API key
6. **Rate limiting**: Queue Places API calls with 200ms delay between them to avoid hitting rate limits

---

## File Structure

Since this needs the Google Maps JavaScript API, the `index.html` must include:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initApp" async defer></script>
```

Keep everything in a single `index.html` file. The app should remain deployable as a static site to Vercel/Netlify with zero build steps.

---

## What NOT to Do
- No backend server — everything runs client-side
- No React/Vue/Angular — vanilla JS only
- No npm/webpack/build tools
- No light mode — dark theme only
- No default Leaflet markers — custom styled circles
- Don't load all Place Details at once — lazy load as user approaches
- Don't show hospitals that are >15 miles off the highway corridor
- Don't show hospitals that are >15 miles behind the user
