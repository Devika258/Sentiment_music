import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './pages/Login';
import Register from './pages/Register';
import Playlist from './pages/Playlist';
import Navbar from './components/Navbar'; // 🔽 import your new Navbar

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) setIsLoggedIn(true);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsLoggedIn(false);
  };

  const showLogin = () => setShowRegister(false);
  const showReg = () => setShowRegister(true);

  return (
    <div>
      <Navbar
        isLoggedIn={isLoggedIn}
        handleLogout={handleLogout}
        showLogin={showLogin}
        showRegister={showReg}
      />

      <div className="container mt-5">
        {!isLoggedIn ? (
          <>
            {showRegister ? (
              <>
                <Register onRegister={() => setShowRegister(false)} />
                <p className="text-center mt-3">
                  Already have an account?{" "}
                  <button onClick={showLogin} className="btn btn-link">Login</button>
                </p>
              </>
            ) : (
              <>
                <Login onLogin={() => setIsLoggedIn(true)} />
                <p className="text-center mt-3">
                  Don't have an account?{" "}
                  <button onClick={showReg} className="btn btn-link">Register</button>
                </p>
              </>
            )}
          </>
        ) : (
          <Playlist />
        )}
      </div>
    </div>
  );
}

export default App;
