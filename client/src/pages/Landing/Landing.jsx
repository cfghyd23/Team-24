import Navbar from '../../components/Navbar/Navbar'
import ContactUs from '../../components/Contactus/Contactus'
import './landing.css'
import Aboutus from '../../components/Aboutus/Aboutus'

const Landing = () => {
  return (
    <div className='landing'>
      <Navbar />
      <div className='top'>
        <span className='topSpan1'>CHANGE WITHIN TO CHANGE THE WORLD</span>
        <span className='topSpan2'>SUSTAINABLE DEVELOPMENT GOALS | VOLUNTEERING | ADVOCACY</span>
      </div>
      <Aboutus />
      <ContactUs />
    </div>
  )
}

export default Landing