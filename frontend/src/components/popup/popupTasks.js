import React, { useState } from 'react';
import './popupTask.css'

const Popup = ({isOpen, onClose}) => {
    const onShadowClick = (event) => {
        if(event.target.classList.contains("popup-shadow")) onClose()
    }
    return (
        <>
            {isOpen &&(
                <div className='popup-task-component'>
                    <div className='popup-shadow' onClick={onShadowClick}></div>
                    <div className='popup-container'>
                        <h2 className='heading'>Создай новую задачу</h2>
                        <h4 className='heading-description'>Процессуальные задачи - это задачи, которые мы выполняем по определенным дням. Будь внимателен, заполни свое расписание правильно. </h4>
                        <form className='form-popup-task' action="#">
                            <div className='input-description-container'>                        
                                <span className='input-description-heading input-heading'>Название</span>
                                <input className='input-popup' placeholder='Название' type="text" required/>
                            </div>
                            <div className='input-description-container'>
                                <input className='input-popup' placeholder='Описание' type="text" required/>
                                <span className='input-date-heading input-heading'>Описание</span>
                                <h5 className='input-description-description'>По необходимости напиши буквально 1-2 предложения</h5>                        
                            </div>
                            <div className='input-description-container'>
                                <input className='date, input-popup' type='Date'/>
                                <h5 className='data-text input-description-description'>DD.MM.YYYY</h5>                        
                            </div>
                            <div className='popup-btn-container'>
                                <button className='btn-popup' onClick={()=> onClose()}>Закрыть</button>
                                <button className='btn-popup'>Создать</button>                        
                            </div>
                        </form>
                    </div>
                </div>
            )}    
        </>
    );
}
 
export default Popup;