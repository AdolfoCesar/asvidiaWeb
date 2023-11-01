let mapDevol = L.map('mapDevol').setView([40.463667,-3.74922],6)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyrigth">OpenStreetMap</a> contributors'
}).addTo(mapDevol);

document.getElementById('select-location').addEventListener('change', function(e){
    let coords =e.target.value.split(",");
    mapDevol.flyTo(coords,13);
})

var carto_ligth = L.tileLayer('https://{s}.basemaps.cartocdn.com/ligth_all/{z}/{x}/{y}{r}.png', {attribution: '©OpenStreetMap, ©CartoDB',subdomains:'abcd',maxZoom:24});

var minimap = new L.Control.minimap(carto_ligth,
    {
        toggleDisplay: true,
        minimized: false,
        position: "bottomleft"
    }).addTo(mapDevol);

new L.Control.scale({imperial:false}).addTo(mapDevol);