import './App.css';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Landing from './pages/Landing/Landing';
import { Routes, Route } from "react-router-dom";
;
function App() {
  return (
    <>
    <Routes>
      <Route exact path="/" element={<Landing />} />
      <Route path="/signin" element={<SignIn />} />
      <Route exact path="/signup" element={<SignUp />} />
    </Routes>
    </>
  );
}

export default App;
