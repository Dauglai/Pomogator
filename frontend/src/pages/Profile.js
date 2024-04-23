import React from 'react'
import ProfileUser from '../components/Profile/ProfileUser'
import ProfileLoggined from '../components/Profile/ProfileLoggined'
import './Profile.css'

const Profile = () => {
    // const isLoggined = false;
    // if (isLoggined) {
    //     return <ProfileLoggined />
    // } else {
    //     <ProfileUser />
    // }
    return (
        <div className='profile-page'>
            {/* <ProfileUser /> */}
            <ProfileLoggined />
        </div>
    );
};

export default Profile;