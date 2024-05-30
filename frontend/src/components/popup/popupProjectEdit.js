import React, { useState } from 'react';
import './popupProjectEdit.css'

const PopupProjectEdit = ({isOpen, onClose}) => {
    const onShadowClick = (event) => {
        if(event.target.classList.contains("popup-project-edit-shadow")) onClose()
    }
    return (
        <>
            {isOpen &&(
                <div className='popup-project-edit-component'>
                    <div className='popup-project-edit-shadow' onClick={onShadowClick}></div>
                    <div className='popup-project-edit-container'>
                        <form className='form-popup-task' action="#">
                            <div className='input-description-container'>                        
                                <span className='input-description-heading input-heading'>Название проекта</span>
                                <input className='input-popup' placeholder='Название' type="text" required/>
                            </div>
                            <div className='input-description-container'>
                                <input className='date, input-popup' type='Date'/>
                                <h5 className='data-text input-description-description'>DD.MM.YYYY</h5>                        
                            </div>
                            <div className='input-description-container'>
                                <input className='input-popup' placeholder='Описание' type="text" required/>
                                <span className='input-date-heading input-heading'>Описание</span>
                                <h5 className='input-description-description'>1-2 предложение, в которых поясняется смысл проекта</h5>                        
                            </div>

                            <div className='popup-btn-container'>
                                <button className='btn-popup' onClick={()=> onClose()}>Завершить редактирование</button>                      
                            </div>
                        </form>
                    </div>
                </div>
            )}    
        </>
    );
}
 
export default PopupProjectEdit;