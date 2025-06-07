#!/usr/bin/env python3
"""
API Test Script for GitHub Portfolio
Run this script to test all API endpoints
"""

import requests
import json
import sys

API_BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, description):
    """Test a single API endpoint"""
    print(f"\n🔍 Testing: {description}")
    print(f"📡 Endpoint: {endpoint}")
    print("-" * 50)
    
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=10)
        
        print(f"✅ Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if endpoint == "/":
                print(f"📄 Message: {data.get('message', 'No message')}")
                print(f"🔗 Available Endpoints: {len(data.get('endpoints', {}))}")
                
            elif endpoint == "/api/repositories":
                print(f"📊 Success: {data.get('success', False)}")
                print(f"📦 Repository Count: {data.get('count', 0)}")
                if data.get('repositories'):
                    first_repo = data['repositories'][0]
                    print(f"🎯 First Repo: {first_repo.get('name', 'N/A')}")
                    print(f"💻 Language: {first_repo.get('language', 'N/A')}")
                    print(f"⭐ Stars: {first_repo.get('stargazers_count', 0)}")
                    
            elif endpoint == "/api/stats":
                print(f"📊 Success: {data.get('success', False)}")
                if data.get('stats'):
                    stats = data['stats']
                    print(f"📂 Public Repos: {stats.get('public_repos', 0)}")
                    print(f"⭐ Total Stars: {stats.get('total_stars', 0)}")
                    print(f"🍴 Total Forks: {stats.get('total_forks', 0)}")
                    print(f"👥 Followers: {stats.get('followers', 0)}")
                    
            elif endpoint == "/api/languages":
                print(f"📊 Success: {data.get('success', False)}")
                languages = data.get('languages', [])
                print(f"💻 Languages Found: {len(languages)}")
                if languages:
                    print(f"🔤 Languages: {', '.join(languages[:5])}")
                    
            print("✅ Test PASSED")
            
        else:
            print(f"❌ Error: {response.status_code}")
            try:
                error_data = response.json()
                print(f"🔴 Error Message: {error_data.get('message', 'Unknown error')}")
            except:
                print(f"🔴 Raw Response: {response.text[:200]}...")
            print("❌ Test FAILED")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Cannot connect to the API server")
        print("💡 Make sure Flask server is running: python app.py")
        print("❌ Test FAILED")
        
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: API request timed out")
        print("❌ Test FAILED")
        
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
        print("❌ Test FAILED")

def main():
    """Run all API tests"""
    print("🚀 GitHub Portfolio API Test Suite")
    print("=" * 60)
    
    # Test endpoints
    endpoints = [
        ("/", "Home endpoint"),
        ("/api/repositories", "Repositories endpoint"),
        ("/api/stats", "Statistics endpoint"),
        ("/api/languages", "Languages endpoint")
    ]
    
    total_tests = len(endpoints)
    passed_tests = 0
    
    for endpoint, description in endpoints:
        try:
            test_endpoint(endpoint, description)
            passed_tests += 1
        except KeyboardInterrupt:
            print("\n\n⚠️ Tests interrupted by user")
            sys.exit(1)
        except:
            print("❌ Test encountered an error")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {passed_tests}/{total_tests}")
    print(f"❌ Failed: {total_tests - passed_tests}/{total_tests}")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Your API is working correctly.")
        print("💡 You can now open index.html in your browser.")
    else:
        print("⚠️ Some tests failed. Check the Flask server and try again.")
        
    print("\n💡 Next Steps:")
    print("1. Make sure Flask server is running: python app.py")
    print("2. Open index.html in your browser")
    print("3. Check browser console for any JavaScript errors")

if __name__ == "__main__":
    main()
