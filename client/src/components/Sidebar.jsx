import React from 'react';
import "../App.css"
import { SidebarData } from './SidebarData';

function Sidebar() {
  return (
    <div className="h-full w-full bg-blue-500">
        <ul className="h-full p-0 w-full">
            {SidebarData.map((val, key) => {
                return (
                    <li 
                        key={key} 
                        onClick={() => {window.location.pathname = val.link}}
                        className="flex items-center text-white cursor-pointer hover:bg-blue-600"
                        >
                            <span className="p-4">{val.icon}</span>
                            <span className="flex-1">{val.title}</span>
                    </li>
                )
            })}
        </ul>
    </div>
  )
};

export default Sidebar;
