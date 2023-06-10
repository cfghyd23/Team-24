import './navbar.css'

const Navbar = () => {
  return (
    <div className='navbar'>
      <h1 className='navHeading'>Marpu Foundation</h1>
      <div className='btns'>
        <button className='navbtn'>Login</button>
        <button className='navbtn'>Register</button>
      </div>
    </div>
  )
}

export default Navbar