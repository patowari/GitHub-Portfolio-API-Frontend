# GitHub-Portfolio-API-Frontend
# 🚀 GitHub Portfolio API & Frontend

A beautiful, responsive portfolio website that dynamically fetches and displays your GitHub repositories using a Flask API backend and modern HTML/CSS/JavaScript frontend.

<img width="690" alt="Screenshot 2025-06-07 at 10 33 02 PM" src="https://github.com/user-attachments/assets/7ecddf40-89ba-491e-b49f-bffe58dbcf26" />


## ✨ Features

### 🎯 Backend API Features
- **RESTful API** built with Flask
- **GitHub API Integration** for real-time data
- **Multiple endpoints** for different data needs
- **Error handling** and status codes
- **CORS enabled** for frontend integration
- **Statistics aggregation** (stars, forks, languages)

### 🎨 Frontend Features
- **Responsive Design** - Works on all devices
- **Real-time Search** - Find repositories instantly
- **Dynamic Filtering** - Filter by programming language
- **Sorting Options** - Sort by stars or update date
- **Beautiful UI** - Modern gradient design with animations
- **Repository Cards** - Detailed info for each project
- **Profile Integration** - Shows GitHub profile stats
- **Topic Tags** - Displays repository topics
- **Loading States** - Smooth user experience

## 🛠️ Tech Stack

**Backend:**
- Python 3.7+
- Flask 2.3.3
- Flask-CORS 4.0.0
- Requests 2.31.0

**Frontend:**
- HTML5
- CSS3 (with modern features)
- Vanilla JavaScript (ES6+)
- Font Awesome Icons

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A modern web browser

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/patowari/GitHub-Portfolio-API-Frontend
cd github-portfolio
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the API
Open `app.py` and update the GitHub username:
```python
GITHUB_USERNAME = "your-github-username"  # Change this to your username
```

### 4. Run the Flask API
```bash
python app.py
```
The API will be available at `http://localhost:5000`

### 5. Open the Frontend
Open `index.html` in your web browser, or serve it using a simple HTTP server:
```bash
# Using Python's built-in server
python -m http.server 8000
```
Then visit `http://localhost:8000`

## 📚 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### GET `/api/repositories`
Fetches all public repositories (excluding forks by default)

**Response:**
```json
{
  "success": true,
  "count": 15,
  "repositories": [
    {
      "id": 123456789,
      "name": "awesome-project",
      "description": "An awesome project description",
      "html_url": "https://github.com/username/awesome-project",
      "language": "JavaScript",
      "stargazers_count": 42,
      "forks_count": 8,
      "topics": ["react", "nodejs", "api"]
    }
  ]
}
```

#### GET `/api/repository/<repo_name>`
Fetches detailed information for a specific repository

#### GET `/api/languages`
Returns all unique programming languages used across repositories

#### GET `/api/stats`
Returns GitHub profile statistics and aggregated repository data

**Response:**
```json
{
  "success": true,
  "stats": {
    "public_repos": 25,
    "total_stars": 150,
    "total_forks": 45,
    "followers": 100,
    "avatar_url": "https://github.com/avatar.jpg"
  }
}
```

## 🎨 Customization

### Frontend Styling
The CSS uses modern features like:
- CSS Grid and Flexbox for layouts
- CSS Custom Properties for theming
- Backdrop filters for glass effects
- CSS animations and transitions

### Color Scheme
Update the gradient colors in the CSS:
```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### API Configuration
Modify the Flask app settings in `app.py`:
```python
# Change port or host
app.run(debug=True, host='0.0.0.0', port=5000)

# Add GitHub token for higher rate limits (optional)
headers = {'Authorization': 'token YOUR_GITHUB_TOKEN'}
```

## 📱 Responsive Design

The portfolio is fully responsive and includes:
- Mobile-first design approach
- Flexible grid layouts
- Touch-friendly interface
- Optimized for all screen sizes

## 🔧 Advanced Configuration

### GitHub API Rate Limits
For higher rate limits, add a GitHub Personal Access Token:

1. Create a token at https://github.com/settings/tokens
2. Add it to your Flask app:
```python
headers = {
    'Authorization': 'token YOUR_GITHUB_TOKEN',
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(url, headers=headers, params=params)
```

### Deployment Options

#### Heroku Deployment
1. Create a `Procfile`:
```
web: python app.py
```

2. Update the port configuration:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

#### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- GitHub API has rate limits (60 requests/hour for unauthenticated requests)
- Large numbers of repositories may take time to load
- Some repository statistics might be cached by GitHub

## 🔮 Future Enhancements

- [ ] Add repository README preview
- [ ] Implement caching for better performance
- [ ] Add dark/light theme toggle
- [ ] Include contribution graph
- [ ] Add project categories/tags
- [ ] Implement pagination for large repository lists
- [ ] Add export functionality (PDF/JSON)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/patowari/github-portfolio/issues) page
2. Create a new issue with detailed information
3. Include error messages and browser console logs

## 🙏 Acknowledgments

- GitHub API for providing repository data
- Font Awesome for beautiful icons
- Flask community for excellent documentation
- Modern CSS techniques and best practices

---

**Made with ❤️ by [Patowari](https://github.com/patowari)**

⭐ Star this repository if you found it helpful!
