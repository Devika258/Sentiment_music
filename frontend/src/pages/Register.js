import React, { useState } from 'react';
import axios from 'axios';

function Register({ onRegister }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    setMessage('');

    try {
      const response = await axios.post('http://localhost:8000/auth/register', {
        username,
        password
      });

      setMessage('✅ Registration successful! You can now log in.');
      if (onRegister) onRegister();
    } catch (error) {
      console.error(error);
      if (error.response?.data?.detail === "Username already exists") {
        setMessage('⚠️ Username already taken. Try another.');
      } else {
        setMessage('❌ Registration failed. Please try again.');
      }
    }
  };

  return (
    <div
      style={{
        backgroundImage: "url('/images/newbackground.jpg')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "2rem"
      }}
    >
      <div className="p-5 bg-white bg-opacity-80 rounded shadow" style={{ width: '450px' }}>
        <h2 className="text-center mb-4">Register</h2>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label className="form-label">Username</label>
            <input
              type="text"
              className="form-control"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn btn-success w-100 mb-3">Register</button>

          {message && (
            <p className={`text-center ${message.includes('❌') ? 'text-danger' : 'text-success'}`}>
              {message}
            </p>
          )}

          <p className="mt-4 text-center">
            Already have an account?{' '}
            <a href="/login" className="text-primary" style={{ textDecoration: 'underline' }}>
              Login
            </a>
          </p>
        </form>
      </div>
    </div>
  );
}

export default Register;
