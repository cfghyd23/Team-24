import React, { useState } from 'react';
import './styles.css';
import logo from './1.jpg';
import { Link } from "react-router-dom"
import Success from './success';

const Form = () => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [gender, setGender] = useState('');
  const [dob, setDob] = useState('');
  const [phone, setPhone] = useState('');
  const [state, setState] = useState('');
  const [city, setCity] = useState('');
  const [education, setEducation] = useState('');
  const [internshipType, setInternshipType] = useState('');
  const [internshipRole, setInternshipRole] = useState('');
  const [aboutYou, setAboutYou] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    console.log('Form submitted:', {
      email,
      name,
      gender,
      dob,
      phone,
      state,
      city,
      education,
      internshipType,
      internshipRole,
      aboutYou
    });
    // Reset form fields
    setEmail('');
    setName('');
    setGender('');
    setDob('');
    setPhone('');
    setState('');
    setCity('');
    setEducation('');
    setInternshipType('');
    setInternshipRole('');
    setAboutYou('');
  };

  return (
    <>
    <h1 className="form-heading"> Application Form </h1>
    <form className="form-container" onSubmit={handleSubmit} action={<Link to={Success} />}>
    <img src={logo} alt="Logo" className="form-logo" />
      <label className="form-label">
        Email:
        <input
          className="form-input"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Name:
        <input
          className="form-input"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Gender:
        <label className="form-radio-label">
          Male
        </label>
        <input
            className="form-radio-input"
            type="radio"
            value="male"
            checked={gender === 'male'}
            onChange={() => setGender('male')}
            required
          />
        <label className="form-radio-label">
          Female
        </label>
        <input
            className="form-radio-input"
            type="radio"
            value="female"
            checked={gender === 'female'}
            onChange={() => setGender('female')}
            required
          />
        <label className="form-radio-label">
          Other
        </label>
        <input
            className="form-radio-input"
            type="radio"
            value="other"
            checked={gender === 'other'}
            onChange={() => setGender('other')}
            required
          />
      </label>
        <br/>
      <label className="form-label">
        Date of Birth:
        <input
          className="form-input"
          type="date"
          value={dob}
          onChange={(e) => setDob(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Phone Number:
        <input
          className="form-input"
          type="tel"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        State:
        <input
          className="form-input"
          type="text"
          value={state}
          onChange={(e) => setState(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        City:
        <input
          className="form-input"
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Education:
        <input
          className="form-input"
          type="text"
          value={education}
          onChange={(e) => setEducation(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Internship Type:
        <label className="form-radio-label">
          In-person
        </label>
        <input
            className="form-radio-input"
            type="radio"
            value="inperson"
            checked={internshipType === 'inperson'}
            onChange={() => setInternshipType('inperson')}
            required
          />
        <label className="form-radio-label">
          Virtual
        </label>
        <input
            className="form-radio-input"
            type="radio"
            value="virtual"
            checked={internshipType === 'virtual'}
            onChange={() => setInternshipType('virtual')}
            required
          />
      </label>

      <br />

      <label className="form-label">
        Internship Role:
        <input
          className="form-input"
          type="text"
          value={internshipRole}
          onChange={(e) => setInternshipRole(e.target.value)}
          required
        />
      </label>

      <label className="form-label">
        Tell us about you:
        <textarea
          className="form-textarea"
          value={aboutYou}
          onChange={(e) => setAboutYou(e.target.value)}
          required
        />
      </label>

      <button type="submit" className="form-submit-btn">Submit</button>
    </form>
    </>
  );
};

export default Form;
