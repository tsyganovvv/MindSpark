import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'

import Home from '@/pages/Home/Home';
import Chat from '@/pages/Chat/Chat';
import Auth from '@/pages/Auth/Auth';
import AuthGoogleCallback from '@/pages/Auth/Google/AuthGoogleCallback'


export default function MainRouter() {

  return (
  <Router>
    <nav>
      <Link to="/" style={{ marginRight: '15px' }}>Home</Link>
      <Link to="/chat" style={{ marginRight: '15px' }}>Chat</Link>
      <Link to="/auth" style={{ marginRight: '15px' }}>Authorization</Link>
    </nav>

    <Routes>
      <Route path="/" element={<Home/>}></Route>
      <Route path="/chat" element={<Chat/>}></Route>
      <Route path="/auth" element={<Auth/>}></Route>
      <Route path="/auth/google" element={<AuthGoogleCallback/>}></Route>
    </Routes>
    <footer>
      <div>
        <p>© 2025 MindSpark. All rights reserved.</p>
      </div>
    </footer>
  </Router>
  )
}