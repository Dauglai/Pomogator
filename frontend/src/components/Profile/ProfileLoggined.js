import React, {useState} from 'react'
import './ProfileLoggined.css'

export default function ProfileUser() {
  const [changeCreditsFlag, changeCredits] = useState('nothing');
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  }
  
  if (changeCreditsFlag == 'nothing') {
    return (  
    <div className='profile-loggined-component'>
      <div className="banner">
        <h1 className="banner-heading">Проекты Союза Студентов</h1>
      </div>
      <div className='profile-loggined-content'>
        <h2 className='content-heading'>
          Основная информация
        </h2>
        <div className='content-container'>
          <div className='content-item'>
            <p>Имя</p>
              <span>
                Нет имени
              </span>
            <svg onClick={() => changeCredits('nameChange')} width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Дата рождения</p>
            <span>Дня рождения нет</span>
            <svg onClick={() => changeCredits('dateChange')} width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Академическая группа</p>
            <span>Группы нет</span>
            <svg onClick={() => changeCredits('groupChange')}  width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Должность</p>
            <span>Надо указать должность</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
        </div>
      </div>



      <div className='profile-loggined-content'>
        <h2 className='content-heading'>
          Контактная информация
        </h2>
        <div className='content-container'>
          <div className='content-item'>
            <p>Вконтакте</p>
            <span>Нуждается в ссылке</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Telegram</p>
            <span>Поделись ссылкой на профиль!</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Почта</p>
            <span>Почты нет</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Google почта</p>
            <p className='avaliable'>ivamov_ivan@gmail.com</p>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
    )
  } else if (changeCreditsFlag ==  'nameChange') {
    return (
      <div className='profile-loggined-component'>
        <div onClick={() => changeCredits('nothing')} className='profile-change-header'>
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 9.25H4.7875L11.775 2.2625L10 0.5L0 10.5L10 20.5L11.7625 18.7375L4.7875 11.75H20V9.25Z" fill="black"/>
          </svg>
          <h1 className='profile-change-heading'>Имя</h1>
        </div>
        <div className='input-container'>
          <span className='input-naming'>Имя</span>
          <input 
            placeholder='Имя'
            className='input'
            value={value}
            onChange={handleChange}
          />
          <span className='profile-change-caption'>Напишите полное имя, фамилию. Можно и отчество)</span>
        </div>
      </div>
    )
  } else if (changeCreditsFlag ==  'dateChange') {
    return (
      <div className='profile-loggined-component'>
        <div onClick={() => changeCredits('nothing')} className='profile-change-header'>
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 9.25H4.7875L11.775 2.2625L10 0.5L0 10.5L10 20.5L11.7625 18.7375L4.7875 11.75H20V9.25Z" fill="black"/>
          </svg>
          <h1 className='profile-change-heading'>Дата Рождения</h1>
        </div>
        <div className='input-container'>
          <span className='input-naming'>Мой др</span>
          <input 
            placeholder='Мой др...'
            className='input'
          />
          <span className='profile-change-caption'>Напишите полную дату</span>
        </div>
      </div>
    )
  } else if (changeCreditsFlag === 'groupChange') {
    return (
      <div className='profile-loggined-component'>
        <div onClick={() => changeCredits('nothing')} className='profile-change-header'>
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 9.25H4.7875L11.775 2.2625L10 0.5L0 10.5L10 20.5L11.7625 18.7375L4.7875 11.75H20V9.25Z" fill="black"/>
          </svg>
          <h1 className='profile-change-heading'>Академическая группа</h1>
        </div>
        <div className='input-container'>
          <span className='input-naming'>Моя академ. группа</span>
          <input 
            placeholder='РИ-000000'
            className='input'
          />
          <span className='profile-change-caption'>Напишите свою академическую группу</span>
        </div>
      </div>
    )
  }
}