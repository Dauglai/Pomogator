import React, { useState } from 'react';
import './SomeProject.css'
import Popup2 from '../popup/popupEvents2';
import BoxEvent from '../icons/iconsEvent.js'
import PopupProjectEdit from '../popup/popupProjectEdit.js'


function SomeProject() {
const [popupOpen2, setPopupOpen2] = useState(false);
const [popupOpen3, setPopupOpen3] = useState(false);
  return (
    <div className="some-project-comp">
      <div className="banner-some-project">
        <h1 className="banner-heading-some-project">ШСА</h1>
        <h3 className='banner-data'>дедлайн: 00.00.00</h3>
        <h4 className='banner-text'>Школа студенческого актива — это мероприятие, направленное на повышение лидерских качеств и профессиональных навыков студентов. В рамках этой школы студенты учатся работать в команде, развивать навыки презентации, делового общения, планирования и реализации проектов. Программа включает в себя тренинги, семинары, мастер-классы, практические занятия и другие формы обучения. Школа студенческого актива способствует формированию профессионального сообщества активных и целеустремленных студентов.</h4>
      </div>
      <div className="some-project-comp-container">
        <div className="btn-edit-project">
            <div className="btns-create-some-proj">
                <button onClick={()=> setPopupOpen3(true)}>
                    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
                    </svg>
                    Редактировать проект
                </button>
            </div>
        </div>
        <div className="doc-container">
          <h2 className='header-some-proj'>Документы</h2>
          <div className="btns-create-some-proj">
            <button>
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
                </svg>
                Создать документ
            </button>
          </div>
        </div>
        <div className="events-container">
          <h2 className='header-some-proj'>Мероприятия</h2>
          <div className="btns-create-some-proj">
            <button onClick={()=> setPopupOpen2(true)}>
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 6.75H6.75V12H5.25V6.75H0V5.25H5.25V0H6.75V5.25H12V6.75Z" fill="white"/>
                </svg>
                Создать мероприятие
            </button>
          </div>
          <div className='box-w-proj-some'>
            <BoxEvent/>
            <BoxEvent/>
            <BoxEvent/>
          </div>
        </div>
      </div>
      <Popup2 
            isOpen={popupOpen2}
            onClose={()=> setPopupOpen2(false)}
            />  
      <PopupProjectEdit
            isOpen={popupOpen3}
            onClose={()=> setPopupOpen3(false)}/>
    </div>
  )
}

export default SomeProject;
