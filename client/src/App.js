import './App.css';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Landing from './pages/Landing/Landing'

function App() {
  return (
    <>
    <SignIn/>
    <SignUp/>
    <div>
      <Landing />
    </div>
    </>
  );
}

export default App;
