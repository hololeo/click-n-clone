javascript:(function(){
    var serverUrl = 'http://127.0.0.1:5000/clone';
    var currentUrl = window.location.href;
    var match = currentUrl.match(/^https?:\/\/github\.com\/([^\/]+\/[^\/]+)/);
    if (match) {
        var repoUrl = 'https://github.com/' + match[1] + '.git';
        window.location.href = serverUrl + '?url=' + encodeURIComponent(repoUrl);
    } else {
        alert('This doesn\'t appear to be a GitHub repository page.');
    }
})();
