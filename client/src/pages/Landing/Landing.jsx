import Navbar from '../../components/Navbar/Navbar'
import './landing.css'
const Landing = () => {
  return (
    <div className='landing'>
      <Navbar />
      <div className='top'>
        <span className='topSpan1'>CHANGE WITHIN TO CHANGE THE WORLD</span>
        <span className='topSpan2'>SUSTAINABLE DEVELOPMENT GOALS | VOLUNTEERING | ADVOCACY</span>
      </div>

      <div>
        <span className=''>About Us</span>
        <p>
          Marpu Foundation is steadfastly committed to advancing Sustainable Development Goals (SDGs)
          through strategic volunteering initiatives and advocacy efforts. Their mission is to harness the power
          of collective action to address global challenges, foster sustainable environments, and uplift
          communities. By promoting volunteerism, they empower individuals to make meaningful
          contributions to our shared goals. Furthermore, through advocacy, they strive to raise awareness,
          inspire action, and drive change at all levels. The approach of Marpu underscores the belief that each
          one of us has a pivotal role to play in the path to a sustainable future, and together, we can transform
          our world for the better.
        </p>
      </div>
    </div>
  )
}

export default Landing