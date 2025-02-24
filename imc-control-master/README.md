# web-app-prototype/web-app-prototype/README.md

# Web App Prototype

This project is a web application prototype designed to manage and visualize weight and height control data. It utilizes Flask for the backend API and Vue.js for the frontend interface, providing a modern and responsive experience for mobile devices.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

- **app.py**: Entry point of the Flask application, initializes the app and sets up the database connection.
- **models.py**: Defines SQLAlchemy models, including the `ControlPesoAltura` model for weight and height control data.
- **routes.py**: Contains API routes for user authentication, data retrieval, and data insertion.
- **requirements.txt**: Lists the dependencies required for the backend.
- **README.md**: Documentation for the backend, including setup instructions and API usage.

### Frontend

- **public/index.html**: Main HTML file for the Vue.js application.
- **src/assets**: Contains static assets such as images and stylesheets.
- **src/components**: Contains Vue components:
  - **Login.vue**: Login component for user authentication.
  - **Summary.vue**: Displays graphs and statistics from the control data.
  - **Form.vue**: Form for inputting control data for the current date.
- **src/router/index.js**: Sets up Vue Router for navigation.
- **src/store/index.js**: Configures Vuex for state management.
- **src/views**: Contains view components:
  - **Home.vue**: Main dashboard view.
  - **Login.vue**: View for the login component.
- **src/App.vue**: Root component of the Vue.js application.
- **src/main.js**: Entry point for the Vue.js application.
- **package.json**: Configuration file for npm.
- **babel.config.js**: Babel configuration for the Vue.js application.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Run the Vue.js application:
   ```
   npm run serve
   ```

## Usage

- Access the application through the frontend URL provided after running the Vue.js application.
- Use the login page to authenticate users.
- View the summary of weight and height control data with visually appealing graphs.
- Insert new control data using the provided form.

## License

This project is licensed under the MIT License.