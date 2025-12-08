import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../api';

function SeriesDetail() {
  const { id } = useParams();
  const [series, setSeries] = useState(null);
  const [episodes, setEpisodes] = useState([]);
  const [feedback, setFeedback] = useState('');
  const [rating, setRating] = useState(5);

  useEffect(() => {
    api.get(`series/${id}/`).then(res => setSeries(res.data));
    api.get('episodes/').then(res => {
        // Simple filter on client side for now
        setEpisodes(res.data.filter(ep => ep.web_series === id));
    });
  }, [id]);

  const submitFeedback = () => {
    if (rating <= 2 && !feedback) {
        alert("Please provide a reason for the low rating.");
        return;
    }
    const payload = {
        account: "ACC001", // Hardcoded Viewer
        web_series: id,
        feedback_text: feedback,
        rating: rating,
        feedback_date: new Date().toISOString().split('T')[0]
    };
    api.post('feedback/', payload)
       .then(() => { alert('Thank you for your feedback!'); setFeedback(''); })
       .catch(err => alert('Failed to submit. Check console.'));
  };

  if (!series) return <div style={{textAlign: 'center', marginTop: '50px'}}>Loading content...</div>;

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto' }}>
      <Link to="/customer" style={{ color: '#999', marginBottom: '20px', display: 'block' }}>← Back to Browse</Link>
      
      {/* Series Header */}
      <div style={{ marginBottom: '40px' }}>
        <h1 style={{ fontSize: '3rem', marginBottom: '10px' }}>{series.name}</h1>
        <div style={{ display: 'flex', gap: '20px', color: '#b3b3b3', fontSize: '1.1rem', marginBottom: '20px' }}>
            <span>{new Date(series.release_date).getFullYear()}</span>
            <span>{series.language}</span>
            <span style={{ border: '1px solid #666', padding: '0 5px', borderRadius: '2px', fontSize: '0.9rem' }}>HD</span>
        </div>
        <p style={{ fontSize: '1.2rem', maxWidth: '700px', color: '#fff' }}>{series.description}</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '40px' }}>
        
        {/* Left Column: Episodes */}
        <div>
          <h2 style={{ borderBottom: '1px solid #333', paddingBottom: '10px', marginBottom: '20px' }}>Episodes</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {episodes.map(ep => (
              <div key={ep.episode_id} style={{ display: 'flex', alignItems: 'center', padding: '15px', backgroundColor: '#222', borderRadius: '4px', transition: '0.2s' }}>
                <span style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#555', marginRight: '20px' }}>{ep.episode_number}</span>
                <div>
                  <h4 style={{ margin: 0, color: 'white' }}>{ep.episode_title}</h4>
                  <span style={{ fontSize: '0.9rem', color: '#888' }}>{ep.duration_minutes}m</span>
                </div>
                <div style={{ marginLeft: 'auto' }}>
                    <button className="btn btn-small btn-secondary">▶</button>
                </div>
              </div>
            ))}
            {episodes.length === 0 && <p>No episodes available yet.</p>}
          </div>
        </div>

        {/* Right Column: Feedback */}
        <div style={{ backgroundColor: '#1f1f1f', padding: '20px', borderRadius: '8px', height: 'fit-content' }}>
          <h3>Rate this Series</h3>
          <div className="form-group">
            <label>Rating (1-5)</label>
            <select value={rating} onChange={e => setRating(parseInt(e.target.value))}>
                {[1,2,3,4,5].map(n => <option key={n} value={n}>{n} Stars</option>)}
            </select>
          </div>
          <div className="form-group">
            <label>Comment {rating <= 2 && <span style={{color: 'var(--brand-red)'}}>*</span>}</label>
            <textarea 
                rows="4"
                placeholder="What did you think?" 
                value={feedback} 
                onChange={e => setFeedback(e.target.value)} 
            />
          </div>
          <button onClick={submitFeedback} className="btn btn-primary" style={{ width: '100%' }}>Submit Review</button>
        </div>

      </div>
    </div>
  );
}
export default SeriesDetail;