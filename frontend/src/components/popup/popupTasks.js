import React, { useState } from 'react';
import './popupTask.css'

function Popup() {

    return (
        <div className='box-popup'>
            <h2>Создай новую задачу</h2>
            <h4>Процессуальные задачи - это задачи, которые мы выполняем по определенным дням. Будь внимателен, заполни свое расписание правильно. </h4>
            <form action="#">
                <input className='imput-popup' placeholder='Название' type="text" required/>
                <input className='imput-popup' placeholder='Описание' type="text" required/>
                <h5>По необходимости напиши буквально 1-2 предложения</h5>
                <input className='date, imput-popup' type='Date'/>
                <label for="" placeholder="Дата" alt="Дата"></label>
                <h5 className='data-text'>DD.MM.YYYY</h5>
                <button className='btn-popup'>Закрыть</button>
                <button className='btn-popup'>Создать</button>
            </form>     
        </div>
    );
}
 
export default Popup;