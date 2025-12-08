import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api';

function CustomerDashboard() {
  const [series, setSeries] = useState([]);

  useEffect(() => {
    api.get('series/').then(res => setSeries(res.data)).catch(console.error);
  }, []);

  return (
    <div>
      <h2 style={{ marginBottom: '20px', borderLeft: '4px solid var(--brand-red)', paddingLeft: '10px' }}>Trending Now</h2>
      <div className="grid">
        {series.map(s => (
          <div key={s.web_series_id} className="card">
            {/* Placeholder for Poster Image - uses a gray block if no image */}
            <div style={{ height: '140px', backgroundColor: '#333', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#555' }}>
               <span>POSTER</span>
            </div>
            <div className="card-body">
              <div>
                <h3 className="card-title">{s.name}</h3>
                <p style={{ fontSize: '0.9rem', display: '-webkit-box', WebkitLineClamp: '3', WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
                  {s.description}
                </p>
                <div style={{ marginTop: '10px', display: 'flex', gap: '10px', fontSize: '0.8rem', color: '#999' }}>
                   <span>{s.no_of_episodes} Episodes</span>
                   <span>• {s.language}</span>
                </div>
              </div>
              <Link to={`/customer/series/${s.web_series_id}`} style={{ marginTop: '15px' }}>
                <button className="btn btn-primary" style={{ width: '100%' }}>Watch Now</button>
              </Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
export default CustomerDashboard;