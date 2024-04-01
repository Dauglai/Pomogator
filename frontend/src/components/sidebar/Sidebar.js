import React from 'react';
import { NavLink } from 'react-router-dom';
import { BsCalendar3 } from "react-icons/bs";
import { BsPerson } from "react-icons/bs";
import { BsPeopleFill } from "react-icons/bs";
import { BsFillBrightnessHighFill } from "react-icons/bs";
import './Sidebar.css'



const Sidebar = ({children}) => {
    const menuItem=[
        {
    
            path:"/profile",
            name:"Мой профиль",
            icon:<BsPerson />
        },
        {
            path:"/tasks",
            name:"Задачи",
            icon:<BsFillBrightnessHighFill/>
        },
        {
            path:"/events",
            name:"Мероприятия",
            icon:<BsCalendar3/>
        },
        {
            path:"/team",
            name:"Команда",
            icon:<BsPeopleFill/>
        }, 
    ]
    return (
        <div className='box'>
            <div className='sidebar'>
                {
                    menuItem.map((item, index)=>(
                        <NavLink to={item.path} key={index} className="link">
                            <div className="icon">{item.icon}</div>
                            <div className='link_text'>{item.name}</div>
                        </NavLink>
                    ))
                }
            </div>
            <main>{children}</main>
        </div>
    );
};

export default Sidebar;