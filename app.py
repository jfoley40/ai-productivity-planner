"""
Podcast Guest Intake Application
A Flask web application for collecting and managing podcast guest information
"""

from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from datetime import datetime
import csv
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Data file path
DATA_FILE = 'submissions.json'


def load_submissions():
    """Load guest submissions from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_submissions(submissions):
    """Save guest submissions to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(submissions, f, indent=2)


@app.route('/')
def index():
    """Main intake form page"""
    return render_template('intake.html')


@app.route('/admin')
def admin():
    """Admin dashboard page"""
    return render_template('admin.html')


@app.route('/api/submit', methods=['POST'])
def submit_guest():
    """API endpoint to submit guest information"""
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'expertise']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'error': f'Missing required field: {field}'}), 400

        # Create submission object
        submission = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S%f'),
            'timestamp': datetime.now().isoformat(),
            'name': data.get('name', ''),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'website': data.get('website', ''),
            'social_media': {
                'twitter': data.get('twitter', ''),
                'linkedin': data.get('linkedin', ''),
                'instagram': data.get('instagram', '')
            },
            'expertise': data.get('expertise', ''),
            'topics': data.get('topics', ''),
            'bio': data.get('bio', ''),
            'previous_appearances': data.get('previous_appearances', ''),
            'availability': data.get('availability', ''),
            'preferred_format': data.get('preferred_format', ''),
            'additional_notes': data.get('additional_notes', ''),
            'heard_about': data.get('heard_about', '')
        }

        # Load existing submissions
        submissions = load_submissions()

        # Add new submission
        submissions.append(submission)

        # Save to file
        save_submissions(submissions)

        return jsonify({'success': True, 'message': 'Submission received successfully!', 'id': submission['id']})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    """API endpoint to retrieve all submissions"""
    try:
        submissions = load_submissions()
        # Sort by timestamp, most recent first
        submissions.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        return jsonify({'success': True, 'submissions': submissions})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/submissions/<submission_id>', methods=['DELETE'])
def delete_submission(submission_id):
    """API endpoint to delete a submission"""
    try:
        submissions = load_submissions()
        submissions = [s for s in submissions if s.get('id') != submission_id]
        save_submissions(submissions)
        return jsonify({'success': True, 'message': 'Submission deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/export/csv')
def export_csv():
    """Export submissions as CSV"""
    try:
        submissions = load_submissions()

        if not submissions:
            return jsonify({'success': False, 'error': 'No submissions to export'}), 404

        # Create CSV in memory
        output = io.StringIO()

        # Define CSV fields
        fieldnames = [
            'ID', 'Timestamp', 'Name', 'Email', 'Phone', 'Website',
            'Twitter', 'LinkedIn', 'Instagram', 'Expertise', 'Topics',
            'Bio', 'Previous Appearances', 'Availability', 'Preferred Format',
            'Additional Notes', 'Heard About Us'
        ]

        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for sub in submissions:
            writer.writerow({
                'ID': sub.get('id', ''),
                'Timestamp': sub.get('timestamp', ''),
                'Name': sub.get('name', ''),
                'Email': sub.get('email', ''),
                'Phone': sub.get('phone', ''),
                'Website': sub.get('website', ''),
                'Twitter': sub.get('social_media', {}).get('twitter', ''),
                'LinkedIn': sub.get('social_media', {}).get('linkedin', ''),
                'Instagram': sub.get('social_media', {}).get('instagram', ''),
                'Expertise': sub.get('expertise', ''),
                'Topics': sub.get('topics', ''),
                'Bio': sub.get('bio', ''),
                'Previous Appearances': sub.get('previous_appearances', ''),
                'Availability': sub.get('availability', ''),
                'Preferred Format': sub.get('preferred_format', ''),
                'Additional Notes': sub.get('additional_notes', ''),
                'Heard About Us': sub.get('heard_about', '')
            })

        # Create response
        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'podcast_guests_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        )

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/export/json')
def export_json():
    """Export submissions as JSON"""
    try:
        submissions = load_submissions()

        if not submissions:
            return jsonify({'success': False, 'error': 'No submissions to export'}), 404

        # Create JSON response
        output = json.dumps(submissions, indent=2)

        return send_file(
            io.BytesIO(output.encode('utf-8')),
            mimetype='application/json',
            as_attachment=True,
            download_name=f'podcast_guests_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        )

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
