// src/App.tsx
import React, { useState } from 'react';
import axios from 'axios';
import './App.css'
 
interface Recommendation {
  movie: string;
  explanation: string;
}
 
const App: React.FC = () => {
  const [movieInput, setMovieInput] = useState<string>('');
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
 
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMovieInput(event.target.value);
  };
 
  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('https://your-backend-url.com/recommend', { movie: movieInput });
      setRecommendations(response.data);
    } catch (err) {
      setError('An error occurred while fetching recommendations.');
    }
    setLoading(false);
  };
 
  return (
    <div className="container">
      <h1>Movie Recommendation</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={movieInput}
          onChange={handleInputChange}
          placeholder="Enter a movie"
          required
        />
        <button type="submit" disabled={loading}>
          Get Recommendations
        </button>
      </form>
 
      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">{error}</p>}
 
      <ul>
        {recommendations.map((rec, index) => (
          <li key={index}>
            <strong>{rec.movie}</strong>: {rec.explanation}
          </li>
        ))}
      </ul>
    </div>
  );
};
 
export default App;