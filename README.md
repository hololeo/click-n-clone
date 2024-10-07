# Click 'n' Clone 
A bookmarklet for rapid repo cloning. Just click and clone!

<img src="https://github.com/user-attachments/assets/da26d168-89b0-4779-af73-3a67e02c41ad" width="150">


### Quickly Clone GitHub Repo with Bookmarklet

To quickly clone a GitHub repository, follow these steps:

1. **First, run the server**:
   - Run the following command to start the server:
     ```bash
     python server.py
     ```
   This starts a local server on port 5000 that will handle the repository cloning.

    **Note:** The cloned repository will be placed in directory 'github_clones' in the same directory where the server script is run.

3. **Set up the bookmarklet**:
   - Copy the code below.
   - Create a new bookmark in your browser.
   - Paste the copied code into the bookmark's URL field.
     
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
// use with bookmarklet maker https://caiorss.github.io/bookmarklet-maker/
```

4. **Using the bookmarklet**:
   - Once the server is running and you've added the bookmarklet, go to any GitHub repository page.
   - Click the bookmark to clone the repo.
   - The repo will be cloned in directory **'github_clones'** relative to the server.py script
   - Once complete, the browser will show a tree output of the files.
   - <img src="https://github.com/user-attachments/assets/c2fa83ff-8d82-477e-8788-9273449da990" width="300">


**Note:** Developed and tested only on MacOSX.

