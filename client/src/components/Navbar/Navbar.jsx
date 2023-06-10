import "./navbar.css";
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div className="navbar">
      <h1 className="navHeading">Marpu Foundation</h1>
      <div className="btns">
        <Link to={`/signin`} >
          <button className="navbtn">Login</button>
        </Link>
        <Link to={`/signup`} >
          <button className="navbtn">Register</button>
        </Link>
        <Link to={`/alumni`} >
          <button className="navbtn">Alumni Connect</button>
        </Link>
      </div>
    </div>
  );
};

export default Navbar;
