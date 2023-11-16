**Overview: What it is**
The Recipe Maker is a full-stack web application that takes as input the user’s perishable and non-perishable kitchen ingredients before making a fetch request to Chat-GPT to get some suggested recipes.

**Technical Structure: Application Components**
The frontend is a simple mixture of HTML, CSS, and vanilla JavaScript. The backend utilizes Flask, a database, and SQL to store a user's larder so they don’t have to retype it every time they log in.

**Main Functionality: User Interface**
There are two main pages: one for entering your non-perishable long-term goods into a ‘larder’ and another for fresh ingredients that aren’t stored because they change daily. On both pages, there are handy suggestions that, when clicked, are automatically added to your larder or ingredients list. Flask then makes a fetch request to the Chat GPT API, which returns 3 recipes from the foods given. The application then presents these on the main page of the application.

**Purpose and Efficiency: Optimizing Chat GPT**
The idea is to make a Fridge dinner recipe maker that modifies Chat GPT to make it faster at making recipes because your larder is already saved (so no re-typing) and there are suggestions so you don’t have to think too hard about what you have.

**File Organization: Directory Structure**

- In the `templates` folder, you’ll find all the HTML. There is a `layout.html` which contains the navigation and footer, as well as the tags which link it to the CSS, JS, and so on. Each of the other HTML files (`Index`, `Larder`, `Login`, and `Register`) extend this Layout and use Jinja programming language to insert dynamic content from the Flask backend.
- Within this folder are images, CSS, and JS for the application. `styles.css` is one file with all the stylings for the website. It has all the colors stored in variables, making them easy to change over the whole application. Then contains all the styling for the classes and HTML elements. The app utilizes the flexbox property especially. There are media queries so the app is mobile-friendly as well. JavaScript was used for dynamically entering the suggested ingredients on the panels on both pages into the inputs; there are two files in the `js` folder.
- Here includes all the imports for the Python/ Flask backend, such as hashed passwords for users, Open AI (for Chat GPT), Session, and more. Then the views with all the app routes, where the main pages require a login from the session. Data from forms in the templates are sent here using POST and stored in variables, then sent to the database.
- The database was set up using a `schema.sql` and `ini_db.py` file which are also included. Then within `app.py` SQL commands are sent to the database, which includes only one table for ‘Users’. Larder ingredients are saved as part of each user, as well as their password and name. A final mention is that there are multiple dependencies in a `venv` folder for Flask and Open AI, which are stored in `requirements.txt` so you can download and use the app yourself.

**Design Considerations: User Interface and Aesthetics**
The key to the design was the purpose, to create an easier and more functionally specific version of Chat GPT. I wanted the page to be easy to navigate, so users can edit their larders, which is why I chose a `layout.html` design pattern. For a modern look, I tried to use modern CSS techniques such as transitions, so hover effects are smoother. I chose an autumnal color scheme, simply because it looked nice and had a variety of usable colors. The logo at the top left was created using GIMP, merging a chef hat with the Chat GPT logo (hopefully I won’t get sued by a disgruntled cheffing robot any time soon).

**Conclusion: Final Remarks**
This was a lot of fun to put together. I wish I could put it online for general use, but sadly, the Chat GPT API charges me for every use, meaning I’d have to set up payments from users, which feels excessive for what the application does. Feel free to download, put in your own API key, and have some tasty fridge dinners!
