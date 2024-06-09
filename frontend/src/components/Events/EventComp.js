import React, { useState } from 'react';
import './EventComp.css'
import Popup1 from '../popup/popupEvents1.js' 
import Popup2 from '../popup/popupEvents2.js' 
import BoxProject from '../icons/iconsProject.js'
import BoxEvent from '../icons/iconsEvent.js'
import SomeProject from './SomeProject.js'

function EventComp() {
  const [popupOpen, setPopupOpen] = useState(false);
  const [popupOpen2, setPopupOpen2] = useState(false);
  return (
    <div className="events-comp">
      <div className="banner">
        <h1 className="banner-heading">Проекты Союза Студентов</h1>
      </div>
      <div className="events-comp-container">
        <div className="btns-create">
          <button onClick={()=> setPopupOpen(true)}>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
            </svg>
            Создать проект
          </button>
          <button onClick={()=> setPopupOpen2(true)}>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
            </svg>
            Создать мероприятие
          </button>
        </div>
        <div className="projs-container">
          <h2 className='header-proj'>Проекты</h2>
          <div className='box-w-proj'>
            <BoxProject/>
            <BoxProject/>
            <BoxProject/>
            <BoxProject/>
            <BoxProject/>
            <BoxProject/>
            <BoxProject/>
          </div>
        </div>
        <div className="events-container">
          <h2 className='header-proj'>Мероприятия</h2>
          <div className='box-w-proj'>
           <BoxEvent/>
           <BoxEvent/>
           <BoxEvent/>
           <BoxEvent/>
           <BoxEvent/>
          </div>
        </div>
        <div className="archive-container">
          <h2 className='header-proj'>Архив</h2>
          <div className='box-w-proj'>
           <BoxEvent/>
           <BoxEvent/>
           <BoxEvent/>
           <BoxProject/>
           <BoxProject/>
          </div>
        </div>
      </div>
      <Popup1 
            isOpen={popupOpen}
            onClose={()=> setPopupOpen(false)}
            />
      <Popup2 
            isOpen={popupOpen2}
            onClose={()=> setPopupOpen2(false)}
            />          
    </div>
    
  )
}

export default EventComp;
