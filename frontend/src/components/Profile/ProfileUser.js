import React from 'react'
import './ProfileUser.css'

export default function ProfileUser() {
  return (
    <div className='profile-user-component'>
      <div className='img-info'></div>
      <div className='personal-info'>
        <div className='personal-info-container'>
          <h2>Иванов Иван Иванович</h2>
          <p>29.02.2003</p>
        </div>
        <p className='info'>заместитель председателя, культурно-массовая комиссия</p>
        <p className='group'>РИ-318743</p>
      </div>
      <h3 className='btn-container-header'>Мои контакты</h3>
      <div className='btn-container'>
        <button>
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M26.14 0H13.86C2.66 0 0 2.66 0 13.86V26.14C0 37.34 2.66 40 13.86 40H26.14C37.34 40 40 37.34 40 26.14V13.86C40 2.66 37.34 0 26.14 0ZM32.3 28.54H29.38C28.28 28.54 27.94 27.64 26 25.66C24.24 24 23.48 23.76 23.06 23.76C22.48 23.76 22.3 23.92 22.3 24.76V27.38C22.3 28.08 22.08 28.52 20.22 28.52C17.14 28.52 13.72 26.64 11.32 23.18C7.7 18.1 6.72 14.26 6.72 13.5C6.72 13.08 6.86 12.68 7.7 12.68H10.64C11.38 12.68 11.66 13 11.94 13.8C13.38 18 15.78 21.6 16.76 21.6C17.14 21.6 17.3 21.42 17.3 20.5V16.2C17.2 14.24 16.14 14.06 16.14 13.36C16.14 13 16.42 12.68 16.88 12.68H21.46C22.08 12.68 22.3 13 22.3 13.76V19.54C22.3 20.16 22.56 20.38 22.76 20.38C23.12 20.38 23.44 20.16 24.1 19.48C26.2 17.14 27.7 13.52 27.7 13.52C27.9 13.1 28.22 12.7 29 12.7H31.86C32.74 12.7 32.94 13.16 32.74 13.78C32.38 15.48 28.82 20.5 28.86 20.5C28.54 21 28.42 21.22 28.86 21.8C29.16 22.22 30.18 23.1 30.86 23.88C32.1 25.3 33.06 26.48 33.32 27.3C33.54 28.12 33.14 28.54 32.3 28.54Z" fill="black"/>
          </svg>
          <div className='btn-item-description'>
            <p>Вконтакте</p>
            <p>ivanov_ivan</p>            
          </div>
        </button>
        <button>
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 0C8.95097 0 0 8.95226 0 20C0 31.0477 8.95226 40 20 40C31.049 40 40 31.0477 40 20C40 8.95226 31.0477 0 20 0ZM29.8232 13.7019L26.5406 29.1703C26.2981 30.2671 25.6452 30.5329 24.7342 30.0168L19.7342 26.3316L17.3226 28.6542C17.0568 28.92 16.831 29.1458 16.3148 29.1458L16.6697 24.0568L25.9355 15.6852C26.3394 15.3303 25.8465 15.129 25.3135 15.4839L13.8619 22.6929L8.92645 21.1523C7.85419 20.8142 7.82968 20.08 9.15226 19.5639L28.4348 12.1277C29.3303 11.8052 30.1123 12.3458 29.8219 13.7006L29.8232 13.7019Z" fill="black"/>
          </svg>
          <div className='btn-item-description'>
            <p>Телеграм</p>
            <p>ivanov_ivan</p>            
          </div>
        </button>
        <button>
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M40 33.3332C40 34.5023 39.7533 35.5862 39.3582 36.5399L26.7286 17.6989L39.2213 3.12552C39.7073 4.1538 40 5.36168 40 6.66696V33.3332ZM20 21.1198L37.3832 0.839992C36.6699 0.319311 35.8666 0 35.0001 0H4.99997C4.13239 0 3.32886 0.319311 2.61841 0.839992L20 21.1198ZM24.8463 19.8929L20.8226 24.5902C20.5873 24.8635 20.2942 25.0001 20 25.0001C19.7057 25.0001 19.4127 24.8635 19.1773 24.5902L15.1527 19.8927L2.36326 38.9746C3.12985 39.6158 4.02827 40 4.99989 40H35.0001C35.9716 40 36.8704 39.6158 37.6367 38.9746L24.8463 19.8929ZM0.778878 3.12541C0.292986 4.15369 0 5.36157 0 6.66696V33.3333C0 34.5025 0.245501 35.5864 0.642112 36.54L13.2703 17.6957L0.778878 3.12541Z" fill="black"/>
          </svg>
          <div className='btn-item-description'>
            <p>Mail</p>
            <p>ivanov_ivan</p>          
          </div>
        </button>
        <button>
          <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M36 0H4C1.8 0 0 2.25 0 5V35C0 37.75 1.8 40 4 40H36C38.2 40 40 37.75 40 35V5C40 2.25 38.2 0 36 0ZM36 35H32V13L20 22.5L8 13V35H4V5H6.4L20 15.5L33.6 5H36V35Z" fill="black"/>
          </svg>
          <div className='btn-item-description'>
            <p>Gmail</p>
            <p>ivanov_ivan</p>
          </div>
        </button>
      </div>
    </div>
  )
}
