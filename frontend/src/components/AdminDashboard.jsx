import { useEffect, useState } from 'react';
import api from '../api';

function AdminDashboard() {
  // --- State Definitions ---
  const [series, setSeries] = useState([]);
  const [formData, setFormData] = useState({
    web_series_id: '', name: '', no_of_episodes: 0, release_date: '', language: '', description: ''
  });
  const [newUser, setNewUser] = useState({ username: '', password: '', email: '' });

  // --- Effects ---
  const fetchSeries = () => {
    api.get('series/').then(res => setSeries(res.data));
  };

  useEffect(fetchSeries, []);

  // --- Handlers ---
  const handleDelete = (id) => {
    if(window.confirm("Are you sure you want to delete this series?")) {
        api.delete(`series/${id}/`).then(fetchSeries);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('series/', formData)
        .then(() => {
            alert('Series Added Successfully');
            fetchSeries();
            setFormData({ web_series_id: '', name: '', no_of_episodes: 0, release_date: '', language: '', description: '' });
        })
        .catch(err => alert('Error: ' + JSON.stringify(err.response.data)));
  };

  const handleCreateUser = (e) => {
    e.preventDefault();
    api.post('register/', { ...newUser, role: 'customer' })
        .then(() => {
            alert('Customer Created Successfully!');
            setNewUser({ username: '', password: '', email: '' });
        })
        .catch(err => alert('Error creating user: ' + JSON.stringify(err.response?.data)));
  };

  // --- Single Return Statement ---
  return (
    <div>
      <h2 style={{ marginBottom: '20px' }}>Admin Dashboard</h2>

      {/* --- SECTION 1: User Registration --- */}
      <div className="card" style={{ marginBottom: '30px', borderLeft: '4px solid #2ecc71' }}>
        <div className="card-body">
            <h3 style={{ color: 'white', marginBottom: '15px' }}>Register New Customer</h3>
            <form onSubmit={handleCreateUser} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr auto', gap: '15px', alignItems: 'end' }}>
                <div className="form-group">
                    <label>Username</label>
                    <input 
                        value={newUser.username} 
                        onChange={e => setNewUser({...newUser, username: e.target.value})} 
                        required 
                    />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input 
                        type="password" 
                        value={newUser.password} 
                        onChange={e => setNewUser({...newUser, password: e.target.value})} 
                        required 
                    />
                </div>
                <div className="form-group">
                    <label>Email (Optional)</label>
                    <input 
                        type="email" 
                        value={newUser.email} 
                        onChange={e => setNewUser({...newUser, email: e.target.value})} 
                    />
                </div>
                <button type="submit" className="btn btn-primary" style={{ height: '42px', backgroundColor: '#2ecc71', border: 'none' }}>
                    Add User
                </button>
            </form>
        </div>
      </div>

      <hr style={{borderColor: '#333', margin: '40px 0'}} />

      {/* --- SECTION 2: Series Management --- */}
      <h3 style={{color: 'white', marginBottom: '15px'}}>Content Management System</h3>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '30px' }}>
        
        {/* Create Form */}
        <div className="card" style={{ height: 'fit-content' }}>
            <div className="card-body">
                <h3 style={{color: 'white', marginBottom: '15px'}}>Add New Series</h3>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Series ID</label>
                        <input placeholder="e.g. WS-999" value={formData.web_series_id} onChange={e => setFormData({...formData, web_series_id: e.target.value})} required />
                    </div>
                    <div className="form-group">
                        <label>Title</label>
                        <input placeholder="Series Name" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} required />
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                        <div className="form-group">
                            <label>Episodes</label>
                            <input type="number" value={formData.no_of_episodes} onChange={e => setFormData({...formData, no_of_episodes: e.target.value})} required />
                        </div>
                        <div className="form-group">
                            <label>Release Date</label>
                            <input type="date" value={formData.release_date} onChange={e => setFormData({...formData, release_date: e.target.value})} required />
                        </div>
                    </div>
                    <div className="form-group">
                        <label>Language</label>
                        <input placeholder="e.g. English" value={formData.language} onChange={e => setFormData({...formData, language: e.target.value})} required />
                    </div>
                    <div className="form-group">
                        <label>Description</label>
                        <textarea rows="3" value={formData.description} onChange={e => setFormData({...formData, description: e.target.value})} />
                    </div>
                    <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>Publish Series</button>
                </form>
            </div>
        </div>

        {/* List Table */}
        <div className="table-container">
            <h3 style={{color: 'white', marginBottom: '15px'}}>Series Database</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Rel. Date</th>
                        <th>Ep</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {series.map(s => (
                        <tr key={s.web_series_id}>
                            <td style={{ fontFamily: 'monospace', color: '#888' }}>{s.web_series_id}</td>
                            <td style={{ fontWeight: 'bold' }}>{s.name}</td>
                            <td>{s.release_date}</td>
                            <td>{s.no_of_episodes}</td>
                            <td>
                                <button onClick={() => handleDelete(s.web_series_id)} className="btn btn-small btn-danger">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
      </div>
    </div>
  );
}
export default AdminDashboard;