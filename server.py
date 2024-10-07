import os
import subprocess
from flask import Flask, request  # pip install Flask
import argparse
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory where repositories will be cloned
CLONE_DIR = os.path.expanduser("./github_clones")

def get_directory_size(directory):
    """Calculate the total size of the directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Check if the file exists to avoid errors
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

@app.route('/clone', methods=['GET'])
def clone_repo():
    logger.info("Received new clone request")

    repo_url = request.args.get('url')
    if not repo_url:
        logger.error("No URL provided")
        return "Error: No URL provided", 400

    logger.info(f"Attempting to clone repository: {repo_url}")

    # Create the clone directory if it doesn't exist
    os.makedirs(CLONE_DIR, exist_ok=True)

    # Extract repo name from URL
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    clone_path = os.path.join(CLONE_DIR, repo_name)

    try:
        # Clone the repository
        subprocess.run(['git', 'clone', repo_url, clone_path], check=True, capture_output=True, text=True)
        logger.info(f"Successfully cloned {repo_url} to {clone_path}")

        # Run the tree command
        tree_output = subprocess.run(['tree', clone_path], check=True, capture_output=True, text=True)
        logger.info("Successfully retrieved directory structure")

        # Calculate the total size of the cloned repository
        total_size_bytes = get_directory_size(clone_path)
        total_size_mb = total_size_bytes / (1024 * 1024)  # Convert to MB

        # Format output in <pre> tags for HTML
        summary = f"<pre>Total size: {total_size_mb:.2f} MB\n{tree_output.stdout}\n</pre>"
        return summary, 200

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to clone repository: {e.stderr}")
        return f"Error cloning repository: {e.stderr}", 500

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Click 'n Clone Server")
    parser.add_argument('--port', type=int, default=5000, help="Port to run the server on")
    args = parser.parse_args()

    logger.info(f"Starting Click 'n Clone server on port {args.port}")
    app.run(host='0.0.0.0', port=args.port)
