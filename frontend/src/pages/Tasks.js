import React, { useState } from 'react';
import './Tasks.css'
import Popup from '../components/popup/popupTasks.js' 
import BoxTasks from '../components/tasks/tasksTasks.js';

const Tasks = () => {
const [popupOpen, setPopupOpen] = useState(false);

    return (
        <div className='head-page-tasks'>
            <div className='main-title'>
                <h1 className='header-tasks'>Мои задачи</h1>
            </div>
            <div className='body-page-tasks'>
                <div className='box-process'>
                    <h1 className='header-tasks'>Процессуалка</h1>
                    <h4 className='subtitle-tasks'>Задачи, которые нужно назначить самостоятельно, не в рамках мероприятия</h4>
                    <button className='new-tasks-btn'
                    onClick={()=> setPopupOpen(true)}
                    >Создать задачу</button>
                </div>
                <div className='box-process'>
                    <h1 className='header-tasks'>Мероприятия</h1>
                    <h4 className='subtitle-tasks'>Задачи, которые назначаются в рамках работы над мероприятием</h4>
                </div>
                <div className='box-process'>
                    <h1 className='header-tasks'>Архив</h1>
                    <h4 className='subtitle-tasks'>Выполненные задачи</h4>
                </div>
                <BoxTasks/>
            </div>
            <Popup 
            isOpen={popupOpen}
            onClose={()=> setPopupOpen(false)}
            />
        </div>
    );
};


export default Tasks;