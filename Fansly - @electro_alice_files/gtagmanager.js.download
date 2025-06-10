var path = window && window.location ? window.location.pathname || "" : "";
if (path.indexOf('/passwordreset/') === -1 && path.indexOf('/managementsession/claim') === -1 && path.indexOf('/thirdpartyconnect/login') === -1) {
    var onLoadCallback = function () {
        //window.dataLayer = window.dataLayer || [];
        if (!window.dataLayer || typeof window.dataLayer.push !== "function") {
            return;
        }
        
        function gtag() { dataLayer.push(arguments); }
    
        gtag('js', new Date());
        gtag('config', 'G-BZSVNWD5W8');
     
     
    };
    
    (function (w, d, s, l, i, onLoadCallback) {
        w[l] = w[l] || []; w[l].push({
            'gtm.start':
                new Date().getTime(), event: 'gtm.js'
        }); var f = d.getElementsByTagName(s)[0],
            j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.onload = onLoadCallback; j.async = true; j.src =
                'https://www.googletagmanager.com/gtm.js?ngsw-bypass=true&id=' + i + dl; f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-WG8ZFQG', onLoadCallback);
}