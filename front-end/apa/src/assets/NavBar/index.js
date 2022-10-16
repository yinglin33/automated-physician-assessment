import React from "react";
import { Nav, NavLink, NavMenu } 
    from "./NavbarElements";
  
const Navbar = () => {
  return (
    <>
      <Nav>
        <NavMenu>
          <NavLink to="./pages/" activeStyle>
            Home
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};
  
export default Navbar;