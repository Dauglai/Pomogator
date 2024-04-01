import React from 'react';
import Sidebar from './components/sidebar/Sidebar';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Profile from './pages/Profile';
import Events from './pages/Events';
import Team from './pages/Team';
import Home from './pages/Home';
import Tasks from './pages/Tasks';
import './App.css'


const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
      </Routes>
      <Sidebar>
        <Routes>
          <Route path='/profile' element={<Profile/>} />
          <Route path='/tasks' element={<Tasks/>} />
          <Route path='/events' element={<Events/>} />
          <Route path='/team' element={<Team/>} />
        </Routes>
      </Sidebar>
    </BrowserRouter>
  );
};

export default App;
