from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# GitHub username
GITHUB_USERNAME = "patowari"

@app.route('/api/repositories', methods=['GET'])
def get_repositories():
    """Fetch repositories from GitHub API"""
    try:
        # GitHub API endpoint
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        
        # Add parameters to get more information and sort by updated
        params = {
            'sort': 'updated',
            'direction': 'desc',
            'per_page': 50  # Adjust as needed
        }
        
        # Make request to GitHub API
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            repositories = response.json()
            
            # Filter and format the data
            formatted_repos = []
            for repo in repositories:
                # Skip forked repositories if you want only original repos
                # Remove this condition if you want to include forks
                if not repo['fork']:
                    formatted_repo = {
                        'id': repo['id'],
                        'name': repo['name'],
                        'full_name': repo['full_name'],
                        'description': repo['description'],
                        'html_url': repo['html_url'],
                        'clone_url': repo['clone_url'],
                        'language': repo['language'],
                        'stargazers_count': repo['stargazers_count'],
                        'forks_count': repo['forks_count'],
                        'watchers_count': repo['watchers_count'],
                        'size': repo['size'],
                        'created_at': repo['created_at'],
                        'updated_at': repo['updated_at'],
                        'pushed_at': repo['pushed_at'],
                        'topics': repo.get('topics', []),
                        'visibility': repo['visibility'],
                        'default_branch': repo['default_branch']
                    }
                    formatted_repos.append(formatted_repo)
            
            return jsonify({
                'success': True,
                'count': len(formatted_repos),
                'repositories': formatted_repos
            })
        else:
            return jsonify({
                'success': False,
                'error': f'GitHub API returned status code: {response.status_code}',
                'message': 'Failed to fetch repositories'
            }), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to connect to GitHub API'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'An unexpected error occurred'
        }), 500

@app.route('/api/repository/<repo_name>', methods=['GET'])
def get_single_repository(repo_name):
    """Fetch a single repository details"""
    try:
        url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            repo = response.json()
            return jsonify({
                'success': True,
                'repository': repo
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Repository not found or GitHub API error: {response.status_code}'
            }), response.status_code
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get all unique languages used across repositories"""
    try:
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        params = {'per_page': 100}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            repositories = response.json()
            languages = set()
            
            for repo in repositories:
                if repo['language'] and not repo['fork']:
                    languages.add(repo['language'])
            
            return jsonify({
                'success': True,
                'languages': sorted(list(languages))
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch repositories'
            }), response.status_code
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get overall GitHub statistics"""
    try:
        # Get user info
        user_url = f"https://api.github.com/users/{GITHUB_USERNAME}"
        user_response = requests.get(user_url)
        
        # Get repositories
        repos_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        params = {'per_page': 100}
        repos_response = requests.get(repos_url, params=params)
        
        if user_response.status_code == 200 and repos_response.status_code == 200:
            user_data = user_response.json()
            repositories = repos_response.json()
            
            # Calculate stats
            total_stars = sum(repo['stargazers_count'] for repo in repositories if not repo['fork'])
            total_forks = sum(repo['forks_count'] for repo in repositories if not repo['fork'])
            original_repos = len([repo for repo in repositories if not repo['fork']])
            
            stats = {
                'public_repos': user_data['public_repos'],
                'original_repos': original_repos,
                'total_stars': total_stars,
                'total_forks': total_forks,
                'followers': user_data['followers'],
                'following': user_data['following'],
                'profile_url': user_data['html_url'],
                'avatar_url': user_data['avatar_url'],
                'bio': user_data.get('bio', ''),
                'location': user_data.get('location', ''),
                'blog': user_data.get('blog', ''),
                'created_at': user_data['created_at']
            }
            
            return jsonify({
                'success': True,
                'stats': stats
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch GitHub data'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': f'GitHub Portfolio API for {GITHUB_USERNAME}',
        'endpoints': {
            '/api/repositories': 'GET - Fetch all repositories',
            '/api/repository/<name>': 'GET - Fetch single repository',
            '/api/languages': 'GET - Get all programming languages used',
            '/api/stats': 'GET - Get GitHub profile statistics'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
