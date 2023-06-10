import './contactus.css'
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
import WhatsAppIcon from '@mui/icons-material/WhatsApp';

export default function ContactUs() {
  return (
    <div className='contactus'>
        <div className='contactus-first'>
            <span className='contactus-first-txt'>CONTACT US</span>
        </div>
        <div className='contactus-second'>
            <p><i className="support-Icon fa-solid fa-phone-flip"></i>Phone No. : +91-9991119898</p>
            <p><i className="support-Icon fa-solid fa-envelope"></i>Email</p>
            <p><i className="support-Icon fa-solid fa-message"></i>Connect for support</p>
        </div>
        <div className="contactus-third">
          <FacebookIcon className="contactus-Icon" />
          <TwitterIcon className="contactus-Icon" />
          <InstagramIcon className="contactus-Icon" />
          <WhatsAppIcon className="contactus-Icon" />
      </div>

    </div>
  )
}
