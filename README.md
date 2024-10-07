# Click 'n' Clone 
A bookmarklet for rapid repo cloning.

Drag this link to your bookmarks bar

[gitclone](javascript:(function(){var%20serverUrl%20=%20'http://127.0.0.1:5000/clone';var%20currentUrl%20=%20window.location.href;var%20match%20=%20currentUrl.match(/^https?:\/\/github\.com\/([^\/]+\/[^\/]+)/);if%20(match){var%20repoUrl%20=%20'https://github.com/'%20+%20match[1]%20+%20'.git';window.location.href%20=%20serverUrl%20+%20'?url='%20+%20encodeURIComponent(repoUrl);}else{alert('This%20doesn\'t%20appear%20to%20be%20a%20GitHub%20repository%20page.');}})())

