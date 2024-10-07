# Click 'n' Clone 
A bookmarklet for rapid repo cloning.


### Clone GitHub Repo Bookmarklet

To quickly clone a GitHub repository, follow these steps:

1. Copy the code below.
2. Create a new bookmark in your browser.
3. Paste the copied code into the bookmark's URL field.
4. Now, when you're on a GitHub repository page, click the bookmark to clone it.

```javascript
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
```

