import React, { useState } from 'react';
import './popupEvents1.css'

const Popup1 = ({isOpen, onClose}) => {
    const onShadowClick = (event) => {
        if(event.target.classList.contains("popup-shadow")) onClose()
    }
    return (
        <>
            {isOpen &&(
                <div className='popup-task-component'>
                    <div className='popup-shadow' onClick={onShadowClick}></div>
                    <div className='popup-container'>
                        <form className='form-popup-task' action="#">
                            <div className='input-description-container'>                        
                                <span className='input-description-heading input-heading'>Название проекта</span>
                                <input className='input-popup' placeholder='Название' type="text" required/>
                            </div>
                            <div className='input-description-container'>
                                <input className='date, input-popup' placeholder='Дата' type='Date'/>
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
 
export default Popup1;