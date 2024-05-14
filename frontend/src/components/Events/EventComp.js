import React from "react"
import './EventComp.css'

function EventComp() {
  return (
    <div className="events-comp">
      <div className="banner">
        <h1 className="banner-heading">Проекты Союза Студентов</h1>
      </div>
      <div className="events-comp-container">
        <div className="btns-create">
          <button>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
            </svg>
            Создать проект
          </button>
          <button>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
            </svg>
            Создать мероприятие
          </button>
        </div>
        <div className="projs-container">
          <h2>Проекты</h2>
          <div></div>
        </div>
        <div className="events-container">

        </div>
        <div className="archive-container">

        </div>
      </div>
      
    </div>
  )
}

export default EventComp;
