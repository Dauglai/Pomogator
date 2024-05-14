import React, { useContext } from 'react'
import AuthContext from '../context/AuthContext'
import './LoginPage.css'

const LoginPage = () => {

   let { loginUser } = useContext(AuthContext)

   return (
      <div className='login-page'>
         <div className='login-container'>
            <form onSubmit={loginUser} className='authlogin'>
               <h2 className='login-header'>Привет</h2>
               <input className='login-input' type="text" name="username" placeholder="Gmail" />
               <input className='login-input' type="password" name="password" placeholder="Password" />
               <p className='login-text'>Пароль можно получить через Союз студентов</p>
               <input className='login-btn' type="submit" value={'Войти'}/>
            </form>
         </div>
      </div>
   )
}

export default LoginPage