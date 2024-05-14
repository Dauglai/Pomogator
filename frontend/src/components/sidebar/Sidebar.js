import React from 'react';
import { NavLink } from 'react-router-dom';
import { CiPizza } from "react-icons/ci";
import { CiCalendar } from "react-icons/ci";
import { CiBoxList } from "react-icons/ci";
import { CiUser } from "react-icons/ci";
import './Sidebar.css'


const Sidebar = ({children}) => {
    const menuItem=[
        {
            path:"/profile",
            name:"Мой профиль",
            icon:<CiUser />
        },
        {
            path:"/tasks",
            name:"Задачи",
            icon:<CiBoxList />
        },
        {
            path:"/events",
            name:"Проекты",
            icon:<CiCalendar />
        },
        {
            path:"/team",
            name:"Команда",
            icon:<CiPizza />

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