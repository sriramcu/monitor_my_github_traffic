# Analyze GitHub Traffic For All Repositories at Once

Have you ever wanted to check the traffic on ALL your repositiories, but were too lazy to click on insights after manually navigating to all your repos? Well, now I've written a program that will open the traffic graphs for all your repos simulataneously, saving you the hassle of clicking a million times. All you have to do is run the program.

This project provides a simple program to monitor the traffic in terms of 
 views on each of my GitHub 
 repositories by opening each repo's traffic insights 
 page in a browser window. 
 
It uses the GitHub API to retrieve a list of repositories for a given username and 
token. It then opens each repository's traffic page in Google Chrome.

## Setup and Requirements
1. Python 3.x
2. `pip install -r requirements.txt`
3. Google Chrome installed on your system
4. Environment Variables (in an .env file in the project root)-  
   1. GITHUB_TOKEN: a valid GitHub token with repository read access
   2. GITHUB_USERNAME: the GitHub username to retrieve repositories for
   3. CHROME_PATH: the path to the Google Chrome executable on your system

## Usage

Run the script using   
`python check_traffic.py`
   
## How it Works

The script loads the environment variables from the .env file using dotenv.
It uses the github library to retrieve a list of repositories for the given username and token.
It registers Google Chrome as the default browser using webbrowser.
It opens each repository's traffic page in Google Chrome using webbrowser.
The reason we don't use the GitHub API and instead open the traffic page in the 
browser is to utilize the intuitive insights/ traffic GUI provided by GitHub instead of 
trying to render it via 
code in this project. 

