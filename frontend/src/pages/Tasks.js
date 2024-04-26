import React from 'react';
import './Tasks.css'
import '../components/popup/popupTasks.js' 

const Tasks = () => {
    return (
        <div className='page'>
            <div className='main-title'>
                <h1>Мои задачи</h1>
            </div>
            <div className='box-process'>
                <h1>Процессуалка</h1>
                <h4>Задачи, которые нужно назначить самостоятельно, не в рамках мероприятия</h4>
                <button>Создать задачу</button>
            </div>

        </div>
    );
};

export default Tasks;