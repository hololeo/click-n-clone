# Click 'n' Clone 
A bookmarklet for rapid repo cloning.


### Quickly Clone GitHub Repo with Bookmarklet

To quickly clone a GitHub repository, follow these steps:

1. **First, run the server**:
   - Run the following command to start the server:
     ```bash
     python server.py
     ```
   This starts a local server on port 5000 that will handle the repository cloning.

2. **Set up the bookmarklet**:
   - Copy the code below.
   - Create a new bookmark in your browser.
   - Paste the copied code into the bookmark's URL field.

3. **Using the bookmarklet**:
   - Once the server is running and you've added the bookmarklet, go to any GitHub repository page.
   - Click the bookmark to clone the repo.

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

