/**
 * GERELTJIN LLC - Footer Map
 * Shows Office, Factory, and Sports Complex locations
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Check if map element exists
    const mapElement = document.getElementById('footer-map');
    if (!mapElement) return;
    
    // ============================================
    // LOCATION COORDINATES
    // TODO: Replace with actual coordinates
    // ============================================
    const locations = {
        office: {
            lat: 47.936471687835116, // Office location (example: central UB)
            lng: 106.92518850713871,
            title: getTranslation('Office'),
            address: getTranslation('Main Office Address'),
            icon: '🏢'
        },
        factory: {
            lat: 47.91507269051517,  // Factory location (example: industrial area)
            lng: 107.03074946593156,
            title: getTranslation('Factory'),
            address: getTranslation('Glass Production Facility'),
            icon: '🏭'
        },
        sports: {
            lat: 47.93576147505511,  // Sports complex (example)
            lng: 106.92260089785793,
            title: getTranslation('Sports Complex'),
            address: getTranslation('Sports Hall Facility'),
            icon: '🏀'
        }
    };
    
    // ============================================
    // Initialize Map
    // ============================================
    const map = L.map('footer-map', {
        scrollWheelZoom: false,
        dragging: true,
        touchZoom: true,
        doubleClickZoom: true,
        zoomControl: true
    }).setView([47.9184, 106.9177], 12); // Center on Ulaanbaatar
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);
    
    // ============================================
    // Custom Icon Function
    // ============================================
    const markerCluster = L.markerClusterGroup({
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: false,
        zoomToBoundsOnClick: true,
        maxClusterRadius: 40
    });

    function createCustomIcon(emoji) {
        return L.divIcon({
            html: `<div class="custom-marker">${emoji}</div>`,
            className: 'custom-marker-wrapper',
            iconSize: [40, 40],
            iconAnchor: [20, 40],
            popupAnchor: [0, -40]
        });
    }
    
    // ============================================
    // Add Markers
    // ============================================
    
    // Office Marker
    const officeMarker = L.marker([locations.office.lat, locations.office.lng], {
        icon: createCustomIcon(locations.office.icon)
    });
    
    officeMarker.bindPopup(`
        <div class="map-popup">
            <h4>${locations.office.title}</h4>
            <p>${locations.office.address}</p>
            <a href="https://www.google.com/maps?q=${locations.office.lat},${locations.office.lng}" target="_blank" class="map-link">
                ${getTranslation('Get Directions')} →
            </a>
        </div>
    `);
    markerCluster.addLayer(officeMarker);
    
    // Factory Marker
    const factoryMarker = L.marker([locations.factory.lat, locations.factory.lng], {
        icon: createCustomIcon(locations.factory.icon)
    });
    
    factoryMarker.bindPopup(`
        <div class="map-popup">
            <h4>${locations.factory.title}</h4>
            <p>${locations.factory.address}</p>
            <a href="https://www.google.com/maps?q=${locations.factory.lat},${locations.factory.lng}" target="_blank" class="map-link">
                ${getTranslation('Get Directions')} →
            </a>
        </div>
    `);
    
    markerCluster.addLayer(factoryMarker);
    
    // Sports Complex Marker
    const sportsMarker = L.marker([locations.sports.lat, locations.sports.lng], {
        icon: createCustomIcon(locations.sports.icon)
    }); 
    
    sportsMarker.bindPopup(`
        <div class="map-popup">
            <h4>${locations.sports.title}</h4>
            <p>${locations.sports.address}</p>
            <a href="https://www.google.com/maps?q=${locations.sports.lat},${locations.sports.lng}" target="_blank" class="map-link">
                ${getTranslation('Get Directions')} →
            </a>
        </div>
    `);

    markerCluster.addLayer(sportsMarker);
    
    map.addLayer(markerCluster);
    // ============================================
    // Fit map to show all markers
    // ============================================
    // const group = L.featureGroup([officeMarker, factoryMarker, sportsMarker]);
    // map.fitBounds(group.getBounds().pad(0.1));
    map.fitBounds(markerCluster.getBounds(), {
        padding: [20, 20]
    });
    
    // ============================================
    // Translation Helper (basic)
    // ============================================
    function getTranslation(key) {
        const lang = document.documentElement.lang || 'en';
        
        const translations = {
            'Office': lang === 'mn' ? 'Оффис' : 'Office',
            'Factory': lang === 'mn' ? 'Үйлдвэр' : 'Factory',
            'Sports Complex': lang === 'mn' ? 'Спорт цогцолбор' : 'Sports Complex',
            'Main Office Address': lang === 'mn' ? 'Төв оффисын хаяг' : 'Main Office Address',
            'Glass Production Facility': lang === 'mn' ? 'Шил боловсруулах үйлдвэр' : 'Glass Production Factory',
            'Sports Hall Facility': lang === 'mn' ? 'Спортын заал' : 'Sports Hall',
            'Get Directions': lang === 'mn' ? 'Чиглэл авах' : 'Get Directions'
        };
        
        return translations[key] || key;
    }
    
    // ============================================
    // Resize map on window resize
    // ============================================
    window.addEventListener('resize', function() {
        setTimeout(function() {
            map.invalidateSize();
        }, 100);
    });
});
