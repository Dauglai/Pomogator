import React from 'react'
import './ProfileLoggined.css'

export default function ProfileUser() {
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
            <span>Имени нет</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Дата рождения</p>
            <span>Дня рождения нет</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.31371 1.99977L12.6274 13.3135L1.31371 24.6272" stroke="#474647" stroke-width="3"/>
            </svg>
          </div>
          <div className='content-item'>
            <p>Академическая группа</p>
            <span>Группы нет</span>
            <svg width="15" height="26" viewBox="0 0 15 26" fill="none" xmlns="http://www.w3.org/2000/svg">
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
}