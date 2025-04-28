import React, { useState } from 'react';
import axios from 'axios';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage('');

    const data = new URLSearchParams();
    data.append('username', username);
    data.append('password', password);

    try {
      const response = await axios.post('http://localhost:8000/auth/login', data, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });

      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      setMessage('✅ Login successful!');
      if (onLogin) onLogin();
    } catch (error) {
      console.error(error);
      setMessage('❌ Invalid credentials');
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
        justifyContent: "center",
        alignItems: "center",
        padding: "2rem"
      }}
    >
      <div className="p-5 bg-white bg-opacity-80 rounded shadow" style={{ width: '450px' }}>
        <h2 className="text-center mb-4">Login</h2>
        <form onSubmit={handleLogin}>
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
          <button type="submit" className="btn btn-primary w-100 mb-3">
            Login
          </button>
          {message && (
            <p className={`text-center ${message.includes('❌') ? 'text-danger' : 'text-success'}`}>
              {message}
            </p>
          )}

          <p className="mt-4 text-center">
            Don't have an account?{' '}
            <a href="/register" className="text-primary" style={{ textDecoration: 'underline' }}>
              Register
            </a>
          </p>
        </form>
      </div>
    </div>
  );
}

export default Login;
