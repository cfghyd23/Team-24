import "./aboutus.css";

const Aboutus = () => {
  return (
    <>
      <div className="aboutus">
        <div className="aboutus-left">
          <span className="aboutus-left-head">About Us</span>
          <p className="aboutus-left-para">
            Marpu Foundation is steadfastly committed to advancing Sustainable
            Development Goals (SDGs) through strategic volunteering initiatives
            and advocacy efforts. Their mission is to harness the power of
            collective action to address global challenges, foster sustainable
            environments, and uplift communities. By promoting volunteerism,
            they empower individuals to make meaningful contributions to our
            shared goals. Furthermore, through advocacy, they strive to raise
            awareness, inspire action, and drive change at all levels. The
            approach of Marpu underscores the belief that each one of us has a
            pivotal role to play in the path to a sustainable future, and
            together, we can transform our world for the better.
          </p>
        </div>
        <div className="aboutus-right">
          <img
            src={
              "https://static.wixstatic.com/media/2cdbfc_cf1b36190dfc46598c48c7606bbc008a~mv2.jpg/v1/fill/w_1895,h_877,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/2cdbfc_cf1b36190dfc46598c48c7606bbc008a~mv2.jpg"
            }
            alt=""
            className="aboutus-img"
          />
        </div>
      </div>
    </>
  );
};

export default Aboutus;
