from flask.templating import render_template
from app import app

@app.route('/')
def index():
    cities = ['new-york-ny', 'los-angeles-ca', 'chicago-il', 'houston-tx', 'philadelphia-pa', 'phoenix-az', 'san-antonio-tx', 'san-diego-ca', 'dallas-tx', 'san-jose-ca', 'austin-tx', 'indianapolis-in', 'jacksonville-fl', 'san-francisco-ca', 'columbus-oh', 'charlotte-nc', 'fort-worth-tx', 'detroit-mi', 'el-paso-tx', 'memphis-tn', 'seattle-wa', 'denver-co', 'washington-dc', 'boston-ma', 'nashville-davidson-tn', 'baltimore-md', 'oklahoma-city-ok', 'louisville-ky', 'jefferson-county-ky', 'portland-or', 'las-vegas-nv', 'milwaukee-wi', 'albuquerque-nm', 'tucson-az', 'fresno-ca', 'sacramento-ca', 'long-beach-ca', 'kansas-city-mo', 'mesa-az', 'virginia-beach-va', 'atlanta-ga', 'colorado-springs-co', 'omaha-ne', 'raleigh-nc', 'miami-fl', 'oakland-ca', 'minneapolis-mn', 'tulsa-ok', 'cleveland-oh', 'wichita-ks', 'arlington-tx', 'new-orleans-la', 'bakersfield-ca', 'tampa-fl', 'honolulu-hi', 'aurora-co', 'anaheim-ca', 'santa-ana-ca', 'st.-louis-mo', 'riverside-ca', 'corpus-christi-tx', 'lexington-fayette-ky', 'pittsburgh-pa', 'anchorage-ak', 'stockton-ca', 'cincinnati-oh', 'st.-paul-mn', 'toledo-oh', 'greensboro-nc', 'newark-nj', 'plano-tx', 'henderson-nv', 'lincoln-ne', 'buffalo-ny', 'jersey-city-nj', 'chula-vista-ca', 'fort-wayne-in', 'orlando-fl', 'st.-petersburg-fl', 'chandler-az', 'laredo-tx', 'norfolk-va', 'durham-nc', 'madison-wi', 'lubbock-tx', 'irvine-ca', 'winston-salem-nc', 'glendale-az', 'garland-tx', 'hialeah-fl', 'reno-nv', 'chesapeake-va', 'gilbert-az', 'baton-rouge-la', 'irving-tx', 'scottsdale-az', 'north-las-vegas-nv', 'fremont-ca', 'boise-city-id', 'richmond-va', 'san-bernardino-ca', 'birmingham-al', 'spokane-wa', 'rochester-ny', 'des-moines-ia', 'modesto-ca', 'fayetteville-nc', 'tacoma-wa', 'oxnard-ca', 'fontana-ca', 'columbus-ga', 'montgomery-al', 'moreno-valley-ca', 'shreveport-la', 'aurora-il', 'yonkers-ny', 'akron-oh', 'huntington-beach-ca', 'little-rock-ar', 'augusta-richmond-county-ga', 'amarillo-tx', 'glendale-ca', 'mobile-al', 'grand-rapids-mi', 'salt-lake-city-ut', 'tallahassee-fl', 'huntsville-al', 'grand-prairie-tx', 'knoxville-tn', 'worcester-ma', 'newport-news-va', 'brownsville-tx', 'overland-park-ks', 'santa-clarita-ca', 'providence-ri', 'garden-grove-ca', 'chattanooga-tn', 'oceanside-ca', 'jackson-ms', 'fort-lauderdale-fl', 'santa-rosa-ca', 'rancho-cucamonga-ca', 'port-st.-lucie-fl', 'tempe-az', 'ontario-ca', 'vancouver-wa', 'cape-coral-fl', 'sioux-falls-sd', 'springfield-mo', 'peoria-az', 'pembroke-pines-fl', 'elk-grove-ca', 'salem-or', 'lancaster-ca', 'corona-ca', 'eugene-or', 'palmdale-ca', 'salinas-ca', 'springfield-ma', 'pasadena-tx', 'fort-collins-co', 'hayward-ca', 'pomona-ca', 'cary-nc', 'rockford-il', 'alexandria-va', 'escondido-ca', 'mckinney-tx', 'kansas-city-ks', 'joliet-il', 'sunnyvale-ca', 'torrance-ca', 'bridgeport-ct', 'lakewood-co', 'hollywood-fl', 'paterson-nj', 'naperville-il', 'syracuse-ny', 'mesquite-tx', 'dayton-oh', 'savannah-ga', 'clarksville-tn', 'orange-ca', 'pasadena-ca', 'fullerton-ca', 'killeen-tx', 'frisco-tx', 'hampton-va', 'mcallen-tx', 'warren-mi', 'bellevue-wa', 'west-valley-city-ut', 'columbia-sc', 'olathe-ks', 'sterling-heights-mi', 'new-haven-ct', 'miramar-fl', 'waco-tx', 'thousand-oaks-ca', 'cedar-rapids-ia', 'charleston-sc', 'visalia-ca', 'topeka-ks', 'elizabeth-nj', 'gainesville-fl', 'thornton-co', 'roseville-ca', 'carrollton-tx', 'coral-springs-fl', 'stamford-ct', 'simi-valley-ca', 'concord-ca', 'hartford-ct', 'kent-wa', 'lafayette-la', 'midland-tx', 'surprise-az', 'denton-tx', 'victorville-ca', 'evansville-in', 'santa-clara-ca', 'abilene-tx', 'athens-clarke-county-ga', 'vallejo-ca', 'allentown-pa', 'norman-ok', 'beaumont-tx', 'independence-mo', 'murfreesboro-tn', 'ann-arbor-mi', 'springfield-il', 'berkeley-ca', 'peoria-il', 'provo-ut', 'el-monte-ca', 'columbia-mo', 'lansing-mi', 'fargo-nd', 'downey-ca', 'costa-mesa-ca', 'wilmington-nc', 'arvada-co', 'inglewood-ca', 'miami-gardens-fl', 'carlsbad-ca', 'westminster-co', 'rochester-mn', 'odessa-tx', 'manchester-nh', 'elgin-il', 'west-jordan-ut', 'round-rock-tx', 'clearwater-fl', 'waterbury-ct', 'gresham-or', 'fairfield-ca', 'billings-mt', 'lowell-ma', 'san-buenaventura-(ventura)-ca', 'pueblo-co', 'high-point-nc', 'west-covina-ca', 'richmond-ca', 'murrieta-ca', 'cambridge-ma', 'antioch-ca', 'temecula-ca', 'norwalk-ca', 'centennial-co', 'everett-wa', 'palm-bay-fl', 'wichita-falls-tx', 'green-bay-wi', 'daly-city-ca', 'burbank-ca', 'richardson-tx', 'pompano-beach-fl', 'north-charleston-sc', 'broken-arrow-ok', 'boulder-co', 'west-palm-beach-fl', 'santa-maria-ca', 'el-cajon-ca', 'davenport-ia', 'rialto-ca', 'las-cruces-nm', 'san-mateo-ca', 'lewisville-tx', 'south-bend-in', 'lakeland-fl', 'erie-pa', 'tyler-tx', 'pearland-tx', 'college-station-tx', 'kenosha-wi', 'sandy-springs-ga', 'clovis-ca', 'flint-mi', 'roanoke-va', 'albany-ny', 'jurupa-valley-ca', 'compton-ca', 'san-angelo-tx', 'hillsboro-or', 'lawton-ok', 'renton-wa', 'vista-ca', 'davie-fl', 'greeley-co', 'mission-viejo-ca', 'portsmouth-va', 'dearborn-mi', 'south-gate-ca', 'tuscaloosa-al', 'livonia-mi', 'new-bedford-ma', 'vacaville-ca', 'brockton-ma', 'roswell-ga', 'beaverton-or', 'quincy-ma', 'sparks-nv', 'yakima-wa', "lee's-summit-mo", 'federal-way-wa', 'carson-ca', 'santa-monica-ca', 'hesperia-ca', 'allen-tx', 'rio-rancho-nm', 'yuma-az', 'westminster-ca', 'orem-ut', 'lynn-ma', 'redding-ca', 'spokane-valley-wa', 'miami-beach-fl', 'league-city-tx', 'lawrence-ks', 'santa-barbara-ca', 'plantation-fl', 'sandy-ut', 'sunrise-fl', 'macon-ga', 'longmont-co', 'boca-raton-fl', 'san-marcos-ca', 'greenville-nc', 'waukegan-il', 'fall-river-ma', 'chico-ca', 'newton-ma', 'san-leandro-ca', 'reading-pa', 'norwalk-ct', 'fort-smith-ar', 'newport-beach-ca', 'asheville-nc', 'nashua-nh', 'edmond-ok', 'whittier-ca', 'nampa-id', 'bloomington-mn', 'deltona-fl', 'hawthorne-ca', 'duluth-mn', 'carmel-in', 'suffolk-va', 'clifton-nj', 'citrus-heights-ca', 'livermore-ca', 'tracy-ca', 'alhambra-ca', 'kirkland-wa', 'trenton-nj', 'ogden-ut', 'hoover-al', 'cicero-il', 'fishers-in', 'sugar-land-tx', 'danbury-ct', 'meridian-id', 'indio-ca', 'concord-nc', 'menifee-ca', 'champaign-il', 'buena-park-ca', 'troy-mi', "o'fallon-mo", 'johns-creek-ga', 'bellingham-wa', 'westland-mi', 'bloomington-in', 'sioux-city-ia', 'warwick-ri', 'hemet-ca', 'longview-tx', 'farmington-hills-mi', 'bend-or', 'lakewood-ca', 'merced-ca', 'mission-tx', 'chino-ca', 'redwood-city-ca', 'edinburg-tx', 'cranston-ri', 'parma-oh', 'new-rochelle-ny', 'lake-forest-ca', 'napa-ca', 'hammond-in', 'fayetteville-ar', 'bloomington-il', 'avondale-az', 'somerville-ma', 'palm-coast-fl', 'bryan-tx', 'gary-in', 'largo-fl', 'brooklyn-park-mn', 'tustin-ca', 'racine-wi', 'deerfield-beach-fl', 'lynchburg-va', 'mountain-view-ca', 'medford-or', 'lawrence-ma', 'bellflower-ca', 'melbourne-fl', 'st.-joseph-mo', 'camden-nj', 'st.-george-ut', 'kennewick-wa', 'baldwin-park-ca', 'chino-hills-ca', 'alameda-ca', 'albany-ga', 'arlington-heights-il', 'scranton-pa', 'evanston-il', 'kalamazoo-mi', 'baytown-tx', 'upland-ca', 'springdale-ar', 'bethlehem-pa', 'schaumburg-il', 'mount-pleasant-sc', 'auburn-wa', 'decatur-il', 'san-ramon-ca', 'pleasanton-ca', 'wyoming-mi', 'lake-charles-la', 'plymouth-mn', 'bolingbrook-il', 'pharr-tx', 'appleton-wi', 'gastonia-nc', 'folsom-ca', 'southfield-mi', 'rochester-hills-mi', 'new-britain-ct', 'goodyear-az', 'canton-oh', 'warner-robins-ga', 'union-city-ca', 'perris-ca', 'manteca-ca', 'iowa-city-ia', 'jonesboro-ar', 'wilmington-de', 'lynwood-ca', 'loveland-co', 'pawtucket-ri', 'boynton-beach-fl', 'waukesha-wi', 'gulfport-ms', 'apple-valley-ca', 'passaic-nj', 'rapid-city-sd', 'layton-ut', 'lafayette-in', 'turlock-ca', 'muncie-in', 'temple-tx', 'missouri-city-tx', 'redlands-ca', 'santa-fe-nm', 'lauderhill-fl', 'milpitas-ca', 'palatine-il', 'missoula-mt', 'rock-hill-sc', 'jacksonville-nc', 'franklin-tn', 'flagstaff-az', 'flower-mound-tx', 'weston-fl', 'waterloo-ia', 'union-city-nj', 'mount-vernon-ny']
    return render_template('index.html', total_cities = len(cities) ,cities = cities)