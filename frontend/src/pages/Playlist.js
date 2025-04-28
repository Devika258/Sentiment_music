import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Playlist() {
  const [mood, setMood] = useState('');
  const [playlist, setPlaylist] = useState([]);
  const [message, setMessage] = useState('');
  const [credits, setCredits] = useState(null);
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(false);

  const token = localStorage.getItem('token');

  useEffect(() => {
    // Set background to body, like contact page
    document.body.style.backgroundImage = "url('/images/backgroung.jpg')";
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center';
    document.body.style.backgroundRepeat = 'no-repeat';
    document.body.style.minHeight = '100vh';

    // Cleanup on component unmount
    return () => {
      document.body.style.backgroundImage = '';
      document.body.style.backgroundSize = '';
      document.body.style.backgroundPosition = '';
      document.body.style.backgroundRepeat = '';
      document.body.style.minHeight = '';
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setPlaylist([]);

    if (!token) {
      setMessage('❌ You must be logged in to get a playlist.');
      return;
    }

    try {
      const response = await axios.post(
        'http://localhost:8000/api/mood/playlist',
        { mood },
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const { playlist, remaining_credits, mood: returnedMood } = response.data;
      setPlaylist(playlist || []);
      setCredits(remaining_credits);
      setMessage(`✅ Playlist for "${returnedMood}" mood:`);
    } catch (error) {
      console.error(error);
      if (error.response?.status === 403) {
        setMessage('❌ You are out of credits. Please upgrade your plan.');
        setCredits(0);
      } else {
        setMessage('❌ Failed to fetch playlist.');
      }
    }
  };

  const fetchHistory = async () => {
    if (!token) {
      setMessage('❌ You must be logged in to view history.');
      return;
    }

    try {
      const res = await axios.get('http://localhost:8000/api/mood/history', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      setHistory(res.data.history || []);
      setShowHistory(true);
    } catch (err) {
      console.error(err);
      setMessage('❌ Failed to load history.');
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        paddingTop: '6rem',
        paddingBottom: '2rem',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'flex-start'
      }}
    >
      <div className="container p-4 bg-white bg-opacity-80 rounded shadow" style={{ maxWidth: '700px' }}>
        <h2 className="text-center mb-4">Get Your Playlist</h2>

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Mood :</label>
            <input
              type="text"
              className="form-control"
              placeholder="Enter your mood"
              value={mood}
              onChange={(e) => setMood(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn btn-success w-100">Get Playlist</button>
        </form>

        {credits !== null && (
          <p className="mt-3 text-center text-muted">
            💳 <strong>{credits}</strong> credit{credits === 1 ? '' : 's'} remaining
          </p>
        )}

        {message && (
          <p className={`mt-3 text-center ${message.includes('❌') ? 'text-danger' : 'text-success'}`}>
            {message}
          </p>
        )}

        {playlist.length > 0 && (
          <ul className="list-group mt-3">
            {playlist.map((track, index) => (
              <li key={index} className="list-group-item">{track}</li>
            ))}
          </ul>
        )}

        <div className="text-center mt-4">
          <button className="btn btn-outline-primary" type="button" onClick={fetchHistory}>
            View History
          </button>
        </div>

        {showHistory && history.length > 0 && (
          <div className="mt-4">
            <h5 className="text-center">Your Playlist History</h5>
            <ul className="list-group">
              {history.map((entry, index) => (
                <li key={index} className="list-group-item">
                  <strong>{entry.mood}</strong> - {new Date(entry.timestamp).toLocaleString()}
                  <ul>
                    {entry.playlist.map((track, i) => (
                      <li key={i}>{track}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default Playlist;
