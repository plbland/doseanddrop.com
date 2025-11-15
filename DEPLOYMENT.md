# Dose & Drop Website - Deployment Guide

This guide explains how to deploy your website with proper URL routing for Apple App Store review.

## 🎯 What's Included

Your website now supports direct linking to:
- `yourdomain.com/privacy` - Privacy Policy page
- `yourdomain.com/marketing` - Marketing Information page
- `yourdomain.com/support` - Support page
- `yourdomain.com/` - Main landing page

## 📁 File Structure

```
doseanddrop-website/
├── index.html          # Main landing page
├── privacy.html        # Privacy Policy (standalone)
├── marketing.html      # Marketing Information (standalone)
├── support.html        # Support page (standalone)
├── .htaccess          # Apache server configuration
├── vercel.json        # Vercel deployment configuration
├── netlify.toml       # Netlify deployment configuration
├── _redirects         # Netlify alternative config
├── firebase.json      # Firebase Hosting configuration
└── DEPLOYMENT.md      # This file
```

## 🚀 Deployment Options

### Option 1: Apache Server (Traditional Hosting)

If you're using a traditional web host with Apache:

1. Upload all files to your web server
2. The `.htaccess` file will automatically handle URL routing
3. Test your URLs:
   - `https://yourdomain.com/privacy`
   - `https://yourdomain.com/marketing`
   - `https://yourdomain.com/support`

**Requirements:**
- Apache with `mod_rewrite` enabled
- `.htaccess` files allowed (AllowOverride All)

### Option 2: Netlify

1. **Via Git:**
   ```bash
   # Initialize git if not already done
   git init
   git add .
   git commit -m "Deploy Dose & Drop website"

   # Push to GitHub/GitLab
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect your Git repository
   - Netlify will automatically detect `netlify.toml`
   - Click "Deploy"

3. **Via Drag & Drop:**
   - Go to [netlify.com](https://netlify.com)
   - Drag the entire folder to the Netlify dashboard
   - Done!

**Testing:** URLs will work automatically with the `netlify.toml` configuration.

### Option 3: Vercel

1. **Via Git:**
   ```bash
   # Install Vercel CLI
   npm install -g vercel

   # Deploy
   vercel
   ```

2. **Via Dashboard:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New" → "Project"
   - Import your Git repository
   - Vercel will detect `vercel.json` automatically
   - Click "Deploy"

**Testing:** The `vercel.json` file handles all URL routing.

### Option 4: Firebase Hosting

1. **Install Firebase CLI:**
   ```bash
   npm install -g firebase-tools
   ```

2. **Initialize Firebase:**
   ```bash
   firebase login
   firebase init hosting
   ```

3. **Configure:**
   - Select your Firebase project
   - Set public directory to `.` (current directory)
   - Configure as single-page app: **No**
   - Don't overwrite existing files

4. **Deploy:**
   ```bash
   firebase deploy --only hosting
   ```

**Testing:** `firebase.json` handles URL routing.

### Option 5: GitHub Pages

GitHub Pages doesn't support server-side redirects, so we need a workaround:

1. **Create separate folders:**
   ```bash
   mkdir -p privacy marketing support
   cp privacy.html privacy/index.html
   cp marketing.html marketing/index.html
   cp support.html support/index.html
   ```

2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add routing folders for GitHub Pages"
   git push
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Select branch (usually `main`)
   - Save

**URLs will be:**
- `username.github.io/repo-name/privacy/`
- `username.github.io/repo-name/marketing/`
- `username.github.io/repo-name/support/`

## ✅ Testing Your Deployment

After deploying, test these URLs:

1. **Direct URL Access:**
   - Visit `https://yourdomain.com/privacy`
   - Visit `https://yourdomain.com/marketing`
   - Visit `https://yourdomain.com/support`

2. **Verify in Browser:**
   - URL should remain clean (no `.html` extension)
   - Page should load without redirecting
   - Content should display correctly

3. **Mobile Testing:**
   - Test on iOS Safari (what Apple reviewers use)
   - Verify pages are mobile-responsive
   - Check all links work

## 📱 For Apple App Store Review

When submitting your iOS app, provide these URLs:

1. **Privacy Policy URL:**
   ```
   https://yourdomain.com/privacy
   ```

2. **Marketing URL** (if needed):
   ```
   https://yourdomain.com/marketing
   ```

3. **Support URL:**
   ```
   https://yourdomain.com/support
   ```

## 🔧 Troubleshooting

### URLs show 404 errors

**Apache (.htaccess):**
- Verify `mod_rewrite` is enabled
- Check `.htaccess` file is uploaded
- Ensure AllowOverride is enabled in server config

**Netlify/Vercel/Firebase:**
- Verify config file is in the root directory
- Check deployment logs for errors
- Redeploy the site

### URLs show .html extension

**Fix:** Your server configuration isn't being applied
- Check that the appropriate config file exists
- Verify file permissions (should be readable)
- Contact your hosting provider

### Pages work locally but not on server

- Ensure all HTML files are uploaded
- Check file paths are correct
- Verify config file is uploaded
- Clear browser cache and test again

## 🎨 Customization

### Update Content

Edit the HTML files directly:
- `privacy.html` - Update privacy policy
- `marketing.html` - Update marketing information
- `support.html` - Update support content
- `index.html` - Update main landing page

### Change Styling

All pages use inline styles. To update:
1. Open the HTML file in an editor
2. Find the `<style>` section
3. Modify CSS as needed
4. Save and redeploy

### Add More Pages

1. Create new HTML file (e.g., `terms.html`)
2. Add routing rule to your config file:

**Apache (.htaccess):**
```apache
RewriteRule ^terms/?$ terms.html [L]
```

**Netlify (netlify.toml):**
```toml
[[redirects]]
  from = "/terms"
  to = "/terms.html"
  status = 200
```

**Vercel (vercel.json):**
```json
{ "source": "/terms", "destination": "/terms.html" }
```

## 🔒 Security Headers

All configuration files include security headers:
- `X-Frame-Options: DENY` - Prevents clickjacking
- `X-Content-Type-Options: nosniff` - Prevents MIME sniffing
- `X-XSS-Protection: 1; mode=block` - XSS protection

## 📞 Need Help?

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your hosting provider supports the configuration
3. Test URLs in incognito mode (clears cache)
4. Contact your hosting provider's support

## ✨ Quick Deploy Commands

**Netlify CLI:**
```bash
npm install -g netlify-cli
netlify deploy --prod
```

**Vercel CLI:**
```bash
npm install -g vercel
vercel --prod
```

**Firebase:**
```bash
npm install -g firebase-tools
firebase deploy --only hosting
```

Your website is now ready for Apple App Store review! 🎉
