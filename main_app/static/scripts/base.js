$('#login').click((event) => {
    $('#panel1').addClass('active');
    $('#panel1').addClass('show');
    $('#panel2').removeClass('active');
    $('#panel2').removeClass('show');
    $('#login-link').addClass('active');
    $('#signup-link').removeClass('active');
});

$('#signup').click((event) => {
    $('#panel1').removeClass('active');
    $('#panel1').removeClass('show');
    $('#panel2').addClass('active');
    $('#panel2').addClass('show');
    $('#login-link').removeClass('active');
    $('#signup-link').addClass('active');
});

// https://stackoverflow.com/a/5448635
const getSearchParameters = () => {
    var prmstr = window.location.search.substr(1);
    return prmstr != null && prmstr != "" ? transformToAssocArray(prmstr) : {};
}

const transformToAssocArray = (prmstr) => {
    var params = {};
    var prmarr = prmstr.split("&");
    for (var i = 0; i < prmarr.length; i++) {
        var tmparr = prmarr[i].split("=");
        params[tmparr[0]] = tmparr[1];
    }
    return params;
}

var params = getSearchParameters();

if (params.registration && params.registration === 'fail') {
    $('#signup').click();
    $('#registration-error').removeClass('hidden');
}

if (params.login && params.login === 'fail') {
    $('#login').click();
    $('#login-error').removeClass('hidden');
}
