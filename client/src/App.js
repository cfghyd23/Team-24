import './App.css';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Landing from './pages/Landing/Landing';
import ActionAreaCard from './components/Alumni';
import { Routes, Route } from "react-router-dom";
import Regform from './pages/Regform/Regform';
import Userprofile from './pages/Profile/Userprofile';
import Certificate from './pages/Profile/Certificate';

function App() {
  return (
    <>
    <Routes>
      <Route exact path="/" element={<Landing />} />
      <Route exact path="/signin" element={<SignIn />} />
      <Route exact path="/signup" element={<SignUp />} />
      <Route exact path="/alumni" element={<ActionAreaCard />} />
      <Route exact path="/register" element={<Regform />} />
      <Route exact path='/userprofile' element={<Userprofile />} />
      <Route exact path='/certificate' element={<Certificate />} />
    </Routes>
    </>
  );
}

export default App;
