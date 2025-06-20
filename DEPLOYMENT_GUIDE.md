# 🚀 Deployment Guide - Typing Speed Game

Your typing game is ready for deployment! Here are the easiest ways to deploy it online.

## 🎯 **Recommended: Render.com (FREE & Easy)**

### Step 1: Prepare Your Code
1. **Create a GitHub repository** (if you don't have one)
2. **Upload your files** to GitHub:
   ```
   typing_game.py
   requirements.txt
   Procfile
   runtime.txt
   templates/
   ├── index.html
   └── leaderboard.html
   ```

### Step 2: Deploy on Render
1. **Go to [render.com](https://render.com)** and sign up
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service**:
   - **Name**: `typing-speed-game`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python typing_game.py`
   - **Plan**: Free

5. **Click "Create Web Service"**
6. **Wait for deployment** (2-3 minutes)

### Step 3: Access Your Game
- **Your game will be available at**: `https://your-app-name.onrender.com`
- **Share this URL** with anyone in the world!

---

## 🌐 **Alternative: Railway.app**

### Step 1: Deploy on Railway
1. **Go to [railway.app](https://railway.app)**
2. **Sign up with GitHub**
3. **Click "New Project"** → **"Deploy from GitHub repo"**
4. **Select your repository**
5. **Railway will auto-detect Python and deploy**

### Step 2: Get Your URL
- Railway will provide a URL like: `https://your-app-name.railway.app`

---

## 🐍 **Alternative: PythonAnywhere**

### Step 1: Create Account
1. **Go to [pythonanywhere.com](https://pythonanywhere.com)**
2. **Sign up for free account**

### Step 2: Upload Files
1. **Go to "Files" tab**
2. **Upload all your files** to your account
3. **Create a new directory** for your project

### Step 3: Set Up Web App
1. **Go to "Web" tab**
2. **Click "Add a new web app"**
3. **Choose "Flask"** and **Python 3.9**
4. **Set source code** to your project directory
5. **Set WSGI file** to point to your `typing_game.py`

---

## 🔧 **Manual Deployment Steps**

### 1. **Create GitHub Repository**
```bash
git init
git add .
git commit -m "Initial commit - Typing Speed Game"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/typing-game.git
git push -u origin main
```

### 2. **Deploy on Render**
1. **Connect GitHub repo** to Render
2. **Auto-deploy** will happen on every push

---

## 📋 **Files Checklist**

Make sure you have these files in your repository:
- ✅ `typing_game.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Tells deployment platform how to run
- ✅ `runtime.txt` - Python version specification
- ✅ `templates/index.html` - Game interface
- ✅ `templates/leaderboard.html` - Leaderboard page

---

## 🌍 **After Deployment**

### Your Game Will Be Available At:
- **Render**: `https://your-app-name.onrender.com`
- **Railway**: `https://your-app-name.railway.app`
- **PythonAnywhere**: `https://your-username.pythonanywhere.com`

### Features Available Online:
- ✅ **Global Access**: Anyone can play from anywhere
- ✅ **Real-time Leaderboard**: Global competition
- ✅ **Persistent Database**: Scores saved permanently
- ✅ **Mobile Friendly**: Works on phones and tablets

---

## 🚨 **Important Notes**

### Database
- **Local**: Uses SQLite file
- **Deployed**: May need to switch to PostgreSQL for production
- **For now**: SQLite works fine for small-scale deployment

### Environment Variables
- **PORT**: Automatically set by deployment platform
- **Debug**: Set to False for production

### Security
- **Debug mode**: Disabled for production
- **Host**: Set to `0.0.0.0` for external access

---

## 🎉 **Share Your Game!**

Once deployed, share your URL with:
- **Classmates** for lab competitions
- **Friends** for typing challenges
- **Social media** to show off your project
- **Portfolio** to demonstrate your skills

---

## 🔄 **Updates**

To update your deployed game:
1. **Make changes** to your local files
2. **Push to GitHub**: `git push origin main`
3. **Auto-deploy** will happen automatically

---

**Your typing game will be live on the internet! 🌐🚀** 