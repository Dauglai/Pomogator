import React, { useState, useEffect, useContext } from 'react'
import AuthContext from '../context/AuthContext';
import '../App.css'
const HomePage = () => {
   const { authTokens, logoutUser } = useContext(AuthContext);
   let [profile, setProfile] = useState([])

   useEffect(() => {
      getProfile()
      // eslint-disable-next-line no-use-before-define, react-hooks/exhaustive-deps
   }, [])

   // eslint-disable-next-line react-hooks/exhaustive-deps
   const getProfile = async () => {
      let response = await fetch('/accounts/profile/', {
         method: 'GET',
         headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + String(authTokens.access)
         }
      })
      let data = await response.json()
      console.log(data)
      if (response.status === 200) {
         setProfile(data)
      } else if (response.statusText === 'Unauthorized') {
         logoutUser()
      }
   }

   return (
      <div className='authlogin'>
         <p>You are logged in to the homepage!</p>
         <p>Name: {profile.first_name} {profile.last_name}</p>
         <p>Email: {profile.gmail}</p>
      </div>
   )
}

export default HomePage