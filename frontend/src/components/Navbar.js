import React from 'react';

const Navbar = ({ isLoggedIn, handleLogout, showLogin, showRegister }) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
      <div className="container-fluid">
        <a className="navbar-brand d-flex align-items-center" href="/">
          {/* Add your logo image */}
          <img
            src="/images/logo.jpeg"  // Make sure the image is placed inside public/images/logo.jpeg
            alt="Logo"
            width="40"
            height="40"
            className="d-inline-block align-text-top me-2"
          />
          <span className="fw-bold text-primary">Sentiment Music Recommender</span>
        </a>

        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll"
          aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarScroll">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {isLoggedIn && (
              <>
                <li className="nav-item">
                  <a className="nav-link active" href="/architecture.html" target="_blank" rel="noopener noreferrer">
                    Architecture & API
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/contact.html" target="_blank" rel="noopener noreferrer">
                    Contact
                  </a>
                </li>
              </>
            )}
          </ul>

          <div className="d-flex">
            {isLoggedIn ? (
              <button className="btn btn-outline-danger" onClick={handleLogout}>
                Logout
              </button>
            ) : (
              <>
                <button className="btn btn-outline-primary me-2" onClick={showLogin}>
                  Login
                </button>
                <button className="btn btn-outline-secondary" onClick={showRegister}>
                  Register
                </button>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
