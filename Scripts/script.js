function get_inurl_vars(){
    var vars = {};
    document.referrer.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m, key, value) {
        vars[key] = decodeURI(value);
    });
    return vars;
}

// &key=QWxsaW5DYWxs