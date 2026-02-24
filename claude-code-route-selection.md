Add a route selection feature that works like Google Maps — show multiple route options and let the user choose which one to take. Here's what to build:

## Route Selection Screen

After the user enters start and end addresses, instead of automatically picking one route:

1. Call Google Directions API with `provideRouteAlternatives: true` to get 2-3 different route options
2. Show a **route selection screen** before entering the tracking view

### Route Selection UI

Display a split view:
- **Left/Top: Map** showing all route options overlaid on the dark map
  - The recommended/fastest route in bright accent color (#C8D96F) 
  - Alternative routes in dimmer colors (#C8D96F55 at 30% opacity)
  - When user hovers/taps a route card, that route highlights bright on the map
  
- **Right/Bottom: Route Cards** (one per route option), each showing:
  - **Route name/label**: "Via I-75 N and I-65 N" or "Via I-95 N" (extract from Google's `summary` field)
  - **Total drive time**: e.g., "21 hr 15 min" (from `legs[0].duration.text`)
  - **Total distance**: e.g., "1,347 miles" (from `legs[0].distance.text`)
  - **Hospitals found**: After a quick scan, show count like "~42 hospitals on this route"
  - **Tags/badges**: 
    - "Fastest" on the shortest-time route
    - "Shortest" on the shortest-distance route (if different)
    - "Most Hospitals" on the route with the most hospitals (if notably more)
  - **A "Select This Route" button** on each card

### How to count hospitals per route quickly

For each route alternative, do a quick scan:
- Sample 5-8 points evenly along each route
- Do a Places nearbySearch at each point (radius 24km / 15mi, type=hospital)
- Deduplicate by place_id
- Show the count on the route card
- Don't fetch full details yet — just the count

### After Selection

When the user clicks "Select This Route":
1. Store the selected route's polyline/path
2. Do the FULL hospital discovery (sample every 20mi, get details for nearby hospitals)
3. Transition to the tracking view with the loading animation: "Finding hospitals along your route... (X of Y points searched)"
4. Then enter the normal live tracking experience

## Route Info Banner (persistent during tracking)

Once tracking begins, show a compact info banner below the nav bar:
- Route summary: "Via I-75 N & I-65 N"
- Drive time remaining (calculated from user's current position to destination using route progress)
- Distance remaining
- "Change Route" button on the right
- This banner should be collapsible (tap to minimize to just the route name)

## Design

Keep the same dark Inversa aesthetic. Route cards should look like premium dark cards with:
- Dark surface (#111111) background
- Subtle border (#1F1F1F)
- The selected/hovered card gets a left border accent (#C8D96F)
- Generous padding (20px)
- Clean typography — route name in bold 18px, details in muted 13px
- Smooth hover animation (slight lift + border color change)

On mobile, show the map on top (40vh) and route cards scrollable below.
On desktop, show map on left (60% width) and cards on right (40%).

## Important

- Make sure the route polyline is clearly visible as a LINE on the map, not just dots
- Each route should be a different shade so they're distinguishable
- The selected route on the tracking view should have a subtle glow effect
- Keep all existing functionality (GPS tracking, hospital categorization, ahead/behind, etc.)
