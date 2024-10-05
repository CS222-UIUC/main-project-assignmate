//server.js

const express = require('express');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const cookieSession = require('cookie-session');
require('dotenv').config();

// Log the environment variables to verify they are loaded correctly
console.log("GOOGLE_CLIENT_ID:", process.env.GOOGLE_CLIENT_ID);
console.log("GOOGLE_CLIENT_SECRET:", process.env.GOOGLE_CLIENT_SECRET);
console.log("COOKIE_KEY:", process.env.COOKIE_KEY);

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cookieSession({
  maxAge: 24 * 60 * 60 * 1000, // 1 day
  keys: [process.env.COOKIE_KEY] // Use a secure key in production
}));


app.use(passport.initialize());
app.use(passport.session());

// Passport Configuration
passport.serializeUser((user, done) => {
  done(null, user);
});

passport.deserializeUser((user, done) => {
  done(null, user);
});

// Google OAuth Strategy
passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  // Restrict to @illinois.edu domain
  if (profile.emails[0].value.endsWith('@illinois.edu')) {
    return done(null, profile);
  } else {
    return done(null, false, { message: 'Unauthorized domain' });
  }
}));

// Routes
app.get('/auth/google', passport.authenticate('google', {
  scope: ['profile', 'email']
}));

app.get('/auth/google/callback', 
  passport.authenticate('google', { failureRedirect: '/' }),
  (req, res) => {
    // Successful authentication, redirect to front end.
    res.redirect('http://localhost:3000'); // Adjust as needed
  }
);

app.get('/api/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});

app.get('/api/current_user', (req, res) => {
  res.send(req.user);
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
