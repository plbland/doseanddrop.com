# Dose & Drop Website

Landing page and policy pages for the Dose & Drop iOS app.

## 🎯 Direct URL Access

This website supports clean, direct URLs required for Apple App Store review:

- **Home:** `https://yourdomain.com/`
- **Privacy Policy:** `https://yourdomain.com/privacy`
- **Marketing Info:** `https://yourdomain.com/marketing`
- **Support:** `https://yourdomain.com/support`

## 📁 Files

- `index.html` - Main landing page (original single-page app)
- `privacy.html` - Standalone privacy policy page
- `marketing.html` - Standalone marketing information page
- `support.html` - Standalone support page
- `.htaccess` - Apache server routing configuration
- `vercel.json` - Vercel deployment configuration
- `netlify.toml` - Netlify deployment configuration
- `_redirects` - Alternative Netlify configuration
- `firebase.json` - Firebase Hosting configuration
- `test-server.py` - Local testing server

## 🚀 Quick Start

### Test Locally

```bash
# Run the test server
python3 test-server.py

# Then visit in your browser:
# http://localhost:8000/privacy
# http://localhost:8000/marketing
# http://localhost:8000/support
```

### Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for:
- Apache servers (traditional hosting)
- Netlify
- Vercel
- Firebase Hosting
- GitHub Pages

## ✅ Apple App Store URLs

When submitting to the App Store, use these URLs:

1. **Privacy Policy URL:**
   ```
   https://yourdomain.com/privacy
   ```

2. **Support URL:**
   ```
   https://yourdomain.com/support
   ```

3. **Marketing URL** (if requested):
   ```
   https://yourdomain.com/marketing
   ```

## 🔧 How It Works

The website uses server-side routing to map clean URLs to HTML files:

```
/privacy    →  privacy.html
/marketing  →  marketing.html
/support    →  support.html
/           →  index.html
```

Different configuration files are included for various hosting platforms. The appropriate one will be used automatically based on your hosting provider.

## 📝 Customization

To update content, simply edit the HTML files:
- Each page is self-contained with inline CSS
- No build process or dependencies required
- Just edit, save, and deploy

## 🔒 Security

All configuration files include security headers:
- X-Frame-Options
- X-Content-Type-Options
- X-XSS-Protection

## 📞 Support

For questions about deployment or customization, see [DEPLOYMENT.md](DEPLOYMENT.md).

---

**Ready for Apple App Store submission** ✓
