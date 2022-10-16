import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Navbar from './assets/NavBar'
import Home from './pages';
import Result from './pages/result'

function App() {
  return (
    <Home />
    // <Router>
    //   <Navbar />
    //   <Routes>
    //     <Route exact path='/' element={<Home/>} />
    //     <Route path='/result' element={<Result/>} />
    //   </Routes>
    // </Router>
  );
}

export default App;
