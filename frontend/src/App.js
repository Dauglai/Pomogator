import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import { AuthProvider } from './context/AuthContext'

import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import Header from './components/Header'

import PrivateRoute from './utils/PrivateRoute'

import React from 'react';
import Sidebar from './components/sidebar/Sidebar';
import Profile from './pages/Profile';
import Events from './pages/Events';
import Team from './pages/Team';
import Tasks from './pages/Tasks';
import './App.css'


function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider className="auth__provider">
          <Header />
          <Routes>
            <Route path="/" element={<PrivateRoute><HomePage /></PrivateRoute>} />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </AuthProvider>
        <Sidebar>
          <Routes>
            <Route path='/profile' element={<Profile />} />
            <Route path='/tasks' element={<Tasks />} />
            <Route path='/events' element={<Events />} />
            <Route path='/team' element={<Team />} />
          </Routes>
        </Sidebar>
      </Router>
    </div>
  );
}

export default App;

