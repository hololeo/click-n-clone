javascript:(function(){
    var serverUrl = 'http://127.0.0.1:5000/clone';
    var currentUrl = window.location.href;
    var repoUrl;
    // Check for GitHub repository
    var githubMatch = currentUrl.match(/^https?:\/\/github\.com\/([^\/]+\/[^\/]+)/);
    if (githubMatch) {
        repoUrl = 'https://github.com/' + githubMatch[1] + '.git';
    } 
    // Check for Hugging Face space
    else if (currentUrl.startsWith('https://huggingface.co/spaces/')) {
        repoUrl = currentUrl;
    }
    if (repoUrl) {
        window.location.href = serverUrl + '?url=' + encodeURIComponent(repoUrl);
    } else {
        alert('This doesn\'t appear to be a GitHub repository or Hugging Face space page.');
    }
})();
// use with bookmarklet maker https://caiorss.github.io/bookmarklet-maker/
