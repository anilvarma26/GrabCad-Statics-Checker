GrabCad-Statics-Checker
GrabCad-Statics-Checker is a Python-based desktop application that allows users to retrieve and view statistics from a GrabCad user profile. It uses web scraping with BeautifulSoup to gather data, and provides a simple graphical interface built with tkinter.

Features
Simple User Interface: Built with tkinter for an easy-to-use GUI.
Profile Statistics: Retrieves profile data such as the number of models, likes, and comments.
Web Scraping: Uses BeautifulSoup to scrape and extract data from GrabCad profiles.
Customizable URL Input: Enter any GrabCad username to get the specific profile statistics.
Requirements
Python 3.x
requests library
beautifulsoup4 library
tkinter (comes with Python by default)
How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/GrabCad-Statics-Checker.git
Install the required dependencies:

You can install the required Python libraries using pip:

bash
Copy code
pip install requests beautifulsoup4
Run the application:

Once the dependencies are installed, run the GrabCad-Statics-Checker.py script:

bash
Copy code
python GrabCad-Statics-Checker.py
Input a GrabCad username:

Launch the application.
Enter a GrabCad username into the input field.
Click "Get Profile" to fetch and display the user's profile statistics.
Example
Enter a GrabCad username (e.g., john_doe) and click the "Get Profile" button to view their profile statistics such as the number of models, likes, and comments.
Contribution
Feel free to fork the repository, raise issues, or submit pull requests to improve the tool.

added an exe file for ease of access of the statics viewer.
