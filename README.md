# Podcast Guest Intake App

A professional web application for collecting and managing podcast guest information. Built with Flask, featuring a beautiful intake form and an admin dashboard for managing submissions.

## Features

✨ **Guest Intake Form**
- Clean, modern, and responsive design
- Comprehensive fields for guest information
- Social media links collection
- Availability and format preferences
- Real-time form validation
- Mobile-friendly interface

📊 **Admin Dashboard**
- View all guest submissions
- Beautiful card-based layout
- Delete submissions
- Export data as CSV or JSON
- Real-time statistics
- Responsive design

💾 **Data Management**
- JSON-based data storage
- Export submissions to CSV format
- Export submissions to JSON format
- Simple and reliable data persistence

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Data Storage**: JSON files

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-productivity-planner
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Guest Intake Form: http://localhost:5000
   - Admin Dashboard: http://localhost:5000/admin

## Usage

### For Podcast Guests

1. Navigate to http://localhost:5000
2. Fill out the intake form with your information:
   - Personal information (name, email, phone)
   - Social media profiles
   - Professional background and expertise
   - Discussion topics you'd like to cover
   - Availability and format preferences
3. Submit the form
4. You'll receive a confirmation message

### For Podcast Administrators

1. Navigate to http://localhost:5000/admin
2. View all guest submissions in a clean, organized layout
3. Review detailed information for each guest:
   - Contact details
   - Social media links
   - Professional background
   - Topics of expertise
   - Availability and preferences
4. Export data:
   - Click "Export as CSV" for spreadsheet-compatible format
   - Click "Export as JSON" for structured data format
5. Delete submissions:
   - Click the delete button on any submission card
   - Confirm the deletion

## Project Structure

```
ai-productivity-planner/
├── app.py                      # Flask application and API endpoints
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── submissions.json            # Data storage (auto-generated)
├── templates/
│   ├── intake.html            # Guest intake form
│   └── admin.html             # Admin dashboard
└── static/
    ├── css/                   # Custom CSS (if needed)
    └── js/                    # Custom JavaScript (if needed)
```

## API Endpoints

### POST /api/submit
Submit a new guest application
- **Body**: JSON object with guest information
- **Response**: Success/error message with submission ID

### GET /api/submissions
Retrieve all submissions
- **Response**: Array of submission objects

### DELETE /api/submissions/<id>
Delete a specific submission
- **Response**: Success/error message

### GET /api/export/csv
Export all submissions as CSV
- **Response**: CSV file download

### GET /api/export/json
Export all submissions as JSON
- **Response**: JSON file download

## Data Storage

Guest submissions are stored in `submissions.json` in the root directory. Each submission includes:

- Unique ID and timestamp
- Personal information (name, email, phone, website)
- Social media profiles (Twitter, LinkedIn, Instagram)
- Professional details (expertise, topics, bio)
- Previous podcast appearances
- Availability and format preferences
- Additional notes
- Source of referral

## Security Notes

⚠️ **Important**: This application is designed for development and local use. Before deploying to production:

1. Change the Flask secret key in `app.py`
2. Add authentication to the admin dashboard
3. Implement HTTPS
4. Add rate limiting to prevent spam
5. Validate and sanitize all inputs on the server side
6. Consider using a proper database (PostgreSQL, MySQL, etc.)
7. Add CORS headers if needed
8. Implement proper error logging

## Customization

### Styling
- The application uses Tailwind CSS via CDN
- Customize colors by editing the gradient values in the HTML files
- Add custom CSS in `/static/css/` if needed

### Fields
- Modify form fields in `templates/intake.html`
- Update API endpoint in `app.py` to handle new fields
- Update admin display in `templates/admin.html`

### Branding
- Update the title and description in both HTML templates
- Add your logo by placing it in `/static/` and updating the templates

## Troubleshooting

**Application won't start**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check if port 5000 is available
- Verify Python version (3.7+)

**Submissions not saving**
- Check file permissions in the project directory
- Ensure `submissions.json` can be created/modified
- Check browser console for JavaScript errors

**Export not working**
- Ensure there are submissions in the database
- Check browser console for errors
- Verify Flask routes are accessible

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue on the GitHub repository.

---

Built with ❤️ for podcasters
