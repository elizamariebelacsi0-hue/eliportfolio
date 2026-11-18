# Eliza Marie Portfolio

A personal portfolio website for presenting my background, skills, projects, and contact information. The site is built with Django, with React and Three.js powering the interactive ID card on the home page.

## Features

- Responsive portfolio pages for Home, About, Projects, Skills, Certificates, and Contact
- Project case studies with technology tags, galleries, and team details
- Skills page with an animated skills orbit
- Interactive 3D ID card on the home page
- Django templates with custom CSS and JavaScript

## Built With

- Python and Django
- HTML, CSS, and JavaScript
- React and Three.js
- Vite for building the React assets
- WhiteNoise for serving static files
- Vercel deployment configuration

## Run Locally

Requirements: Python and Node.js with npm. The checked-in files in `static/dist/` let Django serve the current frontend build without rebuilding it.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

2. Install Python dependencies and start Django:

   ```bash
   python -m pip install -r requirements.txt
   python manage.py runserver
   ```

3. Open <http://127.0.0.1:8000/>.

## Rebuild Frontend Assets

If you change the React components or their styles, rebuild the committed Vite output:

```bash
npm install
npm run build
```

Vite writes the generated files to `static/dist/`.

## Project Structure

- `portfolio/` ? Django settings, URL configuration, and page data
- `templates/` ? Django page templates
- `static/css/` ? page and site stylesheets
- `static/images/` ? icons and other static images
- `static/dist/` ? built React assets served by Django
- `frontend/src/` ? React components and Vite entry points
- `media/` ? portfolio project images

## Deployment

The repository includes `vercel.json` for deploying the Django WSGI application. WhiteNoise serves the committed static assets from `static/`.
