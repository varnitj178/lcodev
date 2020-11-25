import React from 'react'
import Menu from './Menu';

const Base =({
    title = " my title",
    description = "MY descrioption",
    className = "bg-dark text-white p-4",
    children
}) => {   
    return (
      <div>
        <Menu/>
        <div className="container-fluid">
          <div className="jumbotron bg-dark text-white text-center">
            <h2 className="display-4">{title}</h2>
            <h2 className="lead">{description}</h2>
          </div>
          <div className="{className}">{children}</div>
        </div>
        <footer className="footer bg-dark mt-ato py-3">
          <div className="container-fluid bg-success text-white text-center py-3">
            <h4> If you got any question reach me out at Instagram</h4>
            <button className="btn btn-warning btn-lg">Contact us</button>
            <div className="container">
              <span className="text-warning">
                 An Amazing Django React Fullstack
              </span>
            </div>
          </div>
        </footer>
      </div>
    );
} 

export default Base;