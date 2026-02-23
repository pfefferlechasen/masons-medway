import json

def generate_html():
    hospitals = [
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
      {"name":"HCA Florida North Florida Hospital","city":"Gainesville","state":"FL","lat":29.6603,"lng":-82.4116,"rating":4.1,"phone":"+1 352-333-4000"},
      {"name":"UF Health Shands Hospital","city":"Gainesville","state":"FL","lat":29.6399,"lng":-82.3428,"rating":2.9,"phone":"+1 352-265-0111"},
      {"name":"HCA Florida Lake City Hospital","city":"Lake City","state":"FL","lat":30.1835,"lng":-82.6878,"rating":4.1,"phone":"+1 386-719-9000"},
      {"name":"SGMC Health - Main","city":"Valdosta","state":"GA","lat":30.8626,"lng":-83.2871,"rating":4.3,"phone":"+1 229-433-1000"},
      {"name":"Tift Regional Medical Center","city":"Tifton","state":"GA","lat":31.4715,"lng":-83.4919,"rating":2.8,"phone":"+1 229-382-7120"},
      {"name":"Atrium Health Navicent","city":"Macon","state":"GA","lat":32.8338,"lng":-83.6366,"rating":2.5,"phone":"+1 478-633-1000"},
      {"name":"Piedmont Macon","city":"Macon","state":"GA","lat":32.8473,"lng":-83.6187,"rating":4.0,"phone":"+1 478-765-7000"},
      {"name":"Southern Regional Medical Center","city":"Riverdale","state":"GA","lat":33.5794,"lng":-84.3895,"rating":2.9,"phone":"+1 770-991-8000"},
      {"name":"Grady Memorial Hospital","city":"Atlanta","state":"GA","lat":33.7518,"lng":-84.382,"rating":2.9,"phone":"+1 404-616-1000"},
      {"name":"Emory University Hospital","city":"Atlanta","state":"GA","lat":33.7924,"lng":-84.3216,"rating":3.8,"phone":"+1 404-712-2000"},
      {"name":"Piedmont Atlanta Hospital","city":"Atlanta","state":"GA","lat":33.8089,"lng":-84.3949,"rating":3.9,"phone":"+1 404-605-5000"},
      {"name":"Northside Hospital Atlanta","city":"Atlanta","state":"GA","lat":33.9094,"lng":-84.3546,"rating":3.2,"phone":"+1 404-851-8000"},
      {"name":"Ascension Saint Thomas Rutherford","city":"Murfreesboro","state":"TN","lat":35.861,"lng":-86.4249,"rating":3.9,"phone":"+1 615-396-4100"},
      {"name":"TriStar Centennial Medical Center","city":"Nashville","state":"TN","lat":36.1539,"lng":-86.8091,"rating":4.6,"phone":"+1 615-342-1000"},
      {"name":"TriStar Skyline Medical Center","city":"Nashville","state":"TN","lat":36.2453,"lng":-86.75,"rating":4.1,"phone":"+1 615-769-2000"},
      {"name":"Nashville General Hospital","city":"Nashville","state":"TN","lat":36.1668,"lng":-86.8071,"rating":4.3,"phone":"+1 615-341-4000"},
      {"name":"TriStar Southern Hills Medical Center","city":"Nashville","state":"TN","lat":36.0766,"lng":-86.7219,"rating":4.3,"phone":"+1 615-781-4000"},
      {"name":"Ascension Saint Thomas West","city":"Nashville","state":"TN","lat":36.1297,"lng":-86.8448,"rating":4.4,"phone":"+1 615-222-2111"},
      {"name":"TriStar Greenview Regional Hospital","city":"Bowling Green","state":"KY","lat":36.9649,"lng":-86.4368,"rating":4.4,"phone":"+1 270-793-1000"},
      {"name":"The Medical Center at Bowling Green","city":"Bowling Green","state":"KY","lat":36.9958,"lng":-86.4297,"rating":2.3,"phone":"+1 270-745-1000"},
      {"name":"Baptist Health Hardin","city":"Elizabethtown","state":"KY","lat":37.7107,"lng":-85.8768,"rating":2.3,"phone":"+1 270-737-1212"},
      {"name":"UofL Health \u2013 UofL Hospital","city":"Louisville","state":"KY","lat":38.2487,"lng":-85.7455,"rating":3.1,"phone":"+1 502-562-3000"},
      {"name":"Norton Hospital","city":"Louisville","state":"KY","lat":38.2479,"lng":-85.7509,"rating":2.9,"phone":"+1 502-629-8000"},
      {"name":"Baptist Health Louisville","city":"Louisville","state":"KY","lat":38.2379,"lng":-85.6391,"rating":3.1,"phone":"+1 502-897-8100"},
      {"name":"Columbus Regional Health","city":"Columbus","state":"IN","lat":39.2168,"lng":-85.8961,"rating":2.8,"phone":"+1 812-379-4441"},
      {"name":"Franciscan Health Indianapolis","city":"Indianapolis","state":"IN","lat":39.6492,"lng":-86.0798,"rating":2.7,"phone":"+1 317-528-5000"},
      {"name":"Community Hospital South","city":"Indianapolis","state":"IN","lat":39.6376,"lng":-86.1325,"rating":3.0,"phone":"+1 317-887-7000"},
      {"name":"IU Health University Hospital","city":"Indianapolis","state":"IN","lat":39.776,"lng":-86.177,"rating":3.4,"phone":"+1 317-944-5000"},
      {"name":"Sidney & Lois Eskenazi Hospital","city":"Indianapolis","state":"IN","lat":39.7775,"lng":-86.1843,"rating":3.0,"phone":"+1 317-880-0000"},
      {"name":"Ascension St. Vincent Indianapolis","city":"Indianapolis","state":"IN","lat":39.9086,"lng":-86.1974,"rating":3.6,"phone":"+1 317-338-2345"},
      {"name":"Witham Health Services","city":"Lebanon","state":"IN","lat":40.0774,"lng":-86.4732,"rating":4.6,"phone":"+1 765-485-8000"},
      {"name":"IU Health Arnett Hospital","city":"Lafayette","state":"IN","lat":40.4005,"lng":-86.8079,"rating":3.3,"phone":"+1 765-448-8000"},
      {"name":"Methodist Hospitals Northlake","city":"Gary","state":"IN","lat":41.5993,"lng":-87.3577,"rating":3.3,"phone":"+1 219-886-4000"},
      {"name":"St. Catherine Hospital","city":"East Chicago","state":"IN","lat":41.6348,"lng":-87.4475,"rating":4.0,"phone":"+1 219-392-1700"},
      {"name":"Advocate Christ Medical Center","city":"Oak Lawn","state":"IL","lat":41.7213,"lng":-87.732,"rating":3.3,"phone":"+1 708-684-8000"},
      {"name":"Holy Cross Hospital","city":"Chicago","state":"IL","lat":41.7691,"lng":-87.6924,"rating":3.9,"phone":"+1 773-884-9000"},
      {"name":"John H. Stroger Jr. Hospital","city":"Chicago","state":"IL","lat":41.8727,"lng":-87.6737,"rating":3.1,"phone":"+1 312-864-6000"},
      {"name":"Rush University Medical Center","city":"Chicago","state":"IL","lat":41.8746,"lng":-87.6688,"rating":3.4,"phone":"+1 312-942-5000"},
      {"name":"Northwestern Memorial Hospital","city":"Chicago","state":"IL","lat":41.8949,"lng":-87.6214,"rating":3.5,"phone":"+1 312-926-2000"},
      {"name":"Vista Medical Center East","city":"Waukegan","state":"IL","lat":42.3781,"lng":-87.8326,"rating":2.7,"phone":"+1 847-360-3000"},
      {"name":"Advocate Condell Medical Center","city":"Libertyville","state":"IL","lat":42.2736,"lng":-87.9567,"rating":2.9,"phone":"+1 847-362-2900"},
      {"name":"Aurora Medical Center Kenosha","city":"Kenosha","state":"WI","lat":42.5695,"lng":-87.9355,"rating":3.5,"phone":"+1 262-948-5600"},
      {"name":"Froedtert Pleasant Prairie Hospital","city":"Pleasant Prairie","state":"WI","lat":42.5645,"lng":-87.9241,"rating":3.3,"phone":"+1 262-577-8000"},
      {"name":"Ascension All Saints Hospital","city":"Racine","state":"WI","lat":42.7314,"lng":-87.8277,"rating":4.3,"phone":"+1 262-687-4011"},
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

    waypoints = [
      [26.69, -80.10], [26.83, -80.09], [27.50, -80.35], [28.37, -81.29], [28.53, -81.38],
      [29.15, -82.14], [29.64, -82.34], [30.18, -82.69], [30.86, -83.29], [31.47, -83.49],
      [32.84, -83.64], [33.58, -84.39], [33.75, -84.38], [33.91, -84.35], [34.87, -85.09],
      [35.05, -85.31], [35.86, -86.42], [36.08, -86.72], [36.15, -86.81], [36.25, -86.75],
      [36.97, -86.44], [37.00, -86.43], [37.71, -85.88], [38.24, -85.75], [38.25, -85.64],
      [38.70, -85.90], [39.22, -85.90], [39.64, -86.08], [39.64, -86.13], [39.78, -86.18],
      [39.91, -86.20], [40.08, -86.47], [40.40, -86.81], [40.77, -86.97], [41.17, -87.10],
      [41.47, -87.33], [41.60, -87.36], [41.63, -87.45], [41.72, -87.63], [41.77, -87.63],
      [41.87, -87.67], [41.89, -87.62], [42.27, -87.96], [42.38, -87.83], [42.57, -87.93],
      [42.73, -87.83], [42.99, -87.94], [43.04, -88.02], [43.78, -88.43], [44.01, -88.60],
      [44.25, -88.40], [44.28, -88.39]
    ]

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Mason's MedWay</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  
  <style>
    :root {{
      --bg: #0A0A0A;
      --surface: #111111;
      --surface-hover: #1A1A1A;
      --border: #1F1F1F;
      --text-primary: #F5F5F0;
      --text-secondary: #8A8A82;
      --text-muted: #4A4A45;
      --accent: #C8D96F;
      --danger: #E85D5D;
      --amber: #D4A54A;
      --success: #5DAE72;
      --route-glow: #C8D96F33;
    }}
    
    * {{ box-sizing: border-box; }}
    
    html {{ scroll-behavior: smooth; }}
    
    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text-secondary);
      margin: 0; padding: 0;
      overflow-x: hidden;
    }}

    nav {{
      position: fixed; top: 0; left: 0; width: 100%; padding: 20px 24px;
      z-index: 1000; transition: background 0.3s, border-color 0.3s;
      display: flex; justify-content: space-between; align-items: center;
      border-bottom: 1px solid transparent;
    }}
    nav.scrolled {{
      background: rgba(10, 10, 10, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }}
    nav .logo {{ color: var(--text-primary); text-transform: uppercase; letter-spacing: 3px; font-size: 13px; font-weight: 600; }}
    nav .status {{ display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--text-primary); font-weight: 500; }}
    nav .status .dot {{ width: 6px; height: 6px; background: var(--success); border-radius: 50%; box-shadow: 0 0 8px var(--success); opacity: 0; transition: opacity 0.3s; }}
    nav .status .dot.active {{ opacity: 1; }}

    section {{ padding: 120px 24px; max-width: 680px; margin: 0 auto; }}
    
    #hero {{ height: 100vh; width: 100vw; max-width: none; padding: 0; position: relative; }}
    #map {{ width: 100%; height: 100%; background: var(--bg); z-index: 1; }}
    .hero-overlay {{ position: absolute; bottom: 80px; left: 24px; z-index: 500; pointer-events: none; }}
    .hero-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: var(--accent); font-weight: 600; margin-bottom: 8px; }}
    .hero-title {{ font-size: clamp(40px, 10vw, 80px); font-weight: 700; color: var(--text-primary); margin: 0 0 12px 0; letter-spacing: -1.5px; line-height: 1; }}
    .hero-sub {{ font-size: 16px; color: var(--text-primary); font-weight: 400; }}
    
    .scroll-indicator {{
      position: absolute; bottom: 30px; left: 24px; z-index: 500;
      width: 1px; height: 40px; background: var(--border); overflow: hidden;
    }}
    .scroll-indicator::after {{
      content: ''; display: block; width: 100%; height: 50%;
      background: var(--text-primary); animation: scrollDown 2s infinite ease-in-out;
    }}
    @keyframes scrollDown {{ 0% {{ transform: translateY(-100%); }} 100% {{ transform: translateY(200%); }} }}

    .sec-num {{ font-family: monospace; color: var(--text-muted); font-size: 13px; margin-bottom: 24px; display: block; letter-spacing: 1px; font-weight: 500; }}
    h2 {{ font-size: clamp(32px, 8vw, 48px); color: var(--text-primary); margin: 0 0 16px 0; font-weight: 600; letter-spacing: -1px; line-height: 1.1; }}
    p.sec-desc {{ font-size: 16px; line-height: 1.6; color: var(--text-secondary); margin-bottom: 48px; max-width: 480px; }}

    .dash-cards {{ display: flex; flex-direction: column; gap: 16px; }}
    .dash-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; transition: background 0.3s; }}
    .dash-card label {{ display: block; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 8px; font-weight: 600; }}
    .dash-card .val {{ font-size: 24px; color: var(--text-primary); font-weight: 500; letter-spacing: -0.5px; }}

    #gps-banner {{ display: none; background: var(--border); color: var(--text-primary); padding: 24px; border-radius: 12px; font-weight: 500; line-height: 1.5; }}
    
    #list-container {{ display: flex; flex-direction: column; gap: 24px; }}
    .h-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 32px; transition: transform 0.3s, background 0.3s; }}
    .h-card:hover {{ background: var(--surface-hover); }}
    
    .h-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }}
    .h-title {{ font-size: 20px; color: var(--text-primary); font-weight: 600; line-height: 1.3; width: 75%; margin: 0; }}
    .badge {{ background: var(--border); color: var(--text-primary); padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; letter-spacing: 1px; }}
    
    .meta {{ font-size: 14px; margin-bottom: 32px; display: flex; flex-direction: column; gap: 8px; }}
    .meta-row {{ display: flex; align-items: center; gap: 8px; }}
    .dot-rating {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}
    .dot-green {{ background: var(--success); box-shadow: 0 0 8px var(--success); }}
    .dot-amber {{ background: var(--amber); box-shadow: 0 0 8px var(--amber); }}
    .dot-red {{ background: var(--danger); box-shadow: 0 0 8px var(--danger); }}
    .dist {{ color: var(--accent); font-weight: 500; font-family: monospace; font-size: 13px; }}

    .actions {{ display: flex; gap: 12px; }}
    .btn {{
      flex: 1; padding: 18px; border-radius: 12px; text-align: center; text-decoration: none; 
      font-size: 15px; font-weight: 500; transition: all 0.2s; display: block;
    }}
    .btn-primary {{ background: var(--text-primary); color: var(--bg); }}
    .btn-primary:hover {{ background: #fff; transform: translateY(-2px); }}
    .btn-secondary {{ background: transparent; color: var(--text-primary); border: 1px solid var(--border); }}
    .btn-secondary:hover {{ border-color: var(--text-muted); background: rgba(255,255,255,0.05); transform: translateY(-2px); }}

    .qa-btn {{
      display: flex; align-items: center; gap: 16px; padding: 32px; margin-bottom: 16px;
      background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
      color: var(--text-primary); text-decoration: none; font-size: 20px; font-weight: 500;
      transition: all 0.3s;
    }}
    .qa-btn span.icon {{ font-size: 24px; }}
    .qa-btn:hover {{ background: var(--surface-hover); transform: translateY(-4px); }}
    .qa-btn.danger {{ border-color: rgba(232, 93, 93, 0.3); color: var(--danger); }}
    .qa-btn.danger:hover {{ background: rgba(232, 93, 93, 0.1); border-color: var(--danger); }}

    footer {{ padding: 80px 24px; border-top: 1px solid var(--border); max-width: 680px; margin: 0 auto; }}
    footer .logo {{ color: var(--text-primary); text-transform: uppercase; letter-spacing: 2px; font-size: 13px; font-weight: 600; margin-bottom: 16px; }}
    footer .sub {{ font-size: 15px; margin-bottom: 16px; color: var(--text-secondary); font-weight: 400; }}
    footer .disclaimer {{ font-size: 12px; color: var(--text-muted); line-height: 1.5; }}
    
    @media (min-width: 600px) {{
      .dash-cards {{ flex-direction: row; gap: 16px; }}
      .dash-card {{ flex: 1; }}
    }}
  </style>
</head>
<body>

  <nav id="navbar">
    <div class="logo">Mason's MedWay</div>
    <div class="status">
      <div class="dot" id="nav-dot"></div>
      <span id="nav-status">Locating...</span>
    </div>
  </nav>

  <section id="hero">
    <div id="map"></div>
    <div class="hero-overlay animate-in">
      <div class="hero-label">Live Route Tracker</div>
      <h1 class="hero-title">Mason's MedWay</h1>
      <div class="hero-sub">Lake Belvedere Estates, FL → Appleton, WI</div>
    </div>
    <div class="scroll-indicator"></div>
  </section>

  <section id="s001">
    <span class="sec-num">001 · LIVE STATUS</span>
    <h2 class="animate-in">Know what's ahead.</h2>
    <p class="sec-desc animate-in">Real-time tracking along the I-75/I-41 corridor.</p>
    
    <div id="gps-banner" class="animate-in">
      Enable location services to track your route. Currently showing all facilities along the corridor.
    </div>

    <div class="dash-cards animate-in" id="dash-visible">
      <div class="dash-card">
        <label>Current Location</label>
        <div class="val" id="val-loc">Detecting...</div>
      </div>
      <div class="dash-card">
        <label>Next Hospital</label>
        <div class="val" id="val-next">-</div>
      </div>
      <div class="dash-card">
        <label>Facilities Ahead</label>
        <div class="val" id="val-count">0</div>
      </div>
    </div>
  </section>

  <section id="s002">
    <span class="sec-num">002 · UPCOMING HOSPITALS</span>
    <h2 class="animate-in">Hospitals on your route.</h2>
    <p class="sec-desc animate-in">Only showing facilities ahead of you, within 5 miles of the highway. Updated live.</p>
    
    <div id="list-container" class="stagger-group">
      <!-- Injected by JS -->
    </div>
  </section>

  <section id="s003">
    <span class="sec-num">003 · QUICK ACTIONS</span>
    <h2 class="animate-in">In an emergency.</h2>
    <p class="sec-desc animate-in">Immediate actions tailored to your current location.</p>
    
    <div class="animate-in stagger-group">
      <a href="tel:911" class="qa-btn danger">
        <span class="icon">🚨</span> Call 911
      </a>
      <a href="https://www.google.com/maps/search/hospitals+near+me" target="_blank" class="qa-btn">
        <span class="icon">📍</span> Navigation to Nearest Hospital
      </a>
      <a href="#s002" class="qa-btn">
        <span class="icon">📋</span> View All Hospitals Ahead
      </a>
    </div>
  </section>

  <footer>
    <div class="logo animate-in">Mason's MedWay</div>
    <div class="sub animate-in">I-75 / I-41 Corridor · 67 Facilities · All Open 24H</div>
    <div class="disclaimer animate-in">
      Ratings from Google Reviews. In an emergency, always call 911.<br><br>
      © 2026 Mason's MedWay. All rights reserved.
    </div>
  </footer>

  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  
  <script>
    const HOSPITALS = {json.dumps(hospitals)};
    const WAYPOINTS = {json.dumps(waypoints)};
    const ROUTE_DIST_MILES = 1550;

    // --- GSAP Setup ---
    gsap.registerPlugin(ScrollTrigger);

    window.addEventListener('scroll', () => {{
      const nav = document.getElementById('navbar');
      if (window.scrollY > 50) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    }});

    function initAnimations() {{
      gsap.utils.toArray('.animate-in').forEach(el => {{
        gsap.from(el, {{
          y: 40, opacity: 0, duration: 0.8, ease: 'power2.out',
          scrollTrigger: {{ trigger: el, start: 'top 85%', toggleActions: 'play none none none' }}
        }});
      }});
    }}

    // --- Map Setup ---
    const map = L.map('map', {{ zoomControl: false, scrollWheelZoom: false }}).setView([26.72, -80.05], 6);
    L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
      maxZoom: 19, attribution: '&copy; CartoDB'
    }}).addTo(map);

    const routeLine = L.polyline(WAYPOINTS, {{ color: 'var(--accent)', weight: 3, opacity: 0.5 }}).addTo(map);
    map.fitBounds(routeLine.getBounds());

    const userIcon = L.divIcon({{
      className: 'custom-div-icon',
      html: "<div style='background-color: var(--success); width: 14px; height: 14px; border-radius: 50%; box-shadow: 0 0 16px var(--success); border: 2px solid var(--surface);'></div>",
      iconSize: [14, 14], iconAnchor: [7, 7]
    }});

    const hospitalIcon = L.divIcon({{
      className: 'custom-div-icon',
      html: "<div style='background-color: var(--text-secondary); width: 6px; height: 6px; border-radius: 50%; box-shadow: 0 0 4px rgba(255,255,255,0.2);'></div>",
      iconSize: [6, 6], iconAnchor: [3, 3]
    }});

    const userMarker = L.marker([0, 0], {{ icon: userIcon }});
    let hospitalMarkers = [];

    // Precalculate route progress
    let routeSegments = [];
    let totalDist = 0;
    for (let i = 0; i < WAYPOINTS.length - 1; i++) {{
      const p1 = L.latLng(WAYPOINTS[i]);
      const p2 = L.latLng(WAYPOINTS[i+1]);
      const d = map.distance(p1, p2);
      routeSegments.push({{ p1, p2, dist: d, cum: totalDist }});
      totalDist += d;
    }}

    function projectPoint(p, a, b) {{
      const atob = {{ lat: b.lat - a.lat, lng: b.lng - a.lng }};
      const atop = {{ lat: p.lat - a.lat, lng: p.lng - a.lng }};
      const len2 = atob.lat * atob.lat + atob.lng * atob.lng;
      if (len2 === 0) return 0;
      let dot = (atop.lat * atob.lat + atop.lng * atob.lng) / len2;
      return Math.max(0, Math.min(1, dot));
    }}

    function getProgress(latlng) {{
      let minD = Infinity;
      let bestP = 0;
      for (let s of routeSegments) {{
        const t = projectPoint(latlng, s.p1, s.p2);
        const pLat = s.p1.lat + t * (s.p2.lat - s.p1.lat);
        const pLng = s.p1.lng + t * (s.p2.lng - s.p1.lng);
        const projL = L.latLng(pLat, pLng);
        const dSeg = map.distance(latlng, projL);
        if (dSeg < minD) {{
          minD = dSeg;
          const dAlong = map.distance(s.p1, projL);
          bestP = (s.cum + dAlong) / totalDist;
        }}
      }}
      return {{ p: bestP, distToRoute: minD }};
    }}

    HOSPITALS.forEach((h, i) => {{
      const ll = L.latLng(h.lat, h.lng);
      h.progressInfo = getProgress(ll);
      h.id = 'h_' + i;
      h.marker = L.marker(ll, {{ icon: hospitalIcon }});
    }});

    let userLat = null, userLng = null;
    let gpsDenied = false;
    let currentVisibleIds = '';

    function renderList(visible) {{
      const newIds = visible.map(h => h.id).join(',');
      const c = document.getElementById('list-container');
      
      // Update markers
      hospitalMarkers.forEach(m => map.removeLayer(m));
      hospitalMarkers = [];
      visible.forEach(h => {{
        h.marker.addTo(map);
        hospitalMarkers.push(h.marker);
      }});

      if (newIds === currentVisibleIds) {{
        // Just update text content on existing blocks
        visible.forEach(h => {{
          const el = document.getElementById(h.id);
          if (el && h.distAhead !== undefined) {{
            const distEl = el.querySelector('.dist');
            if (distEl) distEl.innerText = `+ ${{Math.round(h.distAhead)}} MI AHEAD`;
          }}
        }});
        return;
      }}
      
      // Rebuild DOM if list changed
      currentVisibleIds = newIds;
      c.innerHTML = '';
      
      visible.forEach(h => {{
        const rClass = h.rating >= 4.0 ? 'dot-green' : (h.rating >= 3.0 ? 'dot-amber' : 'dot-red');
        const distText = h.distAhead !== undefined 
            ? `<div class="dist">+ ${{Math.round(h.distAhead)}} MI AHEAD</div>` 
            : `<div class="dist">N/A</div>`;
            
        const div = document.createElement('div');
        div.className = 'h-card';
        div.id = h.id;
        div.innerHTML = `
          <div class="h-header">
            <h3 class="h-title">${{h.name}}</h3>
            <div class="badge">24H</div>
          </div>
          <div class="meta">
            ${{distText}}
            <div class="meta-row">
              <span class="dot-rating ${{rClass}}"></span> ${{h.rating}} ★ • ${{h.city}}, ${{h.state}}
            </div>
          </div>
          <div class="actions">
            <a href="https://www.google.com/maps/dir/?api=1&destination=${{h.lat}},${{h.lng}}&travelmode=driving" target="_blank" class="btn btn-primary">Get Directions</a>
            <a href="tel:${{h.phone}}" class="btn btn-secondary">Call</a>
          </div>
        `;
        c.appendChild(div);
      }});

      // Trigger GSAP on new elements
      gsap.from(c.children, {{
        y: 40, opacity: 0, duration: 0.6, stagger: 0.1, ease: 'power2.out',
        scrollTrigger: {{ trigger: c, start: 'top 85%', toggleActions: 'play none none none' }}
      }});
      ScrollTrigger.refresh();
    }}

    function updateDashboard(visible) {{
      if (gpsDenied) {{
        document.getElementById('dash-visible').style.display = 'none';
        document.getElementById('gps-banner').style.display = 'block';
        return;
      }}
      
      document.getElementById('dash-visible').style.display = 'flex';
      document.getElementById('gps-banner').style.display = 'none';
      
      document.getElementById('val-count').innerText = visible.length;
      if (visible.length > 0) {{
        document.getElementById('val-next').innerText = visible[0].name;
      }} else {{
        document.getElementById('val-next').innerText = 'None';
      }}
    }}

    function update() {{
      if (gpsDenied) {{
        renderList(HOSPITALS);
        updateDashboard(HOSPITALS);
        return;
      }}
      if (userLat === null) return;
      
      const ul = L.latLng(userLat, userLng);
      const userProg = getProgress(ul).p;
      
      let visible = [];
      HOSPITALS.forEach(h => {{
        if (h.progressInfo.p > userProg - 0.006) {{
          h.distAhead = (h.progressInfo.p - userProg) * ROUTE_DIST_MILES;
          if (h.distAhead < 0) h.distAhead = 0;
          visible.push(h);
        }}
      }});
      visible.sort((a,b) => a.progressInfo.p - b.progressInfo.p);
      
      renderList(visible);
      updateDashboard(visible);
    }}

    let lastStateTime = 0;
    function detectState(lat, lon) {{
      const now = Date.now();
      if (now - lastStateTime < 30000) return;
      lastStateTime = now;
      fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${{lat}}&lon=${{lon}}`)
        .then(r => r.json())
        .then(data => {{
          if (data && data.address && data.address.state) {{
            document.getElementById('nav-status').innerText = 'In ' + data.address.state;
            document.getElementById('val-loc').innerText = data.address.city + ', ' + data.address.state;
          }} else {{
          	document.getElementById('nav-status').innerText = 'Location Found';
            document.getElementById('val-loc').innerText = 'Tracking active';
          }}
        }}).catch(() => {{ 
          document.getElementById('nav-status').innerText = 'Location Found'; 
          document.getElementById('val-loc').innerText = 'Tracking active';
        }});
    }}

    // Initial default render
    initAnimations();
    renderList(HOSPITALS);

    // Geolocation setup
    navigator.geolocation.watchPosition(pos => {{
      userLat = pos.coords.latitude;
      userLng = pos.coords.longitude;
      
      if (!map.hasLayer(userMarker)) userMarker.addTo(map);
      userMarker.setLatLng([userLat, userLng]);
      
      document.getElementById('nav-dot').classList.add('active');
      
      detectState(userLat, userLng);
      update();
    }}, err => {{
      console.error("GPS Error:", err);
      gpsDenied = true;
      document.getElementById('nav-dot').classList.remove('active');
      document.getElementById('nav-status').innerText = 'GPS Disabled';
      update();
    }}, {{ enableHighAccuracy: true, maximumAge: 10000 }});

  </script>
</body>
</html>'''

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()
