import React, { useState } from "react";
import axios from "axios";
import "./App.css";

interface Recommendation {
  title: string;
  reason: string;
}

const App: React.FC = () => {
  const [movie_input, setMovieInput] = useState<string>("");
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMovieInput(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:8000/recommend", {
        movie: movie_input,
      });
      setRecommendations(response.data.recommended_movies);
      // console.log(recommendations);
    } catch (err) {
      setError("An error occurred while fetching recommendations.");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Movie Recommendation</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={movie_input}
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
            <strong>{rec.title}</strong>: {rec.explanation}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
